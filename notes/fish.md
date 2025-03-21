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

- <https://fishshell.com/docs/current/completions.html>
- <https://fishshell.com/docs/current/cmds/complete.html>

```fish
# Completing option argument. Note that command substitution needs to be wrapped in quotations.

complete -c command -x -a "(command)"

# Completing files with known extensions
From https://github.com/fish-shell/fish-shell/blob/master/share/completions/tex.fish
complete -c tex -k -x -a "(__fish_complete_suffix --description='(La)TeX file' .tex)"

# Wrapping a existing command
complete -c command -w existing_command
```

## `set -e` equivalent

There isn't one. [GitHub Issue](https://github.com/fish-shell/fish-shell/issues/510)

## Iteration

```fish
set i 0
set i (math $i + 1)
```

[Variable expansion](https://fishshell.com/docs/current/language.html#variable-expansion)

## Associative Arrays

From <https://stackoverflow.com/a/40019138/5932184>. Store keys in one array, values in the other.

```fish
if set -l index (contains -i -- foo $keys) # `set` won't modify $status, so this succeeds if `contains` succeeds
    echo $values[$index]
end
```
