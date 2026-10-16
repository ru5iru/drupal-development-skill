# Contributing

Keep the skill usable as a complete directory at `skills/drupal-development/`.
Keep human installation and repository maintenance instructions in the root
README; keep task instructions in `SKILL.md` and its references.

## Development checks

Use Python 3.10+ and a virtual environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/check_repository.py
python -m unittest discover -s tests -v
```

The standalone source verifier needs only Python's standard library:

```bash
python3 skills/drupal-development/scripts/verify_bundle.py
```

## Change the skill or tooling

- Keep `name: drupal-development` aligned with the installable directory.
- Keep `agents/openai.yaml` aligned with the skill's scope and icon paths.
- Test script changes with meaningful success and failure cases.
- Check authored local links and installation instructions after moving files.
- Use a fresh task to review substantial behavioral changes to the skill. The
  deterministic CI checks cannot establish the quality of an agent's reasoning.
- Describe the problem, resulting behavior, and validation in each pull request.

## Refresh the standards snapshot

1. Obtain a complete snapshot from the
   [upstream Drupal Coding Standards repository](https://git.drupalcode.org/project/coding_standards)
   in a temporary directory outside this repository. Record its source URL,
   revision, archive root, and checksum. Do not commit the downloaded archive.
2. Extract every original file to `references/standards/` under the skill. Retain
   source bytes, images, dotfiles, and incomplete pages. Never patch the original
   text to satisfy lint tools or remove sections because they appear obsolete.
3. Update all manifest fields, file records, hashes, sizes, and literal heading
   records to describe that exact snapshot. Keep manifest paths sorted. Retain
   archive metadata as provenance without including the archive in the repository.
4. Regenerate `references/source-map.md` using `render_source_map()` in the
   bundled verifier. Route every original non-image source directly from
   `SKILL.md`; inspect the new navigation and document additions/removals.
5. Review the full changed standards and update compatibility notes, routing,
   attribution, README counts, and test expectations where needed. Do not merely
   edit checksums to make validation pass.
6. Run all repository checks and exercise representative Drupal tasks. If the
   downloaded snapshot is an archive compatible with the verifier, also run
   `verify_bundle.py --archive /absolute/path/to/the/local/archive.zip` before
   discarding it. Include the source revision and results in the pull request.

## Licensing

Submit original contributions under the MIT license. Preserve upstream copyright
and license notices, and identify adaptations of upstream material under their
applicable terms. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
