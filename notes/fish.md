# Fish

Set environment variable for one command. Use `env`.

```fish
env VAR=value command
```

## Lists

- 1-based
- `set -a VARIABLE_NAME VALUES...` to append. `-p` to prepend.

## Command Substitution

- Be careful with setting multiline text output to a variable. By
  default, the newlines are replaced with a single space. Use the
  following instead:

```
begin; set -l IFS; set data (cat data.txt); end
```
