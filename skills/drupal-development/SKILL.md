---
name: drupal-development
description: Develop, debug, refactor, analyze, document, and review Drupal modules, themes, and integrations against the complete supplied Drupal standards and 566 exported Sonar way PHP, HTML, CSS, and JavaScript rules. Use for Drupal PHP, hooks, services, PSR-4, exceptions, JavaScript behaviors, jQuery, HTML/Twig, CSS, SQL, YAML, Composer naming, spelling, security assessments, and standards/code-quality audits. Begin with a pre-work scope and clarification summary. Apply explicit Sonar Drupal-framework fallbacks, project-supported APIs, complete rule descriptions, and version-aware guidance.
---

# Drupal Development

Develop, review, refactor, or analyze the requested scope against both the supplied Drupal practices and all applicable exported Sonar way rules. Preserve behavior and public contracts unless the requested change requires otherwise. Treat readability and simplicity as acceptance criteria alongside correctness and standards compliance.

## 0. State scope and clarification needs before work

Before development, code review, refactoring, or substantive analysis, give the user a short list covering the requested scope, applicable Drupal/Sonar guidance, and any clarification needed. Use available project evidence to refine this summary during read-only discovery. Read [Sonar application guidance](references/sonar-guidance.md), especially its pre-work checklist, before selecting rules.

Explicitly state `Clarifications needed: none` when the available context is sufficient. Otherwise list the specific unresolved questions and explain which decisions depend on them. Ask and wait before making dependent changes when an answer is essential; continue independent read-only discovery where useful. Do not repeat answered questions or invent blocking questions for routine choices. State reasonable nonblocking assumptions and unknown analyzer settings rather than claiming certainty.

## 1. Establish the project context

1. Read repository instructions and inspect the working tree before editing. Identify the requested change and its allowed scope.
2. Determine Drupal core, PHP, JavaScript tooling, Twig, and database versions from project files, lockfiles, installed packages, and CI configuration. Locate the actual Drupal root; do not assume it is the repository root or `web/`.
3. Identify the owning module/theme, machine name, relevant libraries, routes, services, configuration, templates, and existing tests. Follow installed APIs and nearby supported patterns.
4. Read [compatibility and source limits](references/compatibility.md) before applying examples. Treat the bundled material as a fixed snapshot, despite its upstream “always-current” wording. Do not assume that old examples describe the installed APIs.
5. Infer missing details from repository evidence. Ask only when a material choice cannot be resolved; for a standalone snippet, state the applicable version assumptions.
6. Inspect available Sonar project configuration, analyzer/server versions, active rule parameters, file suffixes, exclusions, and existing reports. The attached exports do not supply these settings. Do not invent numeric thresholds or claim scanner parity without them. Confirm coverage of Drupal file types such as `.module`, `.install`, `.theme`, `.inc`, and `.twig` when relevant.

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
| All PHP, HTML/Twig, CSS, or JavaScript development, review, refactoring, or analysis | [Sonar application guidance](references/sonar-guidance.md), [complete 566-rule index](references/sonar/index.md), then the full applicable rule entries through [offline lookup](scripts/sonar_rules.py) |
| Exact Sonar PHP / HTML / CSS / JavaScript source or metadata | Original JSON exports: [PHP](references/sonar/exports/php.json), [HTML](references/sonar/exports/html.json), [CSS](references/sonar/exports/css.json), [JavaScript](references/sonar/exports/js.json); preserve all description sections, contexts, exceptions, examples, and impacts |

Preserve the distinction between MUST, SHOULD, recommendations, exceptions, and historical examples. Do not turn a recommendation into an unconditional requirement or invent a rule where the source leaves a choice open.

Inspect the complete index for every relevant language and concern, including security, testing, regex, and integration code. Read full matching rule descriptions before applying or reporting them; a title, search hit, or generic checklist is insufficient. Keep the full key (`php:`, `Web:`, `css:`, or `javascript:`) when citing a rule. Retrieve entries offline, resolving the script path against this skill:

```bash
python /absolute/path/to/drupal-development/scripts/sonar_rules.py list --language php --search Drupal
python /absolute/path/to/drupal-development/scripts/sonar_rules.py show php:S100 php:S1781
python /absolute/path/to/drupal-development/scripts/sonar_rules.py show php:S5808 --format json
```

When a Sonar rule explicitly defines a Drupal-framework fallback, follow that Drupal-specific behavior for Drupal code. In this snapshot `php:S1781` uses uppercase `TRUE`, `FALSE`, and `NULL` in Drupal, and `php:S100` describes Drupal function naming when its default regex is unchanged. Confirm framework context and any configured parameter override; do not apply the generic default or silently disable a rule. Resolve any remaining material conflict using the guidance and report it with both sources.

## Keep the implementation easy to understand

Apply these design constraints during development, refactoring, and review; use them alongside Drupal and Sonar requirements:

- Choose the smallest coherent change that solves the current problem. Inspect nearby code and reuse existing services, utilities, and components before creating another implementation.
- Prefer explicit control flow, descriptive domain names, and one clear responsibility per function. Optimize for a maintainer understanding the code in one read, not for the fewest lines. Avoid dense expressions, clever chaining, excessive indirection, and deeply nested branches.
- Introduce a helper, class, interface, service, or configuration option only for a concrete current responsibility, meaningful reuse, an existing framework contract, or a necessary test boundary. Do not add factories, repositories, adapters, generic pipelines, or speculative extension points merely to anticipate future needs. Follow required Drupal dependency injection and plugin/service contracts without wrapping them in extra layers.
- Keep straightforward one-use logic inline when extraction would merely rename an expression or force the reader to jump between files. Extract when it makes a cohesive operation easier to understand; do not fragment a function solely to reduce its length or a metric.
- Keep validation at relevant trust boundaries and handle real failure cases. Avoid repeated checks for invariants the framework already guarantees, redundant fallback chains, swallowed exceptions, and invented defaults that conceal invalid state. Preserve security, access checks, escaping, cache metadata, and required contracts.
- Use comments and required Drupal documentation to explain intent, contracts, or a non-obvious constraint. Do not narrate obvious statements or add prose to compensate for confusing code; simplify the code first.
- Apply each mandatory standard and applicable Sonar rule using its full exceptions and Drupal fallback. Among compliant solutions, choose the clearest. Do not satisfy a metric with arbitrary helpers, hide findings through suppression, or weaken correctness/security to simplify code. Report a material unresolved conflict with evidence.
- Before finishing, remove unnecessary new abstractions, duplicate branches, unused options, and avoidable file changes. Be able to explain the purpose of each new layer in one sentence tied to the current requirement. For review-only work, report complexity as a maintainability recommendation unless there is evidence of a defect or a specific violated rule; do not rewrite automatically.

## 3. Implement or review the change

1. Turn the applicable Drupal source sections and Sonar rule entries into a short task-specific checklist. Use [review and validation](references/review-and-validation.md) to check coverage across file types and Drupal integration points. Include secondary concerns across all affected languages.
2. Implement with APIs supported by the inspected project. Check service definitions, signatures, autoload paths, configuration names, asset attachments, and template/preprocess contracts together with the code that uses them.
3. Keep code, comments, and names in US English. Apply the source's language-specific conventions: PHP `elseif` differs from JavaScript `else if`; PHP code constants differ from lowercase PHPDoc type names; CSS and JavaScript hooks have different purposes.
4. Follow the full API-documentation rules, including special hook/update/callback documentation, tag order, fully qualified documentation types, and inherited documentation. Do not copy incomplete sample docblocks.
5. For a standards-only cleanup, organize changes by rule across the agreed scope, as the general standard requires. For a functional task, keep related style fixes scoped to touched code; do not expand into an unrelated repository-wide cleanup.
6. For review or analysis, report findings with file locations, applicable Drupal source sections and/or full Sonar rule keys, evidence, impact, and a concrete correction. Separate confirmed defects, style recommendations, security hotspots needing assessment, and unresolved version/parameter questions. Do not modify files for a review-only request. For refactors, preserve framework contracts and behavior while addressing applicable rules and checking regressions.
7. Treat additional engineering checks as implementation checks, not as rules claimed to appear in the archive. Do not claim the archive supplies comprehensive security, accessibility, deployment, or feature-development manuals.
8. Apply every relevant exported rule with its exceptions and framework context. Keep required hook/callback parameters, distinguish complete HTML pages from Twig fragments, and check browser/runtime support before introducing new JavaScript APIs. Apply React, Node.js, WordPress, AWS CDK, and other framework-specific guidance only to matching code. For security hotspots, assess the described risk before deciding whether a fix is required; an empty exported `impacts` array is not proof of safety.

## 4. Verify and report

1. Re-read the finished diff for readability and unnecessary complexity using the [simplicity review](references/review-and-validation.md#review-simplicity), then check it against the applicable full Drupal standards and Sonar descriptions, including Drupal fallbacks and exceptions. Check every touched file type, documentation, supporting YAML, and integration boundary. Resolve conflicts through the compatibility workflow; disclose material deviations.
2. Run the project's existing relevant checks using its pinned dependencies and configuration. Discover commands from repository scripts and CI. Use the command patterns in [review and validation](references/review-and-validation.md) only after confirming their prerequisites.
3. Exercise changed behavior with appropriate tests or a targeted manual check. Include relevant failure/empty cases. Distinguish standards checks, syntax checks, behavior tests, and checks that could not run.
4. Inspect the final working tree for unintended edits or generated artifacts. Report what changed, what passed, and any specific remaining limitation. Never report a check as passing merely because a tool is absent or a command ran against zero files.
5. Distinguish bundle-integrity checks, manual Drupal/Sonar review, actual analyzer results, behavior tests, and quality-gate status. Run the existing configured scanner when available and authorized. Do not claim `Sonar passed`, zero findings, or a passing quality gate from reading these rules, running the bundle verifier, or using a different linter.

## Maintain source completeness

Keep all original files under `references/standards/` byte-for-byte unchanged, including images, dictionary, site configuration, and incomplete or obsolete sections. Use the generated source map for navigation rather than rewriting the originals. Do not execute the source CI, copy its debug settings, or install its historical tool examples into a target project automatically.

Use [the source manifest](references/source-manifest.json) and [the bundle verifier](scripts/verify_bundle.py) when auditing or updating this skill:

```bash
python /absolute/path/to/drupal-development/scripts/verify_bundle.py
python /absolute/path/to/drupal-development/scripts/verify_bundle.py --archive /absolute/path/to/coding_standards-main.zip
```

The first command checks bundled file hashes, sizes, document headings, navigation, and direct source links. The second also compares every original archive file and its archive hash. These checks verify reference completeness; use the target project's checks to verify Drupal code.

Preserve the four Sonar exports byte-for-byte as a separate source set. Use [their manifest](references/sonar/manifest.json), [attribution notice](references/sonar/NOTICE.md), full index, and `sonar_rules.py verify` to verify all 566 rules, 1,343 description sections, and 43 contextual sections. `verify_bundle.py` also checks this source set. Use `scripts/test_sonar_rules.py` for loss-detection and retrieval tests. Do not commit either original ZIP to a distribution or reinterpret missing provenance, parameters, or licensing information as known values.
