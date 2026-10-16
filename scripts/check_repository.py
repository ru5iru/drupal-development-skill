#!/usr/bin/env python3
"""Validate the distributable skill, repository metadata, and source integrity."""

import argparse
import importlib.util
import re
import sys
from pathlib import Path
from zipfile import BadZipFile

try:
    import yaml
except ImportError:
    sys.exit("FAIL: install development dependencies: python -m pip install -r requirements-dev.txt")


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys rather than silently discarding configuration."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def bundle_module(skill):
    spec = importlib.util.spec_from_file_location(
        "verify_bundle", skill / "scripts/verify_bundle.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_repository(root):
    """Return errors; let the source verifier emit its own detailed diagnostics."""
    root = Path(root).resolve()
    skill = root / "skills/drupal-development"
    required = [
        "README.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "CONTRIBUTING.md",
        ".gitignore", ".gitattributes", ".editorconfig", "requirements-dev.txt",
        ".github/workflows/ci.yml", ".github/dependabot.yml",
        "scripts/check_repository.py",
        "tests/test_validation.py", "skills/drupal-development/SKILL.md",
        "skills/drupal-development/agents/openai.yaml",
        "skills/drupal-development/LICENSE",
        "skills/drupal-development/THIRD_PARTY_NOTICES.md",
        "skills/drupal-development/LICENSES/GPL-2.0-or-later.txt",
        "skills/drupal-development/scripts/verify_bundle.py",
    ]
    errors = [f"Missing required file: {name}" for name in required
              if not (root / name).is_file()]
    if errors:
        return errors

    verifier = bundle_module(skill)
    if list(root.rglob("coding_standards-main.zip")):
        errors.append("Do not include coding_standards-main.zip; refer to the upstream repository")
    if verifier.verify(skill):
        errors.append("Standards bundle validation failed")

    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not front:
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        metadata = yaml.load(front.group(1), Loader=UniqueLoader)
        if not isinstance(metadata, dict) or set(metadata) != {"name", "description"}:
            errors.append("Skill frontmatter must contain only name and description")
        else:
            if metadata["name"] != skill.name:
                errors.append("Skill name must match directory: drupal-development")
            description = metadata["description"]
            if (not isinstance(description, str) or not description.strip()
                    or len(description) > 1024 or "<" in description or ">" in description):
                errors.append("Skill description must be nonempty plain text, at most 1024 characters")
    if len(text.splitlines()) >= 500:
        errors.append("Keep SKILL.md under 500 lines; move details to references")

    agent = yaml.load((skill / "agents/openai.yaml").read_text(encoding="utf-8"),
                      Loader=UniqueLoader)
    interface = agent.get("interface", {})
    for key in ("display_name", "short_description", "default_prompt"):
        if not isinstance(interface.get(key), str) or not interface[key].strip():
            errors.append(f"Missing agent interface value: {key}")
    if not 25 <= len(interface.get("short_description", "")) <= 64:
        errors.append("Agent short description must contain 25 to 64 characters")
    if "$drupal-development" not in interface.get("default_prompt", ""):
        errors.append("Agent default prompt must invoke $drupal-development")
    for key in ("icon_small", "icon_large"):
        value = interface.get(key)
        if not isinstance(value, str) or not value:
            errors.append(f"Missing agent icon: {key}")
            continue
        icon = (skill / value).resolve()
        if not icon.is_relative_to(skill) or not icon.is_file():
            errors.append(f"Missing or escaping agent icon: {key}")

    # BaseLoader keeps GitHub's YAML 1.2 'on' key a string (SafeLoader uses 1.1).
    workflow_path = root / ".github/workflows/ci.yml"
    workflow = yaml.load(workflow_path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    if not {"push", "pull_request", "workflow_dispatch"}.issubset(workflow.get("on", {})):
        errors.append("CI must run on push, pull_request, and workflow_dispatch")
    if "pull_request_target" in workflow.get("on", {}):
        errors.append("Use pull_request for checks of contributed code")
    if workflow.get("permissions") != {"contents": "read"}:
        errors.append("CI must use read-only contents permission")
    job = workflow.get("jobs", {}).get("validate", {})
    versions = job.get("strategy", {}).get("matrix", {}).get("python-version", [])
    if not {"3.10", "3.13"}.issubset(versions):
        errors.append("CI must cover Python 3.10 and 3.13")
    steps = job.get("steps", [])
    commands = "\n".join(step.get("run", "") for step in steps)
    for command in ("-r requirements-dev.txt", "scripts/check_repository.py",
                    "unittest discover -s tests", "compileall"):
        if command not in commands:
            errors.append(f"CI is missing validation command: {command}")
    actions = [step["uses"] for step in steps if "uses" in step]
    if not {"actions/checkout", "actions/setup-python"}.issubset(
            action.split("@", 1)[0] for action in actions):
        errors.append("CI must check out source and set up Python")
    for action in actions:
        if not re.fullmatch(r"[\w.-]+/[\w./-]+@[0-9a-f]{40}", action):
            errors.append(f"Pin each CI action to a full commit hash: {action}")
    # Parse these files too, catching invalid or duplicate keys without changing originals.
    yaml.load((root / ".github/dependabot.yml").read_text(encoding="utf-8"), Loader=UniqueLoader)

    authored = [root / "README.md", root / "CONTRIBUTING.md",
                root / "THIRD_PARTY_NOTICES.md", skill / "THIRD_PARTY_NOTICES.md"]
    for path in authored:
        for target in verifier.local_links(path.read_text(encoding="utf-8")):
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f"Broken or escaping local link in {path.relative_to(root)}: {target}")
    if (root / "LICENSE").read_bytes() != (skill / "LICENSE").read_bytes():
        errors.append("Installed skill must carry the same MIT license as the repository")
    if not (root / "LICENSE").read_text(encoding="utf-8").startswith("MIT License\n"):
        errors.append("Root LICENSE must contain the MIT license")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors = check_repository(args.repo_root)
    except (OSError, ValueError, KeyError, TypeError, AttributeError, BadZipFile,
            yaml.YAMLError) as error:
        errors = [str(error)]
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    if errors:
        return 1
    print("PASS: skill metadata, icons, repository documentation, licenses, and CI configuration")
    return 0


if __name__ == "__main__":
    sys.exit(main())
