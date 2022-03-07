# KDE Syntax Highlighting

[link](https://docs.kde.org/stable5/en/kate/katepart/highlight.html)

Root element: `language`
Required Attributes
    - name
    - section
    - extensions="\*.ext",
    - version
    - kateversion="2.4"

Optional Attributes
    - author

Then `highlighting` element, with required elements `contexts` and
`itemdatas`. Optional `list` elements.

## Contexts

### Attributes

- name
- lineEndContext
- lineEmptyContext (default: '#stay')
- fallthroughtContext (default: '#stay')
- noIndentationBasedFolding (default: false)

## Detection Rules

2 required XML attributes:

1. `attribute` - maps to item defined in `itemData`. Sets the style.
2. `context` - sets the context to use.


## Other Notes

1. First context is used by default to start.

## KDE Regex

[link](https://docs.kde.org/stable5/en/kate/katepart/regular-expressions.html)


## Available Default Styles

###  General default styles:

- dsNormal, when no special highlighting is required.
- dsKeyword, built-in language keywords.
- dsFunction, function calls and definitions.
- dsVariable, if applicable: variable names (e.g. $someVar in PHP/Perl).
- dsControlFlow, control flow keywords like if, else, switch, break, return, yield, ...
- dsOperator, operators like + - * / :: < >
- dsBuiltIn, built-in functions, classes, and objects.
- dsExtension, common extensions, such as Qt™ classes and functions/macros in C++ and Python.
- dsPreprocessor, preprocessor statements or macro definitions.
- dsAttribute, annotations such as @override and \_\_declspec(...).

### String-related default styles:

- dsChar, single characters, such as 'x'.
- dsSpecialChar, chars with special meaning in strings such as escapes, substitutions, or regex operators.
- dsString, strings like "hello world".
- dsVerbatimString, verbatim or raw strings like 'raw \backlash' in Perl, CoffeeScript, and shells, as well as r'\raw' in Python.
- dsSpecialString, SQL, regexes, HERE docs, LATEX math mode, ...
- dsImport, import, include, require of modules.

### Number-related default styles:

- dsDataType, built-in data types like int, void, u64.
- dsDecVal, decimal values.
- dsBaseN, values with a base other than 10.
- dsFloat, floating point values.
- dsConstant, built-in and user defined constants like PI.

Comment and documentation-related default styles:

- dsComment, comments.
- dsDocumentation, /\*\* Documentation comments \*/ or """docstrings""".
- dsAnnotation, documentation commands like @param, @brief.
- dsCommentVar, the variable names used in above commands, like "foobar" in @param foobar.
- dsRegionMarker, region markers like //BEGIN, //END in comments.

Other default styles:

- dsInformation, notes and tips like @note in doxygen.
- dsWarning, warnings like @warning in doxygen.
- dsAlert, special words like TODO, FIXME, XXXX.
- dsError, error highlighting and wrong syntax.
- dsOthers, when nothing else fits.

## Validation

There is a validation script that is part of the
<https://invent.kde.org/frameworks/syntax-highlighting.git> repository.
[This is the GitHub mirror](https://github.com/KDE/syntax-highlighting)

Script is on path: `data/schema/validatehl.sh`
