# Bash/Sh

- `"$@"` is all the input variables, properly quoted.
- `"$*"` == `"$1c$2c"`

## Set built in

- Stop execution on error 'set -e'

- `-x`: Print a trace of simple commands, for commands, case commands,
  select commands, and arithmetic for commands and their arguments or
  associated word lists after they are expanded and before they are
  executed. The value of the PS4 variable is expanded and the resultant
  value is printed before the command and its expanded arguments.
