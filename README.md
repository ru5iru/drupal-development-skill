# Drupal Development Skill

A reusable AI coding skill for developing and reviewing Drupal modules, themes,
and integrations against a complete, preserved snapshot of Drupal coding
standards.

Repository: [ru5iru/drupal-development-skill](https://github.com/ru5iru/drupal-development-skill).

The skill covers PHP, API documentation, namespaces, PSR-4, exceptions,
JavaScript, JSDoc, jQuery, CSS, Twig, SQL, YAML, Composer naming, and spelling.
It tells the agent to inspect the project's installed versions, read every
applicable standard, make scoped changes, and verify the result.

## Contents

- [Drupal Development Skill](#drupal-development-skill)
  - [Contents](#contents)
  - [What is included](#what-is-included)
  - [Installation](#installation)
    - [Codex: personal installation on Linux, macOS, or WSL](#codex-personal-installation-on-linux-macos-or-wsl)
    - [Codex: personal installation on Windows PowerShell](#codex-personal-installation-on-windows-powershell)
    - [Codex: installation for one project](#codex-installation-for-one-project)
    - [Confirm the installation](#confirm-the-installation)
    - [Updates and removal](#updates-and-removal)
  - [Usage](#usage)
  - [Validation and CI](#validation-and-ci)
  - [License and attribution](#license-and-attribution)

## What is included

| Path | Purpose |
| --- | --- |
| [skills/drupal-development/SKILL.md](skills/drupal-development/SKILL.md) | Skill instructions and direct routes to every applicable standard |
| [skills/drupal-development/agents/openai.yaml](skills/drupal-development/agents/openai.yaml) | Display metadata, icon paths, and invocation policy |
| [assets/icon.svg](skills/drupal-development/assets/) | Original skill icon |
| [references/standards/](skills/drupal-development/references/standards/) | All 40 original standards files, unchanged |
| [references/source-map.md](skills/drupal-development/references/source-map.md) | Navigation for 32 Markdown documents and 297 literal headings |
| [references/source-manifest.json](skills/drupal-development/references/source-manifest.json) | File sizes, hashes, headings, archive hash, and source revision |
| [references/compatibility.md](skills/drupal-development/references/compatibility.md) | Legacy examples, version compatibility, and incomplete source sections |
| [references/review-and-validation.md](skills/drupal-development/references/review-and-validation.md) | Review coverage and project-specific verification guidance |
| [scripts/verify_bundle.py](skills/drupal-development/scripts/verify_bundle.py) | Dependency-free standards integrity verifier |
| [Upstream Drupal Coding Standards](https://git.drupalcode.org/project/coding_standards) | Source repository for reference and future standards updates |
| [scripts/check_repository.py](scripts/check_repository.py) | Repository, metadata, local-link, and CI configuration validation |
| [tests/](tests/) | Failure-detection tests for the bundle verifier and repository validator |
| [.github/workflows/ci.yml](.github/workflows/ci.yml) | Checks on pushes, pull requests, and manual runs |

This is a skill repository, not a Drupal module. It needs no Drupal, PHP, Node.js,
Composer, API key, or database to install. Python 3.10+ is needed only for the
bundled integrity verifier. Repository development checks also use PyYAML.

The original `coding_standards-main.zip` is not included. Refer to the
[upstream repository](https://git.drupalcode.org/project/coding_standards)
for the source; the complete extracted standards remain bundled with the skill.

## Installation

Download and extract this repository, or clone it:

```bash
git clone https://github.com/ru5iru/drupal-development-skill.git
cd drupal-development-skill
```

### Codex: personal installation on Linux, macOS, or WSL

Run from this repository's root. The existence check prevents overwriting an
existing installation:

```bash
skill_destination="$HOME/.agents/skills/drupal-development"
if [ -e "$skill_destination" ] || [ -L "$skill_destination" ]; then
  echo "An installation already exists at $skill_destination; review it before updating."
else
  mkdir -p "$(dirname "$skill_destination")"
  cp -R skills/drupal-development "$skill_destination"
fi
```

### Codex: personal installation on Windows PowerShell

Run from this repository's root:

```powershell
$skillDestination = Join-Path $HOME '.agents/skills/drupal-development'
if (Test-Path -LiteralPath $skillDestination) {
    throw "An installation already exists at $skillDestination; review it before updating."
}
New-Item -ItemType Directory -Force (Split-Path $skillDestination) | Out-Null
Copy-Item -LiteralPath 'skills/drupal-development' -Destination $skillDestination -Recurse
```

### Codex: installation for one project

Copy the complete `skills/drupal-development` directory into your Drupal
repository at `.agents/skills/drupal-development/`. Keep the bundled references,
scripts, metadata, and license notices together. Commit that directory if your
team should share the skill. Review an existing copy before replacing it.

Codex discovers local skills in `.agents/skills` for a repository and in
`$HOME/.agents/skills` for a user. If the skill does not appear, restart Codex.
See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills).
For another agent that supports `SKILL.md`, use that agent's documented skill
directory; its installation interface and optional metadata support may differ.

### Confirm the installation

From the installed skill directory:

```bash
python3 scripts/verify_bundle.py
```

The output should report 40 original files, 32 Markdown documents, 297 headings,
and 961,231 source bytes. On Windows, use `py -3` in place of `python3` if needed.

### Updates and removal

To update a cloned source repository, run `git pull --ff-only`, then validate it
again. Compare local skill customizations before replacing an installation with
the complete updated `skills/drupal-development` directory. Replace the directory
as a unit so files removed by a later release do not remain behind. To uninstall,
remove only the installed `drupal-development` directory from the skill location
you selected.

## Usage

Open a Drupal project in your coding agent and invoke `$drupal-development` with
a concrete task. Include the module/theme path and any scope constraints.

**Implement a feature**

```text
Use $drupal-development to add the requested configuration form in
web/modules/custom/example. Inspect the installed Drupal and PHP versions,
follow the bundled standards, and run the relevant existing project checks.
```

**Review without editing**

```text
Use $drupal-development to review web/modules/custom/example for coding-standard
violations. Do not edit files. Include file locations, the relevant bundled
source rule, and a suggested correction for each confirmed finding.
```

**Review a theme change**

```text
Use $drupal-development to review this theme's Twig templates, JavaScript
behaviors, and CSS together. Check documentation and integration boundaries,
and distinguish required corrections from recommendations.
```

**Perform a scoped cleanup**

```text
Use $drupal-development to fix PHPDoc issues only in this module. Preserve
behavior, group the cleanup by rule, and report checks that could not run.
```

The agent should establish the version context, read the full applicable
references, implement or report findings within scope, and summarize checks and
remaining limitations. The skill's verifier checks the reference bundle;
Drupal code still needs its own project's linting and behavior tests.

## Validation and CI

Run the standalone source check without installing packages:

```bash
python3 skills/drupal-development/scripts/verify_bundle.py
```

Run the complete repository checks in a virtual environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/check_repository.py
python -m unittest discover -s tests -v
```

For PowerShell, activate with `.venv\Scripts\Activate.ps1`. If PowerShell
activation is unavailable, run `.venv\Scripts\python.exe` directly.

GitHub Actions runs the same checks on Python 3.10 and 3.13, plus Python syntax
compilation. Checks cover bundled source hashes and sizes, section indexing,
navigation, metadata, authored local links, and intentional failure cases.
The workflow has read-only repository permissions, needs no secrets, and pins
its checkout/setup actions to full commit hashes. Dependabot proposes updates
to those actions and the development dependency.

Historical Markdown defects inside `references/standards/` are preserved, so CI
does not reformat or lint that upstream snapshot as newly authored Markdown.
The nested upstream GitLab CI and MkDocs configuration are reference material;
GitHub Actions runs only the workflow in this repository's `.github/workflows/`.

## License and attribution

Original skill instructions, tooling, and repository files are provided under
the [MIT License](LICENSE). Bundled Drupal material retains its upstream terms;
it is excluded from that MIT grant. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)
for source attribution, the documentation license, the GPL terms for upstream
Git-hosted files/sample code, and trademark information. Keep these notices when
redistributing the installable skill.
