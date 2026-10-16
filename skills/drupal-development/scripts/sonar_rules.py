#!/usr/bin/env python3
"""Inspect and verify the complete user-supplied Sonar way rule snapshot offline."""

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from html import escape
from html.parser import HTMLParser
from pathlib import Path

EXPORTS = {"php.json": "php", "html.json": "Web", "css.json": "css", "js.json": "javascript"}
LANGUAGES = {"php": "php", "html": "Web", "web": "Web", "css": "css",
             "js": "javascript", "javascript": "javascript"}
TYPES = {"CODE_SMELL", "BUG", "VULNERABILITY", "SECURITY_HOTSPOT"}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON object key: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


class DescriptionText(HTMLParser):
    """Expose prose, examples, and link URLs without executing source HTML."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag in {"p", "div", "pre", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6", "br"}:
            self.parts.append("\n")
        if tag == "li":
            self.parts.append("\n- ")
        if tag == "a":
            self.links.append(dict(attrs).get("href", ""))

    def handle_endtag(self, tag):
        if tag == "a" and self.links:
            url = self.links.pop()
            if url:
                self.parts.append(f" ({url})")
        if tag in {"p", "div", "pre", "li", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_data(self, data):
        self.parts.append(data)


def plain_text(content):
    parser = DescriptionText()
    parser.feed(content)
    return "".join(parser.parts).strip()


def snapshot(root):
    """Validate all exported entries while preserving every original field/array."""
    source = root / "references/sonar/exports"
    documents = {}
    seen = set()
    for name, prefix in EXPORTS.items():
        path = source / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Missing or symlinked Sonar export: {name}")
        doc = read_json(path)
        rules = doc["rules"]
        if not isinstance(rules, list) or not rules:
            raise ValueError(f"Empty or invalid rule list: {name}")
        if doc["total"] != len(rules) or doc["paging"]["total"] != len(rules):
            raise ValueError(f"Incomplete Sonar export totals: {name}")
        if doc["p"] != 1 or doc["paging"]["pageIndex"] != 1 or doc["ps"] < len(rules):
            raise ValueError(f"Incomplete Sonar export pagination: {name}")
        for rule in rules:
            key = rule["key"]
            if not isinstance(key, str) or not key.startswith(prefix + ":") or key in seen:
                raise ValueError(f"Duplicate or wrong-language rule key: {key}")
            seen.add(key)
            for field in ("name", "severity", "type"):
                if not isinstance(rule[field], str) or not rule[field].strip():
                    raise ValueError(f"Missing rule {field}: {key}")
            if rule["type"] not in TYPES or not isinstance(rule["impacts"], list):
                raise ValueError(f"Invalid rule classification: {key}")
            # Hotspot impact arrays are legitimately empty in the supplied snapshot.
            for impact in rule["impacts"]:
                if not impact.get("softwareQuality") or not impact.get("severity"):
                    raise ValueError(f"Invalid impact: {key}")
            sections = rule["descriptionSections"]
            if not isinstance(sections, list) or not sections:
                raise ValueError(f"Missing description sections: {key}")
            if not any(s.get("key") == "root_cause" for s in sections):
                raise ValueError(f"Missing root cause: {key}")
            for section in sections:
                if not section.get("key") or not isinstance(section.get("content"), str) or not section["content"].strip():
                    raise ValueError(f"Empty description section: {key}")
                if "context" in section:
                    context = section["context"]
                    if not isinstance(context, dict) or not context.get("key") or not context.get("displayName"):
                        raise ValueError(f"Invalid description context: {key}")
        documents[name] = doc
    return documents


def inventory(root, documents):
    files = []
    for name in sorted(documents):
        data = (root / "references/sonar/exports" / name).read_bytes()
        rules = documents[name]["rules"]
        sections = [s for r in rules for s in r["descriptionSections"]]
        files.append({
            "path": "exports/" + name,
            "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "rules": len(rules), "sections": len(sections),
            "context_sections": sum("context" in s for s in sections),
            "type_counts": dict(sorted(Counter(r["type"] for r in rules).items())),
            "rule_keys": sorted(r["key"] for r in rules),
        })
    return {"files": files,
            "rule_count": sum(f["rules"] for f in files),
            "section_count": sum(f["sections"] for f in files),
            "context_section_count": sum(f["context_sections"] for f in files)}


def cell(text):
    return escape(str(text), quote=False).replace("|", "\\|").replace("\n", " ")


def render_index(documents):
    lines = ["# Complete Sonar way rule index", "",
             "Use every applicable rule from this fixed, user-supplied snapshot. "
             "Read `../sonar-guidance.md` before applying rules or examples.", "",
             "Read full descriptions using `python scripts/sonar_rules.py show RULE_KEY` "
             "from the skill directory. Use `--format json` after `show` for the exact "
             "exported fields and HTML. Repeated section names retain their contexts.", "",
             "## Contents", ""]
    for name in sorted(documents):
        lines.append(f"- [{name}](#{name.replace('.', '')})")
    lines.append("")
    for name in sorted(documents):
        rules = documents[name]["rules"]
        lines += [f"## {name}", "", f"[Original export](exports/{name}) — {len(rules)} rules.", "",
                  "| Rule key | Name | Type | Severity | Context variants |",
                  "| --- | --- | --- | --- | --- |"]
        for rule in sorted(rules, key=lambda r: r["key"]):
            contexts = [s["context"]["displayName"] for s in rule["descriptionSections"] if "context" in s]
            lines.append("| " + " | ".join(cell(v) for v in (
                rule["key"], rule["name"], rule["type"], rule["severity"], ", ".join(contexts) or "—"
            )) + " |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def verify(root):
    try:
        manifest = read_json(root / "references/sonar/manifest.json")
        documents = snapshot(root)
        actual = inventory(root, documents)
        errors = []
        if manifest.get("schema_version") != 1:
            errors.append("Unsupported Sonar manifest schema")
        for key, value in actual.items():
            if manifest.get(key) != value:
                errors.append(f"Sonar manifest/source mismatch: {key}")
        source = root / "references/sonar/exports"
        present = {p.name for p in source.iterdir()}
        if present != set(EXPORTS):
            errors.append("Sonar export directory has missing or unlisted entries")
        if (root / "references/sonar/index.md").read_text(encoding="utf-8") != render_index(documents):
            errors.append("Sonar index is incomplete or stale")
        for required in ("references/sonar-guidance.md", "references/sonar/NOTICE.md", "scripts/sonar_rules.py"):
            if not (root / required).is_file():
                errors.append(f"Missing Sonar resource: {required}")
        return errors
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        return [f"Invalid Sonar snapshot: {error}"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("verify", help="Check original hashes, every entry/context, and the complete index")
    commands.add_parser("rebuild", help="Maintainer-only: regenerate manifest/index after an authorized source refresh")
    listing = commands.add_parser("list", help="List matching rule metadata; search full descriptions offline")
    listing.add_argument("--language", choices=sorted(LANGUAGES))
    listing.add_argument("--search", default="")
    listing.add_argument("--type", choices=sorted(TYPES))
    show = commands.add_parser("show", help="Read complete descriptions for one or more full rule keys")
    show.add_argument("keys", nargs="+")
    show.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()
    root = args.skill_root.resolve()
    try:
        if args.command == "verify":
            errors = verify(root)
            if errors:
                for error in errors:
                    print(f"FAIL: {error}", file=sys.stderr)
                return 1
            info = read_json(root / "references/sonar/manifest.json")
            print(f"PASS: {info['rule_count']} Sonar rules, {info['section_count']} sections, "
                  f"{info['context_section_count']} context sections; hashes and full index match")
            return 0
        documents = snapshot(root)
        if args.command == "rebuild":
            path = root / "references/sonar/manifest.json"
            previous = read_json(path) if path.exists() else {}
            result = {"schema_version": 1, "provenance": previous.get("provenance", {}), **inventory(root, documents)}
            path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            (root / "references/sonar/index.md").write_text(render_index(documents), encoding="utf-8")
            print("Updated Sonar manifest and complete rule index; review source changes and provenance before committing")
            return 0
        rules = [r for doc in documents.values() for r in doc["rules"]]
        if args.command == "list":
            for rule in sorted(rules, key=lambda r: r["key"]):
                if args.language and not rule["key"].startswith(LANGUAGES[args.language] + ":"):
                    continue
                if args.type and rule["type"] != args.type:
                    continue
                text = rule["key"] + " " + rule["name"] + " " + " ".join(
                    plain_text(s["content"]) for s in rule["descriptionSections"])
                if args.search.casefold() not in text.casefold():
                    continue
                print(f"{rule['key']} | {rule['type']} | {rule['severity']} | {rule['name']}")
            return 0
        by_key = {r["key"]: r for r in rules}
        unknown = [key for key in args.keys if key not in by_key]
        if unknown:
            raise ValueError("Unknown full Sonar rule key(s): " + ", ".join(unknown))
        selected = [by_key[key] for key in args.keys]
        if args.format == "json":
            print(json.dumps(selected, ensure_ascii=False, indent=2))
        else:
            for rule in selected:
                print(f"\n# {rule['key']}: {rule['name']}\nType: {rule['type']} | Severity: {rule['severity']}")
                print("Impacts: " + json.dumps(rule["impacts"], ensure_ascii=False))
                for section in rule["descriptionSections"]:
                    context = section.get("context")
                    suffix = f" [{context['displayName']} / {context['key']}]" if context else ""
                    print(f"\n## {section['key']}{suffix}\n\n{plain_text(section['content'])}")
        return 0
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
