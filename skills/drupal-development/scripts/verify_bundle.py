#!/usr/bin/env python3
"""Verify the preserved Drupal standards and their complete navigation index."""

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path, PurePosixPath
from zipfile import BadZipFile, ZipFile


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def headings(data):
    """Index literal ATX headings, even after malformed upstream fences."""
    result = []
    for line_number, line in enumerate(data.decode("utf-8").splitlines(), 1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if match:
            result.append({
                "line": line_number,
                "level": len(match.group(1)),
                "text": match.group(2),
            })
    return result


def slug(text):
    return re.sub(r"[^\w\s-]", "", text.lower()).replace(" ", "-")


def cell(text):
    return text.replace("|", "\\|").replace("\n", " ")


def render_source_map(manifest):
    """Render a deterministic contents page without modifying original files."""
    entries = manifest["files"]
    section_count = sum(len(entry.get("headings", [])) for entry in entries)
    document_count = sum(entry["path"].endswith(".md") for entry in entries)
    lines = [
        "# Complete source map", "",
        f"Preserve all {len(entries)} original files ({document_count} Markdown "
        f"documents), {manifest['total_bytes']:,} bytes, and {section_count} "
        "literal section headings from `coding_standards-main.zip`.", "",
        "Use this page as the table of contents for the unmodified originals. "
        "Source line numbers are one-based and support bounded reads even when "
        "upstream Markdown has malformed fences. Read all relevant sections, "
        "not just the headings. See `compatibility.md` for source limitations.", "",
        "## Contents", "",
    ]
    for entry in entries:
        name = entry["path"]
        lines.append(f"- [{name}](#{slug(name)})")
    lines += ["", "## Original files and section contents", ""]
    for entry in entries:
        name = entry["path"]
        lines += [f"## {name}", "",
                  f"[Read the original file](standards/{name}) — "
                  f"{entry['bytes']:,} bytes.", ""]
        sections = entry.get("headings", [])
        if sections:
            lines += ["| Section | Heading level | Source line |",
                      "| --- | --- | --- |"]
            for section in sections:
                lines.append(f"| {cell(section['text'])} | "
                             f"{section['level']} | {section['line']} |")
            lines.append("")
        elif name.endswith(".png"):
            lines += ["Retain this original image and its source-relative path.", ""]
        else:
            lines += ["Read the entire file; it has no ATX section headings.", ""]
    return "\n".join(lines).rstrip() + "\n"


def local_links(text):
    for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        target = match.group(1).split("#", 1)[0]
        if target and not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
            yield target


def verify(root, archive=None):
    errors = []
    manifest = json.loads((root / "references/source-manifest.json").read_text())
    entries = manifest["files"]
    paths = [entry["path"] for entry in entries]
    expected = set(paths)
    if len(expected) != len(paths):
        errors.append("Duplicate manifest paths")
    if paths != sorted(paths):
        errors.append("Manifest paths are not sorted")
    if len(paths) != manifest["file_count"]:
        errors.append("Manifest file count differs")
    if sum(entry["bytes"] for entry in entries) != manifest["total_bytes"]:
        errors.append("Manifest total bytes differ")

    source_root = root / "references/standards"
    actual = set()
    for path in source_root.rglob("*"):
        if path.is_symlink():
            errors.append(f"Unexpected symlink: {path.relative_to(source_root)}")
        if path.is_file():
            actual.add(path.relative_to(source_root).as_posix())
    for name in sorted(expected - actual):
        errors.append(f"Missing source file: {name}")
    for name in sorted(actual - expected):
        errors.append(f"Unlisted source file: {name}")

    for entry in entries:
        name = entry["path"]
        pure = PurePosixPath(name)
        if pure.is_absolute() or ".." in pure.parts:
            errors.append(f"Unsafe manifest path: {name}")
            continue
        path = source_root / name
        if not path.is_file() or path.is_symlink():
            continue
        data = path.read_bytes()
        if len(data) != entry["bytes"] or sha256(data) != entry["sha256"]:
            errors.append(f"Source bytes/hash mismatch: {name}")
        if name.endswith(".md") and headings(data) != entry.get("headings", []):
            errors.append(f"Source heading index mismatch: {name}")

    map_path = root / "references/source-map.md"
    if map_path.read_text() != render_source_map(manifest):
        errors.append("Source map is incomplete or differs from its manifest")

    skill_text = (root / "SKILL.md").read_text()
    direct = set(local_links(skill_text))
    for name in paths:
        if not name.endswith(".png") and f"references/standards/{name}" not in direct:
            errors.append(f"Source is not directly routed from SKILL.md: {name}")

    authored_docs = [root / "SKILL.md", root / "references/compatibility.md",
                     root / "references/review-and-validation.md", map_path,
                     root / "references/sonar-guidance.md", root / "references/sonar/index.md"]
    for path in authored_docs:
        for target in local_links(path.read_text()):
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f"Broken/escaping authored link: {path.name}: {target}")

    # Cross-check the source site's complete navigation without parsing !ENV YAML.
    navigation = (source_root / "mkdocs.yml").read_text()
    for target in re.findall(r":\s+([^\s]+\.md)\s*$", navigation, re.MULTILINE):
        if f"docs/{target}" not in expected:
            errors.append(f"MkDocs navigation target missing: {target}")

    if archive is not None:
        archive_path = Path(archive)
        if sha256(archive_path.read_bytes()) != manifest["archive_sha256"]:
            errors.append("Archive SHA-256 differs from the supplied source archive")
        with ZipFile(archive_path) as source:
            prefix = manifest["archive_root"] + "/"
            zipped = {}
            for item in source.infolist():
                if item.is_dir():
                    continue
                if not item.filename.startswith(prefix):
                    errors.append(f"Unexpected archive root: {item.filename}")
                    continue
                name = item.filename[len(prefix):]
                if name in zipped:
                    errors.append(f"Duplicate archive entry: {name}")
                zipped[name] = source.read(item)
            if set(zipped) != expected:
                errors.append("Archive and manifest file sets differ")
            for name in sorted(expected & set(zipped)):
                path = source_root / name
                if not path.is_file() or path.read_bytes() != zipped[name]:
                    errors.append(f"Archive byte comparison failed: {name}")
            if source.comment.decode("utf-8") != manifest["source_revision"]:
                errors.append("Archive revision comment differs")

    sonar_path = root / "scripts/sonar_rules.py"
    if not sonar_path.is_file():
        errors.append("Missing Sonar rule lookup/verifier")
    else:
        spec = importlib.util.spec_from_file_location("sonar_rules", sonar_path)
        sonar = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sonar)
        errors.extend(sonar.verify(root))

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    document_count = sum(name.endswith(".md") for name in paths)
    section_count = sum(len(entry.get("headings", [])) for entry in entries)
    print(f"PASS: {len(paths)} files, {document_count} Markdown documents, "
          f"{section_count} section headings, {manifest['total_bytes']:,} source bytes")
    print("PASS: source hashes, complete index, direct routes, authored links, and site navigation")
    print("PASS: complete Sonar exports, descriptions, framework contexts, manifest, and index")
    if archive is not None:
        print("PASS: archive hash, revision, full file set, and every file byte-for-byte")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, help="Original standards ZIP for an independent byte comparison")
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        return verify(args.skill_root, args.archive)
    except (OSError, ValueError, KeyError, TypeError, UnicodeError, BadZipFile) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
