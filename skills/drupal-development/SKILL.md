---
name: drupal-development
description: Develop, debug, refactor, document, and review Drupal modules, themes, and integrations using the complete user-supplied Drupal coding standards. Use for Drupal PHP, hooks, services, PSR-4 classes, exceptions, JavaScript, behaviors, jQuery, CSS, Twig templates, SQL/schema changes, YAML configuration, Composer package naming, spelling, and coding-standards audits. Apply version-aware guidance for legacy and modern Drupal projects; consult the bundled full standards rather than relying on a summary.
---

# Drupal Development

Implement the requested Drupal change using the supplied standards as the coding-style baseline. Preserve behavior and public contracts unless the requested change requires otherwise.

## 1. Establish the project context

1. Read repository instructions and inspect the working tree before editing. Identify the requested change and its allowed scope.
2. Determine Drupal core, PHP, JavaScript tooling, Twig, and database versions from project files, lockfiles, installed packages, and CI configuration. Locate the actual Drupal root; do not assume it is the repository root or `web/`.
3. Identify the owning module/theme, machine name, relevant libraries, routes, services, configuration, templates, and existing tests. Follow installed APIs and nearby supported patterns.
4. Read [compatibility and source limits](references/compatibility.md) before applying examples. Treat the bundled material as a fixed snapshot, despite its upstream “always-current” wording. Do not assume that old examples describe the installed APIs.
5. Infer missing details from repository evidence. Ask only when a material choice cannot be resolved; for a standalone snippet, state the applicable version assumptions.

## 2. Load every applicable standard

Read the [general standards](references/standards/docs/index.md), then select **all** relevant rows below. Read the full applicable files before writing or reviewing code; a checklist or search hit is not a substitute. Include secondary concerns: a PHP database service also needs SQL, namespace, exception, and documentation standards; a theme behavior may need JavaScript, jQuery, CSS, Twig, and spelling standards.

Use the [complete source map](references/source-map.md) to find every file and section, including the table of contents for long original documents. Use `rg -n` inside the skill's `references/standards/` directory to locate a specific rule, then read its surrounding section. Resolve these paths against this skill's directory, not the target project.

| Task or concern | Read these full source files |
| --- | --- |
| PHP formatting, arrays, control structures, operators, naming, constructors, chaining, types, interfaces, visibility, strict declarations, includes, and legacy autoloading | [PHP introduction](references/standards/docs/php/index.md), [PHP coding](references/standards/docs/php/coding.md) |
| PHP comments, file/class/member documentation, hooks and updates, callbacks, forms, preprocess functions, templates, lists, events, deprecations, annotations, and all documentation tags | [API documentation](references/standards/docs/php/documentation.md), [documentation examples](references/standards/docs/php/documentation-examples.md) |
| Class imports, aliases, namespaces, source/test placement, and module/theme autoloading | [Namespaces](references/standards/docs/php/namespaces.md), [PSR-4](references/standards/docs/php/psr4.md) |
| Request attributes and reserved framework attribute names | [Services and Symfony naming](references/standards/docs/php/naming-services.md) |
| Exception naming, messages, subclasses, inheritance, and catch formatting | [Exceptions](references/standards/docs/php/exceptions.md) |
| Content-processing placeholders and delimiter matching | [Placeholders and delimiters](references/standards/docs/php/placeholders-delimiters.md) |
| Undefined values, zero/empty/null semantics, and error-reporting examples | [E_ALL compliance](references/standards/docs/php/e_all.md) |
| JavaScript syntax, file closures, names, variables, constants, arrays, functions, constructors, comments, control structures, and operators | [JavaScript coding](references/standards/docs/javascript/coding.md) |
| JavaScript placement, literals, prohibited constructs, user output, DOM updates, theming, and translation | [JavaScript best practices](references/standards/docs/javascript/best-practice.md) |
| JSDoc tags/order, file headers, behavior attach/detach documentation, constructors, namespaces, properties, and custom events | [JavaScript documentation](references/standards/docs/javascript/documentation.md), [shared PHP documentation conventions](references/standards/docs/php/documentation.md) |
| ESLint configuration and custom/contributed JavaScript checks | [ESLint](references/standards/docs/javascript/eslint.md) |
| Existing jQuery code, object-variable prefixes, chaining, delegated events, selector context, properties, and iteration | [jQuery](references/standards/docs/javascript/jquery.md) |
| Any CSS work | [CSS introduction](references/standards/docs/css/coding.md), [formatting](references/standards/docs/css/format.md), [architecture](references/standards/docs/css/architecture.md), [file organization](references/standards/docs/css/file-organization.md), [review](references/standards/docs/css/review.md) |
| CSS property sorting, CSScomb/CSScombx configuration, or existing formatter integrations | [Complete CSScomb settings and tooling](references/standards/docs/css/csscomb.md) |
| Twig expressions, variables, attributes, comments, filters, whitespace, and base/override template documentation | [Twig](references/standards/docs/twig/coding.md), [theme-template documentation](references/standards/docs/php/documentation.md) |
| SQL queries, identifiers, schema/constraint/index naming, database portability, and selected fields | [SQL conventions](references/standards/docs/sql/conventions.md), [all 826 reserved-word entries](references/standards/docs/sql/keywords.md), [SELECT field guidance and exceptions](references/standards/docs/sql/select-from.md) |
| YAML configuration syntax, ownership, simple/entity/bundle naming, length limits, comments, and indentation | [YAML configuration files](references/standards/docs/yaml/configuration-files.md) |
| Composer project/subproject/component names and replacement declarations | [Composer package names](references/standards/docs/composer/package-name.md) |
| Names, comments, and CSpell handling | [Spelling](references/standards/docs/spelling/spelling.md), [supplied project dictionary](references/standards/.cspell-project-words.txt) |
| Markup or accessibility changes | [Markup source](references/standards/docs/markup/style.md), [accessibility source](references/standards/docs/accessibility/accessibility.md); account for their limited contents using the compatibility guidance |
| Auditing the standards site's own build, navigation, or CI | [Source README](references/standards/README.md), [MkDocs configuration](references/standards/mkdocs.yml), [GitLab CI](references/standards/.gitlab-ci.yml), [source ignore file](references/standards/.gitignore) |

Preserve the distinction between MUST, SHOULD, recommendations, exceptions, and historical examples. Do not turn a recommendation into an unconditional requirement or invent a rule where the source leaves a choice open.

## 3. Implement or review the change

1. Turn the applicable source sections into a short task-specific checklist. Use [review and validation](references/review-and-validation.md) to check coverage across file types and Drupal integration points.
2. Implement with APIs supported by the inspected project. Check service definitions, signatures, autoload paths, configuration names, asset attachments, and template/preprocess contracts together with the code that uses them.
3. Keep code, comments, and names in US English. Apply the source's language-specific conventions: PHP `elseif` differs from JavaScript `else if`; PHP code constants differ from lowercase PHPDoc type names; CSS and JavaScript hooks have different purposes.
4. Follow the full API-documentation rules, including special hook/update/callback documentation, tag order, fully qualified documentation types, and inherited documentation. Do not copy incomplete sample docblocks.
5. For a standards-only cleanup, organize changes by rule across the agreed scope, as the general standard requires. For a functional task, keep related style fixes scoped to touched code; do not expand into an unrelated repository-wide cleanup.
6. For a review-only request, report findings with file locations, the applicable source rule, impact, and a concrete correction. Separate confirmed violations from optional recommendations and unresolved version questions. Do not modify files unless authorized.
7. Treat additional engineering checks as implementation checks, not as rules claimed to appear in the archive. Do not claim the archive supplies comprehensive security, accessibility, deployment, or feature-development manuals.

## 4. Verify and report

1. Re-read the finished diff against the applicable full standards. Check every touched file type, including documentation, supporting YAML, and integration boundaries. Resolve conflicts through the compatibility workflow; disclose material deviations.
2. Run the project's existing relevant checks using its pinned dependencies and configuration. Discover commands from repository scripts and CI. Use the command patterns in [review and validation](references/review-and-validation.md) only after confirming their prerequisites.
3. Exercise changed behavior with appropriate tests or a targeted manual check. Include relevant failure/empty cases. Distinguish standards checks, syntax checks, behavior tests, and checks that could not run.
4. Inspect the final working tree for unintended edits or generated artifacts. Report what changed, what passed, and any specific remaining limitation. Never report a check as passing merely because a tool is absent or a command ran against zero files.

## Maintain source completeness

Keep all original files under `references/standards/` byte-for-byte unchanged, including images, dictionary, site configuration, and incomplete or obsolete sections. Use the generated source map for navigation rather than rewriting the originals. Do not execute the source CI, copy its debug settings, or install its historical tool examples into a target project automatically.

Use [the source manifest](references/source-manifest.json) and [the bundle verifier](scripts/verify_bundle.py) when auditing or updating this skill:

```bash
python /absolute/path/to/drupal-development/scripts/verify_bundle.py
python /absolute/path/to/drupal-development/scripts/verify_bundle.py --archive /absolute/path/to/coding_standards-main.zip
```

The first command checks bundled file hashes, sizes, document headings, navigation, and direct source links. The second also compares every original archive file and its archive hash. These checks verify reference completeness; use the target project's checks to verify Drupal code.
