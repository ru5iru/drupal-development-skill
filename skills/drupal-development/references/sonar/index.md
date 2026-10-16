# Complete Sonar way rule index

Use every applicable rule from this fixed, user-supplied snapshot. Read `../sonar-guidance.md` before applying rules or examples.

Read full descriptions using `python scripts/sonar_rules.py show RULE_KEY` from the skill directory. Use `--format json` after `show` for the exact exported fields and HTML. Repeated section names retain their contexts.

## Contents

- [css.json](#cssjson)
- [html.json](#htmljson)
- [js.json](#jsjson)
- [php.json](#phpjson)

## css.json

[Original export](exports/css.json) — 24 rules.

| Rule key | Name | Type | Severity | Context variants |
| --- | --- | --- | --- | --- |
| css:S1116 | Extra semicolons should be removed | CODE_SMELL | MINOR | — |
| css:S1128 | Duplicate imports should be removed | CODE_SMELL | MINOR | — |
| css:S125 | Sections of code should not be commented out | CODE_SMELL | MAJOR | — |
| css:S4647 | Color definitions should be valid | BUG | BLOCKER | — |
| css:S4648 | Duplicated font names should be removed | CODE_SMELL | MAJOR | — |
| css:S4649 | Font declarations should contain at least one generic font family | BUG | MAJOR | — |
| css:S4650 | "calc" operands should be correctly spaced | BUG | BLOCKER | — |
| css:S4651 | "linear-gradient" directions should be valid | BUG | CRITICAL | — |
| css:S4652 | Strings should not contain new lines | CODE_SMELL | MAJOR | — |
| css:S4653 | Units should be valid | BUG | BLOCKER | — |
| css:S4654 | CSS properties should be valid | BUG | BLOCKER | — |
| css:S4655 | "!important" should not be used on "keyframes" | BUG | MAJOR | — |
| css:S4656 | Properties should not be duplicated | BUG | MAJOR | — |
| css:S4657 | Shorthand properties that override related longhand properties should be avoided | BUG | CRITICAL | — |
| css:S4658 | Empty blocks should be removed | CODE_SMELL | MAJOR | — |
| css:S4659 | Pseudo-class selectors should be valid | BUG | MAJOR | — |
| css:S4660 | Pseudo-element selectors should be valid | BUG | MAJOR | — |
| css:S4661 | Media features should be valid | BUG | MAJOR | — |
| css:S4662 | "at-rules" should be valid | BUG | MAJOR | — |
| css:S4663 | Multi-line comments should not be empty | CODE_SMELL | MINOR | — |
| css:S4666 | Selectors should not be duplicated | CODE_SMELL | MAJOR | — |
| css:S4667 | CSS files should not be empty | CODE_SMELL | MAJOR | — |
| css:S4668 | Single line comment syntax should not be used | BUG | BLOCKER | — |
| css:S4670 | Selectors should be known | BUG | CRITICAL | — |

## html.json

[Original export](exports/html.json) — 49 rules.

| Rule key | Name | Type | Severity | Context variants |
| --- | --- | --- | --- | --- |
| Web:AvoidCommentedOutCodeCheck | Sections of code should not be commented out | CODE_SMELL | MAJOR | — |
| Web:DoctypePresenceCheck | "&lt;!DOCTYPE&gt;" declarations should appear before "&lt;html&gt;" tags | BUG | MAJOR | — |
| Web:FlashUsesBothObjectAndEmbedCheck | Flash animations should be embedded using both "&lt;object&gt;" and "&lt;embed&gt;" | BUG | MINOR | — |
| Web:FrameWithoutTitleCheck | "&lt;frames&gt;" should have a "title" attribute | BUG | MINOR | — |
| Web:ImgWithoutAltCheck | Image, area and button with image elements should have an "alt" attribute | CODE_SMELL | MINOR | — |
| Web:ItemTagNotWithinContainerTagCheck | "&lt;li&gt;" and "&lt;dt&gt;" item tags should be in "&lt;ul&gt;", "&lt;ol&gt;" or "&lt;dl&gt;" container tags | BUG | MINOR | — |
| Web:MetaRefreshCheck | Meta tags should not be used to refresh or redirect | CODE_SMELL | MAJOR | — |
| Web:MouseEventWithoutKeyboardEquivalentCheck | Mouse events should have corresponding keyboard events | BUG | MINOR | — |
| Web:PageWithoutTitleCheck | "&lt;title&gt;" should be present in all pages | BUG | MAJOR | — |
| Web:S1134 | Track uses of "FIXME" tags | CODE_SMELL | MAJOR | — |
| Web:S1135 | Track uses of "TODO" tags | CODE_SMELL | INFO | — |
| Web:S1827 | Attributes deprecated in HTML5 should not be used | CODE_SMELL | MAJOR | — |
| Web:S4084 | Videos should have subtitles | CODE_SMELL | MAJOR | — |
| Web:S4645 | &lt;script&gt;...&lt;/script&gt; elements should not be nested | BUG | MAJOR | — |
| Web:S5148 | Authorizing an opened window to access back to the originating window is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| Web:S5247 | Disabling auto-escaping in template engines is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| Web:S5254 | "&lt;html&gt;" element should have a language attribute | BUG | MAJOR | — |
| Web:S5255 | "aria-label" or "aria-labelledby" attributes should be used to differentiate similar elements | CODE_SMELL | MAJOR | — |
| Web:S5256 | Tables should have headers | BUG | MAJOR | — |
| Web:S5257 | HTML "&lt;table&gt;" should not be used for layout purposes | CODE_SMELL | MAJOR | — |
| Web:S5258 | Tables used for layout should not include semantic markup | BUG | CRITICAL | — |
| Web:S5260 | Table cells should reference their headers | BUG | CRITICAL | — |
| Web:S5264 | "&lt;object&gt;" tags should provide an alternative content | CODE_SMELL | MINOR | — |
| Web:S5725 | Using remote artifacts without integrity checks is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| Web:S6793 | ARIA properties in DOM elements should have valid values | CODE_SMELL | MAJOR | — |
| Web:S6807 | DOM elements with ARIA roles should have the required properties | CODE_SMELL | MAJOR | — |
| Web:S6811 | DOM elements with ARIA role should only have supported properties | CODE_SMELL | MAJOR | — |
| Web:S6819 | Prefer tag over ARIA role | CODE_SMELL | MAJOR | — |
| Web:S6821 | DOM elements with ARIA roles should have a valid non-abstract role | CODE_SMELL | MAJOR | — |
| Web:S6822 | No redundant ARIA role | CODE_SMELL | MAJOR | — |
| Web:S6823 | DOM elements with the `aria-activedescendant` property should be accessible via the tab key | CODE_SMELL | MAJOR | — |
| Web:S6824 | No ARIA role or property for unsupported DOM elements | CODE_SMELL | MAJOR | — |
| Web:S6825 | Focusable elements should not have "aria-hidden" attribute | CODE_SMELL | MAJOR | — |
| Web:S6827 | Anchors should contain accessible content | CODE_SMELL | MINOR | — |
| Web:S6840 | DOM elements should use the "autocomplete" attribute correctly | CODE_SMELL | MAJOR | — |
| Web:S6841 | "tabIndex" values should be 0 or -1 | CODE_SMELL | MAJOR | — |
| Web:S6842 | Non-interactive DOM elements should not have interactive ARIA roles | CODE_SMELL | MAJOR | — |
| Web:S6843 | Interactive DOM elements should not have non-interactive ARIA roles | CODE_SMELL | MAJOR | — |
| Web:S6844 | Anchor tags should not be used as buttons | CODE_SMELL | MAJOR | — |
| Web:S6845 | Non-interactive DOM elements should not have the `tabIndex` property | CODE_SMELL | MAJOR | — |
| Web:S6846 | DOM elements should not use the "accesskey" property | CODE_SMELL | MAJOR | — |
| Web:S6847 | Non-interactive elements shouldn't have event handlers | CODE_SMELL | MAJOR | — |
| Web:S6848 | Non-interactive DOM elements should not have an interactive handler | CODE_SMELL | MAJOR | — |
| Web:S6850 | Heading elements should have accessible content | CODE_SMELL | MAJOR | — |
| Web:S6851 | Images should have a non-redundant alternate description | CODE_SMELL | MAJOR | — |
| Web:S6852 | Elements with an interactive role should support focus | CODE_SMELL | MAJOR | — |
| Web:S6853 | Label elements should have a text label and an associated control | CODE_SMELL | MAJOR | — |
| Web:TableHeaderHasIdOrScopeCheck | "&lt;th&gt;" tags should have "id" or "scope" attributes | BUG | MAJOR | — |
| Web:UnsupportedTagsInHtml5Check | Elements deprecated in HTML5 should not be used | BUG | MAJOR | — |

## js.json

[Original export](exports/js.json) — 315 rules.

| Rule key | Name | Type | Severity | Context variants |
| --- | --- | --- | --- | --- |
| javascript:S101 | Class names should comply with a naming convention | CODE_SMELL | MINOR | — |
| javascript:S1068 | Unused private class members should be removed | CODE_SMELL | MAJOR | — |
| javascript:S107 | Functions should not have too many parameters | CODE_SMELL | MAJOR | — |
| javascript:S1077 | Image, area, button with image and object elements should have an alternative text | CODE_SMELL | MINOR | — |
| javascript:S108 | Nested blocks of code should not be left empty | CODE_SMELL | MAJOR | — |
| javascript:S1082 | Mouse events should have corresponding keyboard events | BUG | MINOR | JSX |
| javascript:S1090 | iFrames must have a title | CODE_SMELL | MINOR | — |
| javascript:S1119 | Labels should not be used | CODE_SMELL | MAJOR | — |
| javascript:S1121 | Assignments should not be made from within sub-expressions | CODE_SMELL | MAJOR | — |
| javascript:S1125 | Boolean literals should not be used in comparisons | CODE_SMELL | MINOR | — |
| javascript:S1126 | Return of boolean expressions should not be wrapped into an "if-then-else" statement | CODE_SMELL | MINOR | — |
| javascript:S1128 | Unnecessary imports should be removed | CODE_SMELL | MINOR | — |
| javascript:S1134 | Track uses of "FIXME" tags | CODE_SMELL | MAJOR | — |
| javascript:S1135 | Track uses of "TODO" tags | CODE_SMELL | INFO | — |
| javascript:S1143 | Jump statements should not occur in "finally" blocks | BUG | CRITICAL | — |
| javascript:S1186 | Functions should not be empty | CODE_SMELL | CRITICAL | — |
| javascript:S1199 | Nested code blocks should not be used | CODE_SMELL | MINOR | — |
| javascript:S1219 | "switch" statements should not contain non-case labels | CODE_SMELL | BLOCKER | — |
| javascript:S1226 | Initial values of parameters, caught exceptions, and loop variables should not be ignored | BUG | MINOR | — |
| javascript:S125 | Sections of code should not be commented out | CODE_SMELL | MAJOR | — |
| javascript:S1264 | A "while" loop should be used instead of a "for" loop | CODE_SMELL | MINOR | — |
| javascript:S128 | Switch cases should end with an unconditional "break" statement | CODE_SMELL | BLOCKER | — |
| javascript:S1301 | "if" statements should be preferred over "switch" when simpler | CODE_SMELL | MINOR | — |
| javascript:S1313 | Using hardcoded IP addresses is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S1314 | Octal values should not be used | CODE_SMELL | BLOCKER | — |
| javascript:S1321 | "with" statements should not be used | BUG | MINOR | — |
| javascript:S1439 | Only "while", "do", "for" and "switch" statements should be labelled | CODE_SMELL | MAJOR | — |
| javascript:S1472 | Function call arguments should not start on new lines | CODE_SMELL | MINOR | — |
| javascript:S1479 | "switch" statements should not have too many "case" clauses | CODE_SMELL | MAJOR | — |
| javascript:S1481 | Unused local variables and functions should be removed | CODE_SMELL | MINOR | — |
| javascript:S1515 | Functions should not be defined inside loops | CODE_SMELL | MAJOR | — |
| javascript:S1516 | Multiline string literals should not be used | CODE_SMELL | MINOR | — |
| javascript:S1523 | Dynamically executing code is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| javascript:S1527 | Future reserved words should not be used as identifiers | CODE_SMELL | BLOCKER | — |
| javascript:S1529 | Bitwise operators should not be used in boolean contexts | BUG | MAJOR | — |
| javascript:S1533 | Wrapper objects should not be used for primitive types | CODE_SMELL | MINOR | — |
| javascript:S1534 | Member names should not be duplicated within a class or object literal | BUG | MAJOR | — |
| javascript:S1536 | Function argument names should be unique | BUG | MAJOR | — |
| javascript:S1607 | Tests should not be skipped without providing a reason | CODE_SMELL | MAJOR | Mocha, Node.js, Jest, Jasmine |
| javascript:S1656 | Variables should not be self-assigned | BUG | MAJOR | — |
| javascript:S1751 | Loops with at most one iteration should be refactored | BUG | MAJOR | — |
| javascript:S1763 | All code should be reachable | BUG | MAJOR | — |
| javascript:S1764 | Identical expressions should not be used on both sides of a binary operator | BUG | MAJOR | — |
| javascript:S1788 | Function parameters with default values should be last | CODE_SMELL | MAJOR | — |
| javascript:S1848 | Objects should not be created to be dropped immediately without being used | BUG | MAJOR | — |
| javascript:S1854 | Unused assignments should be removed | CODE_SMELL | MAJOR | — |
| javascript:S1862 | "if/else if" chains and "switch" cases should not have the same condition | BUG | MAJOR | — |
| javascript:S1871 | Two branches in a conditional structure should not have exactly the same implementation | CODE_SMELL | MAJOR | — |
| javascript:S1874 | Deprecated APIs should not be used | CODE_SMELL | MINOR | — |
| javascript:S1940 | Boolean checks should not be inverted | CODE_SMELL | MINOR | — |
| javascript:S1994 | "for" loop increment clauses should modify the loops' counters | CODE_SMELL | CRITICAL | — |
| javascript:S2004 | Functions should not be nested too deeply | CODE_SMELL | CRITICAL | — |
| javascript:S2068 | Hard-coded passwords are security-sensitive | SECURITY_HOTSPOT | BLOCKER | — |
| javascript:S2077 | Formatting SQL queries is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S2092 | Creating cookies without the "secure" flag is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S2094 | Classes should not be empty | CODE_SMELL | MINOR | — |
| javascript:S2123 | Values should not be uselessly incremented | BUG | MAJOR | — |
| javascript:S2137 | Special identifiers should not be bound or assigned | BUG | MAJOR | — |
| javascript:S2187 | Test files should contain at least one test case | CODE_SMELL | BLOCKER | — |
| javascript:S2189 | Loops should not be infinite | BUG | BLOCKER | — |
| javascript:S2201 | Return values from functions without side effects should not be ignored | BUG | MAJOR | — |
| javascript:S2234 | Parameters should be passed in the correct order | CODE_SMELL | MAJOR | — |
| javascript:S2245 | Using pseudorandom number generators (PRNGs) is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| javascript:S2251 | A "for" loop update clause should move the counter in the right direction | BUG | MAJOR | — |
| javascript:S2259 | Properties of variables with "null" or "undefined" values should not be accessed | BUG | MAJOR | — |
| javascript:S2301 | Methods should not contain selector parameters | CODE_SMELL | MAJOR | — |
| javascript:S2310 | Loop counters should not be assigned within the loop body | CODE_SMELL | MAJOR | — |
| javascript:S2392 | Variables should be used in the blocks where they are declared | CODE_SMELL | MAJOR | — |
| javascript:S2430 | Constructor names should start with an upper case letter | CODE_SMELL | CRITICAL | — |
| javascript:S2432 | Setters should not return values | BUG | MAJOR | — |
| javascript:S2486 | Exceptions should not be ignored | CODE_SMELL | MINOR | — |
| javascript:S2589 | Boolean expressions should not be gratuitous | CODE_SMELL | MAJOR | — |
| javascript:S2598 | File uploads should be restricted | VULNERABILITY | CRITICAL | Multer, Formidable |
| javascript:S2612 | Setting loose POSIX file permissions is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S2639 | Empty character classes should not be used | BUG | MAJOR | — |
| javascript:S2681 | Multiline blocks should be enclosed in curly braces | CODE_SMELL | MAJOR | — |
| javascript:S2685 | "arguments.caller" and "arguments.callee" should not be used | CODE_SMELL | MAJOR | — |
| javascript:S2688 | "NaN" should not be used in comparisons | BUG | MAJOR | — |
| javascript:S2692 | "indexOf" checks should not be for positive numbers | CODE_SMELL | MAJOR | — |
| javascript:S2699 | Tests should include assertions | CODE_SMELL | BLOCKER | — |
| javascript:S2703 | Variables should be declared explicitly | CODE_SMELL | BLOCKER | — |
| javascript:S2737 | "catch" clauses should do more than rethrow | CODE_SMELL | MINOR | — |
| javascript:S2755 | XML parsers should not be vulnerable to XXE attacks | VULNERABILITY | BLOCKER | libxmljs |
| javascript:S2757 | Non-existent operators '=+', '=-' and '=!' should not be used | BUG | MAJOR | — |
| javascript:S2814 | Variables and functions should not be redeclared | CODE_SMELL | MAJOR | — |
| javascript:S2819 | Origins should be verified during cross-origin communications | VULNERABILITY | CRITICAL | — |
| javascript:S2870 | "delete" should not be used on arrays | CODE_SMELL | MAJOR | — |
| javascript:S2871 | "Array.prototype.sort()" and "Array.prototype.toSorted()" should use a compare function | BUG | CRITICAL | — |
| javascript:S2970 | Assertions should be complete | CODE_SMELL | BLOCKER | — |
| javascript:S2990 | The global "this" object should not be used | CODE_SMELL | MINOR | — |
| javascript:S2999 | "new" should only be used with functions and classes | BUG | MAJOR | — |
| javascript:S3001 | "delete" should be used only with object properties | BUG | MINOR | — |
| javascript:S3330 | Creating cookies without the "HttpOnly" flag is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S3358 | Ternary operators should not be nested | CODE_SMELL | MAJOR | — |
| javascript:S3403 | Strict equality operators should not be used with dissimilar types | BUG | MAJOR | — |
| javascript:S3415 | Assertion arguments should be passed in the correct order | CODE_SMELL | MAJOR | — |
| javascript:S3500 | "const" variables should not be reassigned | BUG | MAJOR | — |
| javascript:S3504 | Variables should be declared with "let" or "const" | CODE_SMELL | CRITICAL | — |
| javascript:S3516 | Function returns should not be invariant | CODE_SMELL | BLOCKER | — |
| javascript:S3531 | Generators should explicitly "yield" a value | BUG | MAJOR | — |
| javascript:S3579 | Array indexes should be numeric | CODE_SMELL | MAJOR | — |
| javascript:S3616 | Comma and logical OR operators should not be used in switch cases | BUG | MAJOR | — |
| javascript:S3626 | Jump statements should not be redundant | CODE_SMELL | MINOR | — |
| javascript:S3686 | Functions should be called consistently with or without "new" | CODE_SMELL | MAJOR | — |
| javascript:S3696 | Literals should not be thrown | CODE_SMELL | MAJOR | — |
| javascript:S3699 | The return value of void functions should not be used | BUG | MAJOR | — |
| javascript:S3735 | "void" should not be used | CODE_SMELL | CRITICAL | — |
| javascript:S3776 | Cognitive Complexity of functions should not be too high | CODE_SMELL | CRITICAL | — |
| javascript:S3782 | Arguments to built-in functions should match documented types | CODE_SMELL | MAJOR | — |
| javascript:S3785 | "in" should not be used with primitive types | BUG | CRITICAL | — |
| javascript:S3796 | Callbacks of array methods should have return statements | BUG | BLOCKER | — |
| javascript:S3799 | Destructuring patterns should not be empty | BUG | MAJOR | — |
| javascript:S3800 | Functions should always return the same type | CODE_SMELL | MAJOR | — |
| javascript:S3812 | Parentheses should be used when negating "in" and "instanceof" operations | BUG | CRITICAL | — |
| javascript:S3834 | "new" operator should not be used with Symbol and BigInt | BUG | CRITICAL | — |
| javascript:S3854 | "super()" should be invoked appropriately | BUG | CRITICAL | — |
| javascript:S3863 | Imports from the same module should be merged | CODE_SMELL | MINOR | — |
| javascript:S3923 | All branches in a conditional structure should not have exactly the same implementation | BUG | MAJOR | — |
| javascript:S3972 | Conditionals should start on new lines | CODE_SMELL | CRITICAL | — |
| javascript:S3981 | Collection size and array length comparisons should make sense | BUG | MAJOR | — |
| javascript:S3984 | Errors should not be created without being thrown | BUG | MAJOR | — |
| javascript:S4030 | Collection contents should be used | CODE_SMELL | MAJOR | — |
| javascript:S4036 | Searching OS commands in PATH is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S4043 | Array-mutating methods should not be used misleadingly | CODE_SMELL | MAJOR | — |
| javascript:S4084 | Media elements should have captions | CODE_SMELL | MINOR | — |
| javascript:S4123 | "await" should only be used with promises | CODE_SMELL | CRITICAL | — |
| javascript:S4125 | "typeof" expressions should only be compared to valid values | BUG | CRITICAL | — |
| javascript:S4138 | "for of" should be used with Iterables | CODE_SMELL | MINOR | — |
| javascript:S4140 | Sparse arrays should not be created with extra commas | CODE_SMELL | MAJOR | — |
| javascript:S4143 | Collection elements should not be replaced unconditionally | BUG | MAJOR | — |
| javascript:S4144 | Functions should not have identical implementations | CODE_SMELL | MAJOR | — |
| javascript:S4158 | Empty collections should not be accessed or iterated | BUG | MINOR | — |
| javascript:S4165 | Assignments should not be redundant | CODE_SMELL | MAJOR | — |
| javascript:S4275 | Getters and setters should access the expected fields | BUG | CRITICAL | — |
| javascript:S4423 | Weak SSL/TLS protocols should not be used | VULNERABILITY | CRITICAL | Node.js, AWS CDK |
| javascript:S4426 | Cryptographic keys should be robust | VULNERABILITY | CRITICAL | Node.js |
| javascript:S4502 | Disabling CSRF protections is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| javascript:S4507 | Delivering code in production with debug features activated is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S4524 | "default" clauses should be last | CODE_SMELL | CRITICAL | — |
| javascript:S4619 | "in" should not be used on arrays | CODE_SMELL | MAJOR | — |
| javascript:S4624 | Template literals should not be nested | CODE_SMELL | MAJOR | — |
| javascript:S4634 | Shorthand promises should be used | CODE_SMELL | MAJOR | — |
| javascript:S4721 | Using shell interpreter when executing OS commands is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S4790 | Using weak hashing algorithms is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| javascript:S4822 | Promise rejections should not be caught by "try" blocks | BUG | MAJOR | — |
| javascript:S4830 | Server certificates should be verified during SSL/TLS connections | VULNERABILITY | CRITICAL | Node.js, Request |
| javascript:S5042 | Expanding archive files without controlling resource consumption is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| javascript:S5122 | Having a permissive Cross-Origin Resource Sharing policy is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5148 | Authorizing an opened window to access back to the originating window is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5247 | Disabling auto-escaping in template engines is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S5254 | HTML elements should have a valid language attribute | CODE_SMELL | MAJOR | — |
| javascript:S5256 | Tables should have headers | BUG | MAJOR | — |
| javascript:S5257 | HTML "&lt;table&gt;" should not be used for layout purposes | CODE_SMELL | MAJOR | — |
| javascript:S5260 | Table cells should reference their headers | BUG | CRITICAL | — |
| javascript:S5264 | "&lt;object&gt;" tags should provide an alternative content | CODE_SMELL | MINOR | — |
| javascript:S5332 | Using clear-text protocols is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| javascript:S5443 | Using publicly writable directories is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| javascript:S5527 | Server hostnames should be verified during SSL/TLS connections | VULNERABILITY | CRITICAL | Node.js |
| javascript:S5542 | Encryption algorithms should be used with secure mode and padding scheme | VULNERABILITY | CRITICAL | Node.js |
| javascript:S5547 | Cipher algorithms should be robust | VULNERABILITY | CRITICAL | Node.js |
| javascript:S5604 | Using intrusive permissions is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S5659 | JWT should be signed and verified with strong cipher algorithms | VULNERABILITY | CRITICAL | jsonwebtoken |
| javascript:S5689 | Disclosing fingerprints from web application technologies is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5691 | Statically serving hidden files is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S5693 | Allowing requests with excessive content length is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S5725 | Using remote artifacts without integrity checks is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5728 | Disabling content security policy fetch directives is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5730 | Allowing mixed-content is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5732 | Disabling content security policy frame-ancestors directive is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5734 | Allowing browsers to sniff MIME types is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5736 | Disabling strict HTTP no-referrer policy is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5739 | Disabling Strict-Transport-Security policy is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5757 | Allowing confidential information to be logged is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5759 | Forwarding client IP address is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S5842 | Repeated patterns in regular expressions should not match the empty string | BUG | MINOR | — |
| javascript:S5843 | Regular expressions should not be too complicated | CODE_SMELL | MAJOR | — |
| javascript:S5850 | Alternatives in regular expressions should be grouped when used with anchors | BUG | MAJOR | — |
| javascript:S5852 | Using slow regular expressions is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| javascript:S5856 | Regular expressions should be syntactically valid | BUG | CRITICAL | — |
| javascript:S5860 | Names of regular expressions named groups should be used | CODE_SMELL | MAJOR | — |
| javascript:S5863 | Assertions should not be given twice the same argument | BUG | MAJOR | — |
| javascript:S5868 | Unicode Grapheme Clusters should be avoided inside regex character classes | BUG | MAJOR | — |
| javascript:S5869 | Character classes in regular expressions should not contain the same character twice | CODE_SMELL | MAJOR | — |
| javascript:S5876 | A new session should be created during user authentication | VULNERABILITY | CRITICAL | Passport |
| javascript:S5958 | Tests should check which exception is thrown | CODE_SMELL | MAJOR | — |
| javascript:S5973 | Tests should be stable | CODE_SMELL | MAJOR | — |
| javascript:S6019 | Reluctant quantifiers in regular expressions should be followed by an expression that can't match the empty string | CODE_SMELL | MAJOR | — |
| javascript:S6035 | Single-character alternations in regular expressions should be replaced with character classes | CODE_SMELL | MAJOR | — |
| javascript:S6079 | Tests should not execute any code after "done()" is called | CODE_SMELL | CRITICAL | — |
| javascript:S6080 | Disabling Mocha timeouts should be explicit | BUG | MAJOR | — |
| javascript:S6092 | Chai assertions should have only one reason to succeed | CODE_SMELL | MAJOR | — |
| javascript:S6249 | Authorizing HTTP communications with S3 buckets is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| javascript:S6252 | Disabling versioning of S3 buckets is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| javascript:S6265 | Granting access to S3 buckets to all or authenticated users is security-sensitive | SECURITY_HOTSPOT | BLOCKER | — |
| javascript:S6268 | Disabling Angular built-in sanitization is security-sensitive | SECURITY_HOTSPOT | BLOCKER | — |
| javascript:S6270 | Policies authorizing public access to resources are security-sensitive | SECURITY_HOTSPOT | BLOCKER | — |
| javascript:S6275 | Using unencrypted EBS volumes is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S6281 | Allowing public ACLs or policies on a S3 bucket is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| javascript:S6302 | Policies granting all privileges are security-sensitive | SECURITY_HOTSPOT | BLOCKER | — |
| javascript:S6303 | Using unencrypted RDS DB resources is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S6308 | Using unencrypted Elasticsearch domains is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S6317 | AWS IAM policies should limit the scope of permissions given | VULNERABILITY | CRITICAL | AWS CDK |
| javascript:S6319 | Using unencrypted SageMaker notebook instances is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S6321 | Administration services access should be restricted to specific IP addresses | VULNERABILITY | MINOR | — |
| javascript:S6323 | Alternation in regular expressions should not contain empty alternatives | BUG | MAJOR | — |
| javascript:S6324 | Regular expressions should not contain control characters | BUG | MAJOR | — |
| javascript:S6325 | Regular expression literals should be used when possible | CODE_SMELL | MINOR | — |
| javascript:S6326 | Regular expressions should not contain multiple spaces | CODE_SMELL | MAJOR | — |
| javascript:S6327 | Using unencrypted SNS topics is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S6328 | Replacement strings should reference existing regular expression groups | BUG | MAJOR | — |
| javascript:S6329 | Allowing public network access to cloud resources is security-sensitive | SECURITY_HOTSPOT | BLOCKER | — |
| javascript:S6330 | Using unencrypted SQS queues is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S6331 | Regular expressions should not contain empty groups | CODE_SMELL | MAJOR | — |
| javascript:S6332 | Using unencrypted EFS file systems is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| javascript:S6333 | Creating public APIs is security-sensitive | SECURITY_HOTSPOT | BLOCKER | — |
| javascript:S6351 | Regular expressions with the global flag should be used with caution | BUG | MAJOR | — |
| javascript:S6353 | Regular expression quantifiers and character classes should be used concisely | CODE_SMELL | MINOR | — |
| javascript:S6397 | Character classes in regular expressions should not contain only one character | CODE_SMELL | MAJOR | — |
| javascript:S6418 | Hard-coded secrets are security-sensitive | SECURITY_HOTSPOT | BLOCKER | — |
| javascript:S6426 | Exclusive tests should not be commited to version control | BUG | MAJOR | — |
| javascript:S6435 | React "render" functions should return a value | BUG | MAJOR | — |
| javascript:S6438 | Comments inside JSX expressions should be enclosed in curly braces | BUG | MAJOR | — |
| javascript:S6439 | React components should not render non-boolean condition values | BUG | MAJOR | — |
| javascript:S6440 | React Hooks should be properly called | BUG | MAJOR | — |
| javascript:S6441 | Unused methods of React components should be removed | CODE_SMELL | MAJOR | — |
| javascript:S6442 | React's useState hook should not be used directly in the render function or body of a component | BUG | MAJOR | — |
| javascript:S6443 | React state setter function should not be called with its matching state variable | BUG | MAJOR | — |
| javascript:S6477 | JSX list components should have a key property | CODE_SMELL | MAJOR | — |
| javascript:S6478 | React components should not be nested | CODE_SMELL | MAJOR | — |
| javascript:S6479 | JSX list components should not use array indexes as key | CODE_SMELL | MAJOR | — |
| javascript:S6481 | React Context Provider values should have stable identities | CODE_SMELL | MAJOR | — |
| javascript:S6486 | JSX list components keys should match up between renders | CODE_SMELL | MAJOR | — |
| javascript:S6509 | Extra boolean casts should be removed | CODE_SMELL | MINOR | — |
| javascript:S6522 | Import variables should not be reassigned | CODE_SMELL | MAJOR | — |
| javascript:S6523 | Optional chaining should not be used if returning "undefined" throws an error | BUG | MAJOR | — |
| javascript:S6534 | Numbers should not lose precision | BUG | MAJOR | — |
| javascript:S6535 | Unnecessary character escapes should be removed | CODE_SMELL | MAJOR | — |
| javascript:S6544 | Promises should not be misused | BUG | MAJOR | — |
| javascript:S6551 | Objects and classes converted or coerced to strings should define a "toString()" method | CODE_SMELL | MINOR | — |
| javascript:S6557 | Ends of strings should be checked with "startsWith()" and "endsWith()" | CODE_SMELL | MAJOR | — |
| javascript:S6582 | Optional chaining should be preferred | CODE_SMELL | MAJOR | — |
| javascript:S6594 | "RegExp.exec()" should be preferred over "String.match()" | CODE_SMELL | MINOR | — |
| javascript:S6627 | Users should not use internal APIs | CODE_SMELL | MAJOR | — |
| javascript:S6635 | Constructors should not return values | CODE_SMELL | MINOR | — |
| javascript:S6637 | Unnecessary calls to ".bind()" should not be used | CODE_SMELL | MINOR | — |
| javascript:S6638 | Binary expressions should not always return the same value | BUG | MAJOR | — |
| javascript:S6643 | Prototypes of builtin objects should not be modified | CODE_SMELL | MAJOR | — |
| javascript:S6644 | Ternary operator should not be used instead of simpler alternatives | CODE_SMELL | MINOR | — |
| javascript:S6645 | Variables should not be initialized to undefined | CODE_SMELL | MINOR | — |
| javascript:S6647 | Unnecessary constructors should be removed | CODE_SMELL | MINOR | — |
| javascript:S6650 | Renaming import, export, and destructuring assignments should not be to the same name | CODE_SMELL | MINOR | — |
| javascript:S6653 | Use Object.hasOwn static method instead of hasOwnProperty | CODE_SMELL | MINOR | — |
| javascript:S6654 | __proto__ property should not be used | CODE_SMELL | MINOR | — |
| javascript:S6657 | Octal escape sequences should not be used | CODE_SMELL | MAJOR | — |
| javascript:S6660 | If statements should not be the only statement in else blocks | CODE_SMELL | MAJOR | — |
| javascript:S6661 | Object spread syntax should be used instead of "Object.assign" | CODE_SMELL | MAJOR | — |
| javascript:S6666 | Spread syntax should be used instead of "apply()" | CODE_SMELL | MAJOR | — |
| javascript:S6671 | Literals should not be used for promise rejection | CODE_SMELL | MAJOR | — |
| javascript:S6676 | Calls to ".call()" and ".apply()" methods should not be redundant | CODE_SMELL | MAJOR | — |
| javascript:S6679 | "Number.isNaN()" should be used to check for "NaN" value | CODE_SMELL | MAJOR | — |
| javascript:S6746 | In React "this.state" should not be mutated directly | CODE_SMELL | MAJOR | — |
| javascript:S6747 | JSX elements should not use unknown properties and attributes | CODE_SMELL | MAJOR | — |
| javascript:S6748 | React "children" should not be passed as prop | CODE_SMELL | MAJOR | — |
| javascript:S6749 | Redundant React fragments should be removed | CODE_SMELL | MINOR | — |
| javascript:S6750 | The return value of "ReactDOM.render" should not be used | CODE_SMELL | MAJOR | — |
| javascript:S6754 | The return value of "useState" should be destructured and named symmetrically | CODE_SMELL | MINOR | — |
| javascript:S6756 | "setState" should use a callback when referencing the previous state | BUG | MAJOR | — |
| javascript:S6757 | "this" should not be used in functional components | BUG | MAJOR | — |
| javascript:S6761 | "children" and "dangerouslySetInnerHTML" should not be used together | BUG | MAJOR | — |
| javascript:S6763 | "shouldComponentUpdate" should not be defined when extending "React.PureComponent" | CODE_SMELL | MAJOR | — |
| javascript:S6766 | JSX special characters should be escaped | CODE_SMELL | MAJOR | — |
| javascript:S6767 | Unused React typed props should be removed | CODE_SMELL | MINOR | TypeScript, PropTypes |
| javascript:S6770 | User-defined JSX components should use Pascal case | CODE_SMELL | MINOR | — |
| javascript:S6772 | Spacing between inline elements should be explicit | CODE_SMELL | MAJOR | — |
| javascript:S6774 | React components should validate prop types | CODE_SMELL | MAJOR | — |
| javascript:S6775 | All "defaultProps" should have non-required PropTypes | CODE_SMELL | MINOR | PropTypes, TypeScript |
| javascript:S6788 | React's "findDOMNode" should not be used | CODE_SMELL | MAJOR | — |
| javascript:S6789 | React's "isMounted" should not be used | CODE_SMELL | MAJOR | — |
| javascript:S6790 | String references should not be used | CODE_SMELL | MAJOR | — |
| javascript:S6791 | React legacy lifecycle methods should not be used | CODE_SMELL | MAJOR | — |
| javascript:S6793 | ARIA properties in DOM elements should have valid values | CODE_SMELL | MAJOR | — |
| javascript:S6807 | DOM elements with ARIA roles should have the required properties | CODE_SMELL | MAJOR | — |
| javascript:S6811 | DOM elements with ARIA role should only have supported properties | CODE_SMELL | MAJOR | — |
| javascript:S6819 | Prefer tag over ARIA role | CODE_SMELL | MAJOR | — |
| javascript:S6821 | DOM elements with ARIA roles should have a valid non-abstract role | CODE_SMELL | MAJOR | — |
| javascript:S6822 | No redundant ARIA role | CODE_SMELL | MAJOR | — |
| javascript:S6823 | DOM elements with the `aria-activedescendant` property should be accessible via the tab key | CODE_SMELL | MAJOR | JSX |
| javascript:S6824 | No ARIA role or property for unsupported DOM elements | CODE_SMELL | MAJOR | — |
| javascript:S6825 | Focusable elements should not have "aria-hidden" attribute | CODE_SMELL | MAJOR | — |
| javascript:S6827 | Anchors should contain accessible content | CODE_SMELL | MINOR | — |
| javascript:S6836 | "case" and "default" clauses should not contain lexical declarations | CODE_SMELL | MAJOR | — |
| javascript:S6840 | DOM elements should use the "autocomplete" attribute correctly | CODE_SMELL | MAJOR | — |
| javascript:S6841 | "tabIndex" values should be 0 or -1 | CODE_SMELL | MAJOR | — |
| javascript:S6842 | Non-interactive DOM elements should not have interactive ARIA roles | CODE_SMELL | MAJOR | — |
| javascript:S6843 | Interactive DOM elements should not have non-interactive ARIA roles | CODE_SMELL | MAJOR | — |
| javascript:S6844 | Anchor tags should not be used as buttons | CODE_SMELL | MAJOR | — |
| javascript:S6845 | Non-interactive DOM elements should not have the `tabIndex` property | CODE_SMELL | MAJOR | — |
| javascript:S6846 | DOM elements should not use the "accesskey" property | CODE_SMELL | MAJOR | — |
| javascript:S6847 | Non-interactive elements shouldn't have event handlers | CODE_SMELL | MAJOR | — |
| javascript:S6848 | Non-interactive DOM elements should not have an interactive handler | CODE_SMELL | MAJOR | — |
| javascript:S6850 | Heading elements should have accessible content | CODE_SMELL | MAJOR | — |
| javascript:S6851 | Images should have a non-redundant alternate description | CODE_SMELL | MAJOR | — |
| javascript:S6852 | Elements with an interactive role should support focus | CODE_SMELL | MAJOR | — |
| javascript:S6853 | Label elements should have a text label and an associated control | CODE_SMELL | MAJOR | — |
| javascript:S6859 | Imports should not use absolute paths | CODE_SMELL | CRITICAL | — |
| javascript:S6861 | Mutable variables should not be exported | CODE_SMELL | CRITICAL | — |
| javascript:S6957 | Deprecated React APIs should not be used | CODE_SMELL | MINOR | — |
| javascript:S6958 | Literals should not be used as functions | BUG | CRITICAL | — |
| javascript:S6959 | "Array.reduce()" calls should include an initial value | BUG | MAJOR | — |
| javascript:S7059 | Constructors should not contain asynchronous operations | CODE_SMELL | CRITICAL | — |
| javascript:S7060 | Module should not import itself | CODE_SMELL | MAJOR | — |
| javascript:S878 | Comma operator should not be used | CODE_SMELL | MAJOR | — |
| javascript:S888 | Equality operators should not be used in "for" loop termination conditions | CODE_SMELL | CRITICAL | — |
| javascript:S905 | Non-empty statements should change control flow or have at least one side-effect | BUG | MAJOR | — |
| javascript:S930 | Function calls should not pass extra arguments | BUG | CRITICAL | — |

## php.json

[Original export](exports/php.json) — 178 rules.

| Rule key | Name | Type | Severity | Context variants |
| --- | --- | --- | --- | --- |
| php:S100 | Function names should comply with a naming convention | CODE_SMELL | MINOR | — |
| php:S101 | Class names should comply with a naming convention | CODE_SMELL | MINOR | — |
| php:S1045 | All "catch" blocks should be able to catch exceptions | BUG | MAJOR | — |
| php:S105 | Tabulation characters should not be used | CODE_SMELL | MINOR | — |
| php:S1066 | Mergeable "if" statements should be combined | CODE_SMELL | MAJOR | — |
| php:S1068 | Unused "private" fields should be removed | CODE_SMELL | MAJOR | — |
| php:S107 | Functions should not have too many parameters | CODE_SMELL | MAJOR | — |
| php:S1075 | URIs should not be hardcoded | CODE_SMELL | MINOR | — |
| php:S108 | Nested blocks of code should not be left empty | CODE_SMELL | MAJOR | — |
| php:S110 | Inheritance tree of classes should not be too deep | CODE_SMELL | MAJOR | — |
| php:S1109 | A close curly brace should be located at the beginning of a line | CODE_SMELL | MINOR | — |
| php:S1110 | Redundant pairs of parentheses should be removed | CODE_SMELL | MAJOR | — |
| php:S1116 | Empty statements should be removed | CODE_SMELL | MINOR | — |
| php:S112 | Generic exceptions ErrorException, RuntimeException and Exception should not be thrown | CODE_SMELL | MAJOR | — |
| php:S1124 | Modifiers should be declared in the correct order | CODE_SMELL | MINOR | — |
| php:S1125 | Boolean literals should not be redundant | CODE_SMELL | MINOR | — |
| php:S1126 | Return of boolean expressions should not be wrapped into an "if-then-else" statement | CODE_SMELL | MINOR | — |
| php:S113 | Files should end with a newline | CODE_SMELL | MINOR | — |
| php:S1131 | Lines should not end with trailing whitespaces | CODE_SMELL | MINOR | — |
| php:S1134 | Track uses of "FIXME" tags | CODE_SMELL | MAJOR | — |
| php:S1135 | Track uses of "TODO" tags | CODE_SMELL | INFO | — |
| php:S114 | Interface names should comply with a naming convention | CODE_SMELL | MINOR | — |
| php:S1142 | Functions should not contain too many return statements | CODE_SMELL | MAJOR | — |
| php:S1144 | Unused "private" methods should be removed | CODE_SMELL | MAJOR | — |
| php:S1145 | Useless "if(true) {...}" and "if(false){...}" blocks should be removed | BUG | MAJOR | — |
| php:S115 | Constant names should comply with a naming convention | CODE_SMELL | CRITICAL | — |
| php:S1155 | "empty()" should be used to test for emptiness | CODE_SMELL | MINOR | — |
| php:S116 | Field names should comply with a naming convention | CODE_SMELL | MINOR | — |
| php:S117 | Local variable and function parameter names should comply with a naming convention | CODE_SMELL | MINOR | — |
| php:S1172 | Unused function parameters should be removed | CODE_SMELL | MAJOR | — |
| php:S1185 | Overriding methods should do more than simply call the same method in the super class | CODE_SMELL | MINOR | — |
| php:S1186 | Methods should not be empty | CODE_SMELL | CRITICAL | — |
| php:S1192 | String literals should not be duplicated | CODE_SMELL | CRITICAL | — |
| php:S121 | Control structures should use curly braces | CODE_SMELL | CRITICAL | — |
| php:S1226 | Function and method parameters' initial values should not be ignored | BUG | MINOR | — |
| php:S125 | Sections of code should not be commented out | CODE_SMELL | MAJOR | — |
| php:S1264 | A "while" loop should be used instead of a "for" loop | CODE_SMELL | MINOR | — |
| php:S127 | "for" loop stop conditions should be invariant | CODE_SMELL | MAJOR | — |
| php:S128 | Switch cases should end with an unconditional "break" statement | CODE_SMELL | BLOCKER | — |
| php:S1301 | "switch" statements should have at least 3 "case" clauses | CODE_SMELL | MINOR | — |
| php:S131 | "switch" statements should have "default" clauses | CODE_SMELL | CRITICAL | — |
| php:S1313 | Using hardcoded IP addresses is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| php:S138 | Functions should not have too many lines of code | CODE_SMELL | MAJOR | — |
| php:S1448 | Classes should not have too many methods | CODE_SMELL | MAJOR | — |
| php:S1479 | "switch" statements should not have too many "case" clauses | CODE_SMELL | MAJOR | — |
| php:S1481 | Unused local variables should be removed | CODE_SMELL | MINOR | — |
| php:S1488 | Local variables should not be declared and then immediately returned or thrown | CODE_SMELL | MINOR | — |
| php:S1523 | Dynamically executing code is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| php:S1599 | Variable variables should not be used | CODE_SMELL | BLOCKER | — |
| php:S1600 | Deprecated predefined variables should not be used | CODE_SMELL | MAJOR | — |
| php:S1603 | Deprecated constructor declarations should not be used | CODE_SMELL | MAJOR | — |
| php:S1605 | "__construct" functions should not make PHP 4-style calls to parent constructors | CODE_SMELL | MAJOR | — |
| php:S1607 | A reason should be provided when skipping a test | CODE_SMELL | MAJOR | — |
| php:S1656 | Variables should not be self-assigned | BUG | MAJOR | — |
| php:S1697 | Short-circuit logic should be used to prevent null pointer dereferences in conditionals | BUG | MAJOR | — |
| php:S1751 | Loops with at most one iteration should be refactored | BUG | MAJOR | — |
| php:S1757 | "&lt;?php" and "&lt;?=" tags should be used | CODE_SMELL | MINOR | — |
| php:S1763 | All code should be reachable | BUG | MAJOR | — |
| php:S1764 | Identical expressions should not be used on both sides of a binary operator | BUG | MAJOR | — |
| php:S1765 | The "var" keyword should not be used | CODE_SMELL | MINOR | — |
| php:S1766 | More than one property should not be declared per statement | CODE_SMELL | MINOR | — |
| php:S1780 | Closing tag "?&gt;" should be omitted on files containing only PHP | CODE_SMELL | MINOR | — |
| php:S1781 | PHP keywords and constants "true", "false", "null" should be lower case | CODE_SMELL | MINOR | — |
| php:S1784 | Method visibility should be explicitly declared | BUG | MINOR | — |
| php:S1788 | Method arguments with default values should be last | CODE_SMELL | MAJOR | — |
| php:S1793 | "elseif" keyword should be used in place of "else if" keywords | CODE_SMELL | MINOR | — |
| php:S1848 | Objects should not be created to be dropped immediately without being used | BUG | MAJOR | — |
| php:S1854 | Unused assignments should be removed | CODE_SMELL | MAJOR | — |
| php:S1862 | Related "if/else if" statements and "cases" in a "switch" should not have the same condition | BUG | MAJOR | — |
| php:S1871 | Two branches in a conditional structure should not have exactly the same implementation | CODE_SMELL | MAJOR | — |
| php:S1940 | Boolean checks should not be inverted | CODE_SMELL | MINOR | — |
| php:S1998 | References should not be passed to function calls | CODE_SMELL | CRITICAL | Core PHP |
| php:S2003 | "require_once" and "include_once" should be used instead of "require" and "include" | BUG | MINOR | — |
| php:S2004 | Functions should not be nested too deeply | CODE_SMELL | CRITICAL | — |
| php:S2010 | "&amp;&amp;" and "\|\|" should be used | CODE_SMELL | MINOR | — |
| php:S2014 | "$this" should not be used in a static context | BUG | BLOCKER | — |
| php:S2053 | Password hashing functions should use an unpredictable salt | VULNERABILITY | CRITICAL | Core PHP |
| php:S2068 | Hard-coded credentials are security-sensitive | SECURITY_HOTSPOT | BLOCKER | — |
| php:S2077 | Formatting SQL queries is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| php:S2092 | Creating cookies without the "secure" flag is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| php:S2115 | A secure password should be used when connecting to a database | VULNERABILITY | BLOCKER | Core PHP |
| php:S2123 | Values should not be uselessly incremented | BUG | MAJOR | — |
| php:S2166 | Classes named like "Exception" should extend "Exception" or a subclass | CODE_SMELL | MAJOR | — |
| php:S2187 | TestCases should contain tests | CODE_SMELL | BLOCKER | — |
| php:S2201 | Return values from functions without side effects should not be ignored | BUG | MAJOR | — |
| php:S2234 | Parameters should be passed in the correct order | CODE_SMELL | MAJOR | — |
| php:S2245 | Using pseudorandom number generators (PRNGs) is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| php:S2251 | A "for" loop update clause should move the counter in the right direction | BUG | MAJOR | — |
| php:S2612 | Setting loose POSIX file permissions is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| php:S2681 | Multiline blocks should be enclosed in curly braces | CODE_SMELL | MAJOR | — |
| php:S2699 | Tests should include assertions | CODE_SMELL | BLOCKER | — |
| php:S2737 | "catch" clauses should do more than rethrow | CODE_SMELL | MINOR | — |
| php:S2755 | XML parsers should not be vulnerable to XXE attacks | VULNERABILITY | BLOCKER | Core PHP |
| php:S2757 | Non-existent operators like "=+" should not be used | BUG | MAJOR | — |
| php:S2761 | Unary prefix operators should not be repeated | BUG | MAJOR | — |
| php:S3011 | Reflection should not be used to increase accessibility of classes, methods, or fields | CODE_SMELL | MAJOR | — |
| php:S3330 | Creating cookies without the "HttpOnly" flag is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| php:S3358 | Ternary operators should not be nested | CODE_SMELL | MAJOR | — |
| php:S3360 | Test class names should end with "Test" | CODE_SMELL | BLOCKER | — |
| php:S3415 | Assertion arguments should be passed in the correct order | CODE_SMELL | MAJOR | — |
| php:S3626 | Jump statements should not be redundant | CODE_SMELL | MINOR | — |
| php:S3699 | The output of functions that don't return anything should not be used | BUG | MAJOR | — |
| php:S3776 | Cognitive Complexity of functions should not be too high | CODE_SMELL | CRITICAL | — |
| php:S3801 | Functions should use "return" consistently | CODE_SMELL | MAJOR | — |
| php:S3923 | All branches in a conditional structure should not have exactly the same implementation | BUG | MAJOR | — |
| php:S3972 | Conditionals should start on new lines | CODE_SMELL | CRITICAL | — |
| php:S3973 | A conditionally executed single line should be denoted by indentation | CODE_SMELL | CRITICAL | — |
| php:S3981 | Array or Countable object count comparisons should make sense | BUG | MAJOR | — |
| php:S3984 | Exceptions should not be created without being thrown | BUG | MAJOR | — |
| php:S4143 | Array values should not be replaced unconditionally | BUG | MAJOR | — |
| php:S4144 | Methods should not have identical implementations | CODE_SMELL | MAJOR | — |
| php:S4423 | Weak SSL/TLS protocols should not be used | VULNERABILITY | CRITICAL | Core PHP |
| php:S4426 | Cryptographic keys should be robust | VULNERABILITY | CRITICAL | Core PHP |
| php:S4433 | LDAP connections should be authenticated | VULNERABILITY | CRITICAL | — |
| php:S4502 | Disabling CSRF protections is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| php:S4507 | Delivering code in production with debug features activated is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| php:S4524 | "default" clauses should be first or last | CODE_SMELL | CRITICAL | — |
| php:S4790 | Using weak hashing algorithms is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| php:S4824 | References used in "foreach" loops should be "unset" | BUG | CRITICAL | Core PHP |
| php:S4828 | Signaling processes is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| php:S4830 | Server certificates should be verified during SSL/TLS connections | VULNERABILITY | CRITICAL | cURL |
| php:S4833 | Use of namespaces should be preferred to "include" or "require" functions | CODE_SMELL | MAJOR | — |
| php:S5042 | Expanding archive files without controlling resource consumption is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| php:S5122 | Having a permissive Cross-Origin Resource Sharing policy is security-sensitive | SECURITY_HOTSPOT | MINOR | — |
| php:S5328 | Manual generation of session ID is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| php:S5332 | Using clear-text protocols is security-sensitive | SECURITY_HOTSPOT | CRITICAL | — |
| php:S5361 | `str_replace` should be preferred to `preg_replace` | CODE_SMELL | CRITICAL | — |
| php:S5527 | Server hostnames should be verified during SSL/TLS connections | VULNERABILITY | CRITICAL | cURL |
| php:S5542 | Encryption algorithms should be used with secure mode and padding scheme | VULNERABILITY | CRITICAL | OpenSSL, Mcrypt |
| php:S5547 | Cipher algorithms should be robust | VULNERABILITY | CRITICAL | Mcrypt, OpenSSL |
| php:S5632 | Raised Exceptions must derive from Throwable | BUG | BLOCKER | — |
| php:S5693 | Allowing requests with excessive content length is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| php:S5708 | Caught Exceptions must derive from Throwable | BUG | BLOCKER | — |
| php:S5713 | A subclass should not be in the same "catch" clause as a parent class | CODE_SMELL | MINOR | — |
| php:S5779 | Assertion failure exceptions should not be ignored | BUG | CRITICAL | — |
| php:S5785 | PHPUnit assertTrue/assertFalse should be simplified to the corresponding dedicated assertion | CODE_SMELL | MAJOR | — |
| php:S5797 | Constants should not be used as conditions | CODE_SMELL | CRITICAL | — |
| php:S5808 | Authorizations should be based on strong decisions | VULNERABILITY | MAJOR | Symfony, Laravel |
| php:S5842 | Repeated patterns in regular expressions should not match the empty string | BUG | MINOR | — |
| php:S5843 | Regular expressions should not be too complicated | CODE_SMELL | MAJOR | — |
| php:S5850 | Alternatives in regular expressions should be grouped when used with anchors | BUG | MAJOR | — |
| php:S5855 | Regex alternatives should not be redundant | BUG | MAJOR | — |
| php:S5857 | Character classes should be preferred over reluctant quantifiers in regular expressions | CODE_SMELL | MINOR | — |
| php:S5863 | Assertions should not compare an object to itself | BUG | MAJOR | — |
| php:S5868 | Unicode Grapheme Clusters should be avoided inside regex character classes | BUG | MAJOR | — |
| php:S5869 | Character classes in regular expressions should not contain the same character twice | CODE_SMELL | MAJOR | — |
| php:S5876 | A new session should be created during user authentication | VULNERABILITY | CRITICAL | — |
| php:S5911 | Class of caught exception should be defined | BUG | BLOCKER | Core PHP |
| php:S5994 | Regex patterns following a possessive quantifier should not always fail | BUG | CRITICAL | — |
| php:S5996 | Regex boundaries should not be used in a way that can never be matched | BUG | CRITICAL | — |
| php:S6001 | Back references in regular expressions should only refer to capturing groups that are matched before the reference | BUG | CRITICAL | — |
| php:S6002 | Regex lookahead assertions should not be contradictory | BUG | CRITICAL | — |
| php:S6019 | Reluctant quantifiers in regular expressions should be followed by an expression that can't match the empty string | CODE_SMELL | MAJOR | — |
| php:S6035 | Single-character alternations in regular expressions should be replaced with character classes | CODE_SMELL | MAJOR | — |
| php:S6323 | Alternation in regular expressions should not contain empty alternatives | BUG | MAJOR | — |
| php:S6326 | Regular expressions should not contain multiple spaces | CODE_SMELL | MAJOR | — |
| php:S6328 | Replacement strings should reference existing regular expression groups | BUG | MAJOR | — |
| php:S6331 | Regular expressions should not contain empty groups | CODE_SMELL | MAJOR | — |
| php:S6341 | WordPress theme and plugin editors are security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| php:S6343 | Disabling automatic updates is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| php:S6344 | Constants should not be redefined | CODE_SMELL | MAJOR | — |
| php:S6345 | Allowing all external requests from a WordPress server is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| php:S6346 | Allowing unauthenticated database repair in WordPress is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| php:S6347 | WordPress options should not be defined at the end of "wp-config.php" | CODE_SMELL | MAJOR | WordPress |
| php:S6348 | Allowing unfiltered HTML content in WordPress is security-sensitive | SECURITY_HOTSPOT | MAJOR | — |
| php:S6349 | WordPress option names should not be misspelled | CODE_SMELL | MAJOR | WordPress |
| php:S6353 | Regular expression quantifiers and character classes should be used concisely | CODE_SMELL | MINOR | — |
| php:S6393 | Regular expressions should have valid delimiters | BUG | CRITICAL | Core PHP |
| php:S6395 | Non-capturing groups without quantifier should not be used | CODE_SMELL | MAJOR | — |
| php:S6396 | Superfluous curly brace quantifiers should be avoided | CODE_SMELL | MAJOR | — |
| php:S6397 | Character classes in regular expressions should not contain only one character | CODE_SMELL | MAJOR | — |
| php:S6418 | Hard-coded secrets are security-sensitive | SECURITY_HOTSPOT | BLOCKER | — |
| php:S6437 | Credentials should not be hard-coded | VULNERABILITY | BLOCKER | — |
| php:S6600 | Unnecessary parentheses should not be used for constructs | CODE_SMELL | CRITICAL | — |
| php:S836 | Variables should be initialized before use | BUG | MAJOR | — |
| php:S905 | Non-empty statements should change control flow or have at least one side-effect | BUG | MAJOR | — |
| php:S907 | "goto" statement should not be used | CODE_SMELL | MAJOR | — |
| php:S930 | The number of arguments passed to a function should match the number of parameters | BUG | MAJOR | — |
