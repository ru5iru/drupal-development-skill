# Review and validation

## Contents

- [Plan coverage](#plan-coverage)
- [Check integration boundaries](#check-integration-boundaries)
- [Choose project checks](#choose-project-checks)
- [Use conditional command patterns](#use-conditional-command-patterns)
- [Report evidence](#report-evidence)

## Plan coverage

Start from the changed behavior and every affected file type. Read full relevant standards from the routing table in `SKILL.md`. Use `source-map.md` for section-level navigation. Expand the checklist when the diff adds a new concern.

Give the required scope/guidance/clarification summary before development, review, refactoring, or analysis. Include `Clarifications needed: none` when context is sufficient. Read [Sonar application guidance](sonar-guidance.md), inspect the [complete rule index](sonar/index.md) for every relevant language, and retrieve each applicable full description. Include Sonar exceptions, configured parameters when known, and Drupal-specific fallbacks in the task checklist. Do not substitute generic defaults for an explicit Drupal branch.

| Change | Include in the review |
| --- | --- |
| PHP function, class, interface, trait, or enum | Formatting, arrays/operators, control structures, names, visibility/modifier order, type hints and compatibility, interface contracts, documentation, imports, PSR-4 placement, and empty/undefined-value semantics. Include enum-case and class-suffix rules where applicable. |
| Hook, update, callback, form, preprocess, or template function | The exact documentation convention for that function category; standard versus additional parameters; summary wording; callbacks and associated handler references; themeable groups; applicable source examples and their known limitations. |
| PHPDoc/API change | Summary and wrapping; all applicable tags and their order; namespaced types; `@param`/`@return` descriptions and documented exceptions; `{@inheritdoc}`; typed-property rules; lists; groups; code/link/section tags; events/deprecations/plugin annotations when used. |
| Service or content-processing change | Actual service registration and constructor contracts, Request attribute prefix/reserved names, exception semantics, safe placeholders/delimiters, and relevant SQL/translation/output concerns. |
| JavaScript | Closure/scope, declaration and naming rules, semicolons/returns, strict comparisons, object/array formatting, functions/control structures, own-property filtering, comments/JSDoc and tag order, translation, event documentation, output handling, and effective ESLint configuration. |
| Existing jQuery | `$` variable/property names, selector context/caching, chaining, delegated events, explicit prevention/propagation, version-supported property APIs, and native collection iteration guidance. |
| CSS | Full formatting and declaration guidance, comments, selectors, component/sub-element/modifier names, both base and modifier classes, separation of layout/style/state/behavior, absence of styled `js-` hooks, specificity and `!important`, correct files, reusable patterns, stale/redundant rules, RTL, and formatter exclusions when relevant. |
| Twig/markup | File documentation, variables and preprocess links, default versus override `@ingroup`, expressions/loops/filters, comments, attributes, escaping, whitespace, source limits, and project-specific semantic/accessibility requirements. |
| SQL/schema | Parameter binding, identifier/table conventions for the installed abstraction, explicit columns and exceptions, singular/prefixed table naming, named constraints/indexes, Schema API, reserved words, portability, and access behavior. |
| YAML configuration | Correct owning extension; simple versus entity versus bundle names; `.yml` filename; total and component length limits; two-space semantic indentation; comments; inspect other YAML file types through their own installed schema. |
| Composer packaging | Two-part vendor/project format, drupal.org project ownership, subproject precedence, parent-component names, and valid `replace` metadata. |
| All changes | US English, relevant CSpell exceptions, line endings/whitespace where specified, no unrelated edits, and alignment between comments and current behavior. |

## Check integration boundaries

Treat these as implementation checks to complement the supplied style standard, not as additional rules claimed to exist in it:

- Match class paths, namespaces, imported interfaces, and discovered test locations.
- Match service IDs/arguments to consuming constructors and callable signatures. Respect inherited APIs when adding types.
- Match routes, form callbacks, permissions, library attachments/dependencies, and existing application registration patterns when those files change.
- Match configuration object names and schemas to actual readers/writers and installed entity metadata.
- Match preprocess variables to template documentation and attribute rendering. Retain user-content escaping and relevant access/cache behavior.
- For behavior changes, exercise initial attachment and repeated/AJAX attachment where the existing project uses them; check detach/cleanup when changed.
- For UI changes, inspect the affected component in relevant states, viewport sizes, keyboard interaction, and LTR/RTL contexts as applicable.
- Preserve data and public API compatibility during a style-only change.

## Choose project checks

Read Composer/package scripts, CI jobs, installed binaries, lint configuration, ignore patterns, and existing test instructions. Prefer the repository's own commands. Run checks against changed custom code and relevant integration points; include dependencies only when the change requires it.

Use PHP_CodeSniffer with the project's installed Drupal/Coder/Slevomat configuration, ESLint with the effective project configuration, and the existing CSS/Twig/YAML/spelling tools where available. Do not assume that all these tools are installed, that one tool covers every file type, or that the archive's example install commands match the project.

Do not automatically download executables, add dependencies, rewrite configuration, or make global installations merely because a validation tool is absent. Use available checks and report the specific missing check. Install a project dependency only when it is necessary and within the task's scope.

## Use conditional command patterns

Substitute actual paths and verify the tools/options before running. These are patterns, not commands to execute blindly:

```bash
# Inspect registered project checks and installed coding standards.
composer run-script --list
./vendor/bin/phpcs -i

# Use the repository ruleset and explicit supported paths, if configured.
./vendor/bin/phpcs --standard=phpcs.xml.dist path/to/custom_module

# With no repository ruleset, use this only if Drupal is listed by phpcs -i.
./vendor/bin/phpcs --standard=Drupal path/to/changed_file.php

# Syntax-check each changed PHP file, including .module/.install/.inc as needed.
php -l path/to/changed_file.php

# Use the locally installed ESLint and its project configuration.
./node_modules/.bin/eslint path/to/changed_file.js

# Run the matching existing PHPUnit test/configuration if present.
./vendor/bin/phpunit -c actual/phpunit.xml.dist actual/tests/path

# Inspect the completed patch and whitespace errors.
git diff --check
git diff --stat
git status --short
```

Inspect the actual repository ruleset filename; it may be `phpcs.xml`, `.phpcs.xml`, `phpcs.xml.dist`, or a script-selected configuration elsewhere. Use the project's exact test configuration, bootstrap, and environment. A syntax pass alone does not validate autoloading, dependency injection, Drupal runtime behavior, or template rendering.

Use an existing formatter's check/lint mode first. Avoid auto-fixing broad directories, vendor/core files, or generated assets outside the request. If a formatter is used to change files, inspect its entire diff and rerun affected checks.

## Report evidence

Perform two complementary reviews of the finished change:

1. Review standards and integration coverage against the relevant source files and final diff.
2. Verify the changed behavior using targeted tests or manual execution, plus available lint/syntax/build checks.

Review both Drupal and applicable Sonar practices in each pass. Preserve framework contracts during refactors, separate security-hotspot assessments from confirmed defects, and report unknown thresholds or version-dependent choices. The reference checks (`verify_bundle.py`, `sonar_rules.py verify`, and `test_sonar_rules.py`) verify source integrity and retrieval; only actual configured analyzer output can establish Sonar findings or quality-gate status.

Record exact commands, outcomes, and useful scope internally; summarize routine verification for the user. Separate a missing dependency, a skipped check, a pre-existing failure, and a new regression. Do not equate an ignored file or empty check set with success.

For a code review, give each confirmed finding a file location, an explanation, and the source path/section that supports it. Mark recommendations and source ambiguities separately. For implementation, report changes, relevant checks, and unresolved limitations without claiming full standards compliance that was not verified.

Include full Sonar keys for relevant findings and explain any applicable Drupal fallback or exception. Acknowledge the absence of actual Sonar analysis when it could not run. Do not interpret a missing scanner finding, an empty hotspot impact array, or a passing reference verifier as proof of safety.
