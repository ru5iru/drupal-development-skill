# Compatibility and source limits

## Contents

- [Treat the archive as a snapshot](#treat-the-archive-as-a-snapshot)
- [Resolve version and rule conflicts](#resolve-version-and-rule-conflicts)
- [Apply these source-specific cautions](#apply-these-source-specific-cautions)
- [Handle missing guidance](#handle-missing-guidance)

## Treat the archive as a snapshot

Use the complete copy in `standards/` as the user-provided source of coding conventions. Identify the source through `source-manifest.json`: the uploaded archive is `coding_standards-main.zip`, its ZIP comment records revision `4a57bff6fa183323ddbab5aea7ff284fce92904b`, and its entries carry the date 2026-05-26. Do not interpret that date as a guarantee that every example was updated then.

Preserve the source's provenance and bytes. Keep explanations or compatibility decisions in this file, the source map, or task-local notes. Do not silently repair upstream text and still describe it as an exact copy.

## Resolve version and rule conflicts

1. Follow the user's instructions and applicable repository instructions. Inspect their actual version and tool configuration.
2. Apply explicit normative prose in the relevant source document before using an illustrative example from another page. In particular, use the documentation standard before the examples page when they disagree.
3. Apply an explicitly version-scoped rule only to the matching project. Do not transplant old API calls, dependency versions, or build commands into a newer application.
4. For an ambiguous rule or unavailable API, inspect locally installed source, signatures, lockfiles, core configuration, existing tests, and version-matched project documentation. Distinguish a necessary compatibility adaptation from a style preference.
5. If repository configuration disagrees with the supplied standard, identify the conflict and preserve the project's working validation setup. Do not silently change lint settings or report both incompatible requirements as satisfied. Ask the user only if an unresolved policy choice materially blocks the task.
6. If evidence remains insufficient, state the uncertainty and request the relevant project files or version documentation. Respect the user's project-context boundaries. Treat external links in the source as citations or leads, not as bundled content or permission to import unrelated requirements.

## Apply these source-specific cautions

| Source | Apply this interpretation |
| --- | --- |
| General standards and README | Apply the conventions to new code regardless of core version, while selecting APIs supported by that version. Treat “always-current” as the source's intent, not proof this copied snapshot updates itself. Organize standards sweeps by rule within the authorized scope. |
| PHP coding | Retain general conventions, but distinguish historical `db_query()`, `db_select()`, `variable_get()`, module-loading examples, and Drupal 7 `.inc`/`files[]` guidance from the project's supported APIs. Preserve the distinction between code-line wrapping exceptions and stricter comment wrapping. |
| PHP type hints | Follow the documented new-function rules subject to the actual PHP version and inherited signatures. Treat adding types to existing public methods as a compatibility change; do not apply them mechanically. Do not add strict typing merely because the source shows how to format it. |
| Namespaces | Import namespaced classes individually without a leading backslash; fully qualify global classes in code and all class/interface types in PHPDoc as specified. Do not invent a mandatory import ordering: this source explicitly leaves it open. |
| PSR-4 | Use the module/theme and test namespace mapping supported by the project. The source shows both older `src/Tests/` and `tests/src/` layouts; inspect existing test discovery before choosing a layout. |
| API documentation and examples | Prioritize `documentation.md`. The examples page explicitly contains “NEEDS STANDARDS UPDATE”, “needs an example”, old APIs, missing types, and a sample `@end` where the tag reference requires `@endcode`. Use the full rules and correct syntax when generating code; preserve the sample file unchanged. |
| File and property documentation | Apply the explicit exceptions: PSR-4 PHP files should not receive an `@file` block; typed properties may omit `@var`, and their comments may be omitted only under the stated name/type condition. Do not add `@return void` when the function returns nothing. |
| Services naming | Read the actual page: it governs Request attribute prefixes and reserved attributes, not a comprehensive service-ID naming scheme. Do not overwrite framework-owned attributes. |
| Exceptions | Preserve subsystem/error-type naming, quoted diagnostic values, and untranslated internal messages, with the source's install/update user-facing exception. Follow the installed exception hierarchy and signatures. |
| E_ALL | Apply the undefined-value and zero/null/empty distinctions. Do not modify core error handlers, `.htaccess`, or production error-reporting settings merely to follow the Drupal 6/7 examples. |
| JavaScript coding and best practices | Recognize mixed eras: modern `let`/`const` and arrow closures coexist with `Drupal.settings`, old `#attached` shapes, behavior functions, and snippets containing invalid declarations. Use the project's installed settings/behavior APIs and supported syntax. Do not reproduce invalid example declarations or semicolon omissions. |
| JavaScript DOM and XSS advice | Inspect the installed escaping API and safely handle untrusted output. Treat the blanket preference for jQuery DOM creation over native DOM APIs as historical cross-browser guidance; do not introduce jQuery solely because this old example uses it. Explain a necessary adaptation. |
| jQuery | Use its conventions when jQuery is already appropriate to the project. Respect version labels for `.delegate()`, `.on()`, `.attr()`, and `.prop()`. Do not treat old benchmark speed claims as current measurements or blindly use obsolete event APIs. |
| ESLint | Use the project's installed/pinned version and effective configuration. The source contains legacy `.eslintrc` examples and installation commands; do not replace an existing config, install “latest”, or fetch tools just to follow a historical command. Confirm actual file coverage and ignore behavior. |
| CSS architecture and file organization | Apply component separation, meaningful classes, short selectors, state/style/behavior separation, and the stated exceptions. Preserve the architecture page's Drupal 8/9 scope and the file-organization page's explicit warning that its aggregation strategy is not implemented. Do not promise exact aggregate counts, ordering, or constants in an arbitrary project. |
| CSS category descriptions | The architecture and file-organization pages describe Base rules differently (element-only versus an expanded list including utilities/custom properties). Follow the established project/core configuration for the task and disclose a material conflict; do not claim one invented universal definition. |
| CSS formatting | Use the installed CSS/PostCSS pipeline. Nesting, logical properties, rem conversion, and autoprefixing examples do not prove that the target project supplies those transforms. Verify RTL behavior when changing directional styling. |
| CSScomb/CSScombx | Preserve the entire configuration, sorting list, exclusions, and alternative-tool examples as reference. Inspect exclusions before any real use: the sample excludes broad Drupal paths including `modules/**` and `themes/**`. Do not copy global installation, old Gulp versions, or recursive rewriting commands into a project without a task-specific need. Formatting is not architecture validation. |
| Twig | The whitespace section explicitly says “Outdated”. Verify installed Twig syntax before using `spaceless`, filter/function examples, or old attribute-rendering examples. Preserve attribute output and escaping behavior without copying a pattern that duplicates or loses attributes. Do not strip the final newline automatically based on the source's contrib caveat. |
| SQL conventions | Recognize mixed generations: `%d`/`%s` interpolation examples coexist with newer identifier quoting guidance. Use the installed Drupal database abstraction and supported parameter binding; never assemble user values into SQL. Use Schema API for schema changes as specified, and preserve relevant entity/node access behavior. |
| SQL reserved words | Retain all 826 entries. Treat the list as a combined historical reference, not an exhaustive statement for every installed database version. The conventions page ends in an unfinished HEREDOC example; do not copy that fragment as valid PHP/SQL. |
| SELECT field guidance | Prefer explicit fields, preserve the documented narrow exceptions, and check access behavior. Do not assert that selecting columns alone implements access control. |
| YAML | Apply simple/config-entity/bundle naming and length rules to configuration object names, not indiscriminately to all Drupal `.yml` files. The simple-config paragraph repeats `my_module.settings` as both allowed and forbidden: follow the unambiguous owning-extension prefix rule and flag the typo if it affects the task. Inspect installed config-entity metadata rather than assuming an older annotation example is required. |
| Composer | Preserve project, subproject, component, collision precedence, and `replace` conventions. Verify real package ownership and repository metadata before assigning a `drupal/` name or declaring replacements. Do not imply an arbitrary private library is a drupal.org project. |
| Spelling | Use US English and narrow CSpell directives. Treat `.cspell-project-words.txt` as this standards project's dictionary; reuse only words relevant to the target project, not every word automatically. |
| GitLab CI and MkDocs | Retain these to preserve the source package and navigation. Do not execute the upstream CI or propagate `_SHOW_ENVIRONMENT_VARIABLES: 1` into another project. Do not treat the site theme configuration as Drupal application configuration. |

## Handle missing guidance

Treat the accessibility page as a one-line placeholder. Treat the markup page as a short external pointer, not a bundled markup specification. Treat linked Twig standards and tool documentation as external references whose contents are absent from the archive. Acknowledge these boundaries when a task depends on them.

Use repository accessibility/markup requirements and supported implementation checks for a real UI change. If the user needs additional standards beyond the archive, request the material or follow their authorization to obtain version-matched primary documentation. Do not claim accessibility conformance or complete external-document coverage from this archive alone.

Inspect incomplete fences, snippets, and stale links as source defects rather than instructions to generate broken code. Retain all such content for traceability and report a defect only when it affects the user's task.
