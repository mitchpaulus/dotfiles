# Shell

## Finding the current directory of running script

If `readlink` is available (on all my systems it typically is), can use
solution from: [https://stackoverflow.com/a/1638397/5932184](https://stackoverflow.com/a/1638397/5932184).

Solution is:

```sh
#!/bin/sh
# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH
```

Although this post from the bash FAQ is pretty convincing that this is
still a bit of a hack and isn't necessarily the best way to go about
things. [link](https://mywiki.wooledge.org/BashFAQ/028)

## Case Statement

Can never remember the syntax for case statements.

```
case word in
    pattern [| pattern]... ) command-list ;;
esac
```

## Basename/Dirname

- `basename` removes directory portions
- `dirname` removes file, leaving directory

## Grep in if statement

```sh
if printf '%s' $var | grep -q 'pattern'; then ... ; fi
```


## Writing your own shell

[Cool link](https://www.cs.cornell.edu/courses/cs414/2004su/homework/shell/shell.html)

## Pass variable contents to standard input

This is POSIX compatible as well.

```
printf '%s' "$var" | program
```
