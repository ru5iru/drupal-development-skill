# Apply Drupal and Sonar guidance together

## Contents

- [State the pre-work summary](#state-the-pre-work-summary)
- [Understand the snapshot](#understand-the-snapshot)
- [Select and read rules](#select-and-read-rules)
- [Apply Drupal fallbacks and resolve conflicts](#apply-drupal-fallbacks-and-resolve-conflicts)
- [Respect context and framework contracts](#respect-context-and-framework-contracts)
- [Review security-sensitive code](#review-security-sensitive-code)
- [Verify and report evidence](#verify-and-report-evidence)
- [Maintain the snapshot](#maintain-the-snapshot)

## State the pre-work summary

Before development, code review, refactoring, or substantive analysis, list:

1. **Scope and intent:** the affected module/theme, behavior, files, and whether the user requested edits or findings only.
2. **Applicable guidance:** relevant Drupal source documents and Sonar language/rule families. Name specific rule keys when already known; refine them after read-only discovery.
3. **Clarifications needed:** list any material unresolved questions, or explicitly state `Clarifications needed: none`.
4. **Assumptions and verification limits:** identify any nonblocking version, parameter, framework, or scanner uncertainty and how it affects the work.

Read repository instructions, project files, lockfiles, existing code, and available analysis reports to answer questions before asking the user. If essential uncertainty remains about behavior, permitted scope, API compatibility, or a genuine rule conflict, ask and wait before dependent edits. Do not block unrelated read-only inspection. Do not ask again for supplied information or require analyzer credentials for an offline review. Identify unknown numeric thresholds only when they matter; the exports alone cannot establish configured limits.

## Understand the snapshot

The user supplied four JSON exports, described as default-enabled Sonar way rules:

| Export | Rule-key prefix | Rules | Code smells | Bugs | Vulnerabilities | Hotspots |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `php.json` | `php:` | 178 | 99 | 43 | 13 | 23 |
| `html.json` | `Web:` | 49 | 33 | 13 | 0 | 3 |
| `css.json` | `css:` | 24 | 9 | 15 | 0 | 0 |
| `js.json` | `javascript:` | 315 | 177 | 75 | 13 | 50 |
| Total | | 566 | 318 | 146 | 26 | 76 |

The exports contain 1,343 description sections and 43 context-specific sections across 32 rules. Nine rules repeat section keys for different contexts. Preserve section arrays and their order; never store sections in a dictionary keyed only by `key`. Keep legacy `severity`/`type` fields and `impacts` separately rather than inventing a severity conversion. All 76 exported hotspots have empty impact arrays; preserve that valid data.

Server/analyzer versions, export time, profile identifiers, active parameter values, project analysis scope, and quality-gate settings were not supplied. Record these as unknown. The snapshot is complete relative to its own reported totals; this does not independently prove which profile produced it or that another Sonar installation has identical defaults. Use actual project/server evidence for current settings without silently overwriting the supplied baseline. Identify deviations explicitly.

Original files: [PHP](sonar/exports/php.json), [HTML](sonar/exports/html.json), [CSS](sonar/exports/css.json), [JavaScript](sonar/exports/js.json). Use [the manifest](sonar/manifest.json) and [complete index](sonar/index.md) to track the fixed source set. The source archive is not needed at runtime.

## Select and read rules

Inspect the complete index for every language and concern involved. Include secondary concerns such as PHP-generated HTML, embedded CSS/JavaScript, tests, regular expressions, authorization, queries, file handling, and build/infrastructure code when present. Do not limit selection to styling rules or a few familiar IDs.

Use the offline helper in the skill's `scripts/` directory:

```bash
python scripts/sonar_rules.py list --language php
python scripts/sonar_rules.py list --language html --search ARIA
python scripts/sonar_rules.py list --language js --type SECURITY_HOTSPOT
python scripts/sonar_rules.py show php:S100 php:S1781
python scripts/sonar_rules.py show php:S5808 --format json
```

Run these from the skill directory or use an absolute script path. `list` searches complete descriptions as well as names/keys. Search hits are candidates, not a compliance result. `show` returns all sections including repeated framework variants, code examples, exceptions, and resource URLs. `--format json` returns the full exported rule objects without transformation; use it to inspect exact source markup and metadata. If Python is unavailable, read the relevant raw JSON entries directly, preserving the complete arrays. Do not fetch external resources merely because they are linked in the descriptions.

## Apply Drupal fallbacks and resolve conflicts

Follow an explicit Drupal-framework fallback in the Sonar description whenever the code is Drupal code. Read the exception itself, not just the generic title. In particular:

- **`php:S1781`:** keep PHP keywords lowercase and Drupal boolean/null literals uppercase (`TRUE`, `FALSE`, `NULL`) as its Drupal-specific description requires. Do not confuse PHPDoc type spelling with code literals.
- **`php:S100`:** follow its Drupal function-naming behavior when Drupal is detected and the default naming expression has not been replaced. Keep module-prefixed procedural names and the distinction between procedural functions and class methods established by the Drupal source. Preserve inherited signatures and magic-method exceptions.

Inspect project evidence for framework context and configured overrides. If the actual scanner fails to detect Drupal or uses an overriding parameter that conflicts with Drupal practices, describe the discrepancy and seek clarification for a material decision. Do not silently change Drupal naming/casing, disable rules, add suppressions, or rewrite the Sonar profile to obtain a clean result.

For another apparent conflict, first read both complete requirements, including MUST/SHOULD distinctions, exceptions, contexts, and version scope. Prefer a solution satisfying both and preserving supported APIs and behavior. If a genuine conflict remains, identify both sources, explain the impact, and clarify the required policy before dependent edits. A rule title is not enough evidence of a conflict.

## Respect context and framework contracts

| Situation | Apply this handling |
| --- | --- |
| `php:S1172` and unused parameters | Do not remove mandatory Drupal hook/callback arguments or inherited/interface parameters. The rule explicitly excludes overriding/interface methods; check other framework contracts before changing signatures. |
| `php:S116` property naming | Account for the Drupal source's underscore allowance for configuration-entity properties. Inspect the active naming expression and scanner context rather than renaming serialized/configuration keys mechanically. |
| Complexity, length, argument-count, duplicate-string, or regex limits | Read any supplied parameter values. Treat numbers appearing only in description examples as documented examples/defaults, not proof of the active server configuration. Do not invent missing limits. |
| `php:S1155` and emptiness checks | Preserve zero, empty string, null, array, object/Countable, and undefined-value semantics. Do not apply `empty()` to arbitrary objects as a substitute for their element count. |
| PHP services, sessions, forms, authorization, SQL, and output | Implement the rule's intent through supported Drupal APIs and existing services; generic PHP or other-framework examples are not drop-in Drupal implementations. |
| `Web:` HTML rules and Twig | Apply rendered markup requirements in context. Page-title/doctype rules concern complete documents, not every component fragment. Preserve Twig escaping and assess `Web:S5247` when raw output or auto-escaping is changed. Static source review does not establish rendered accessibility conformance. |
| JavaScript behaviors and jQuery | Preserve Drupal attach/detach contracts, repeated/AJAX attachment behavior, library dependencies, and translation. Check runtime/browser/toolchain support before modernizing APIs such as ES2022 `Object.hasOwn()` (`javascript:S6653`). |
| React/JSX, Node.js, AWS CDK, WordPress, Laravel, Symfony, and other contexts | Keep all exported rules discoverable. Apply each framework-specific rule or section only to matching code; record a relevant nonapplicability rationale instead of deleting the source rule. |
| CSS and preprocessing | Check whether a file is CSS, Sass/SCSS, Less, or generated output; retain documented exceptions, valid fallbacks, cascade intent, and existing browser requirements. Do not remove a fallback merely from a duplicate-property title. |
| Historical or invalid examples | Extract the intended requirement and write valid version-supported code. For example, the exported `php:S3360` snippet contains `public void`, which must not be copied as PHP method syntax. |

## Review security-sensitive code

Treat exported `VULNERABILITY` and `BUG` rules as checks for defects supported by actual code evidence. For `SECURITY_HOTSPOT`, read the `assess_the_problem`, `default`, and other supplied sections, evaluate trust boundaries and existing protections, and decide whether a fix is required. Do not automatically label every hotspot exploitable or safe. Preserve a reviewed-safe rationale when supported; leave unresolved assessments explicit. An empty `impacts` array is source metadata, not a safety verdict.

Inspect relevant queries, secrets, XML/XXE settings, authentication/session handling, TLS, permissions, uploads/archives, CORS, template escaping, and regular expressions using the full applicable rules. Sonar's own descriptions sometimes state analyzer limitations: for example, `php:S2077` and `javascript:S2077` describe limited tracking of SQL strings. Absence of a finding is not evidence that every path is secure. Do not import unrelated rules from a different profile or claim a complete security audit from this snapshot.

## Verify and report evidence

For development and refactors, review the final diff against both rule sources and exercise behavior/regression cases. For review and analysis, report actionable findings with location, evidence, the exact Drupal source section and/or full Sonar key, the applicable exception/context, impact, and a concrete correction. Separate confirmed findings, recommendations, hotspot assessments, and unresolved questions.

Discover installed tools and existing project commands. Check effective inclusion of Drupal-specific PHP suffixes, `.twig`, embedded languages, test paths, exclusions, and generated/vendor code. Run a configured scanner only within the authorized scope; do not install a server, change profiles, or request credentials just for a manual review. Keep analyzer output and any configured quality gate separate from local lint results and manual reasoning. Report skipped/unavailable checks accurately.

The bundle verifier validates references. It does not execute PHP/JavaScript analysis or establish a passing quality gate. Never report `Sonar passed` without actual matching analyzer evidence.

## Maintain the snapshot

Keep the four JSON files byte-for-byte intact. Record known provenance and leave unavailable metadata null. Preserve SonarSource attribution; the attached exports do not establish redistribution terms. Before publishing their descriptions in a public MIT repository, establish applicable source/version-specific terms and retain separate third-party notices. Do not label SonarSource text as original MIT work.

After an explicitly authorized source refresh, replace the full exports, update provenance, run `python scripts/sonar_rules.py rebuild`, and review all source/index changes. Never regenerate hashes merely to conceal accidental edits. Run `sonar_rules.py verify`, `verify_bundle.py`, and `test_sonar_rules.py`. These checks must retain every rule, full section content, repeated context, type, severity, impact, and indexed key. Keep CI tests resilient to legitimate snapshot and action-pin updates.
