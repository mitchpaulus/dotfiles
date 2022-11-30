# Fish

Set environment variable for one command. Use `env`.

```fish
env VAR=value command
```

## Lists

- 1-based
- `set -a VARIABLE_NAME VALUES...` to append. `-p` to prepend.
- Can get length using `count` built-in

## Command Substitution

- Be careful with setting multiline text output to a variable. By
  default, the newlines are replaced with a single space. Use the
  following instead:

```
begin; set -l IFS; set data (cat data.txt); end
```

## Strings

Substring: `string sub -s start -e end -l length <string>`
1-index based, can use negative values as well.

Length: `string length <string>`

## Process Substitution

```fish
sort (command | psub) (command2 | psub)
```

## History

`fish` doesn't provide any history settings - it stores up to 256k
*unique* history items. [See GitHub Issue #2674](https://github.com/fish-shell/fish-shell/issues/2674)

## Check for arguments

From [Stack](https://stackoverflow.com/a/29643375/5932184)

```fish
if count $argv > /dev/null
```

## Events

Can bind functions to events like:

```fish
function myfunc --on-event fish_prompt
```

can list functions using: `function --help`

[When an alias should actually be an abbr](https://www.sean.sh/log/when-an-alias-should-actually-be-an-abbr/)


## Key Bindings

Emacs bindings are default, or execute command `fish_default_key_bindings` to go back
For default vim bindings, execute command `fish_vi_key_bindings`.

Useful command line functions:

- down-or-search/up-or-search, typically bound to \cn and \cp

## Completions

```
# Completing option argument. Note that command substitution needs to be wrapped in quotations.

complete -c command -x -a "(command)"
```
