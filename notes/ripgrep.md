# `ripgrep`

```man
USAGE:
    rg [OPTIONS] PATTERN [PATH ...]
    rg [OPTIONS] [-e PATTERN ...] [-f PATTERNFILE ...] [PATH ...]
    rg [OPTIONS] --files [PATH ...]
    rg [OPTIONS] --type-list
    command | rg [OPTIONS] PATTERN

-I, --no-filename
--no-heading
-N                   suppress line numbers
-i, --ignore-case
-v, --invert-match
-A, --after-context <NUM>
-o, --only-matching
-l, --files-with-matches
--no-ignore : Remove .gitignore logic
--hidden: Search hidden directories
-uu: Normally the option to use when searching everywhere.
```

## Patterns

Uses Rust regex. https://docs.rs/regex/1.5.4/regex/#syntax

Most meta constructs do not have escaping: e.g. '(' for grouping, '+' for 1 or more.
