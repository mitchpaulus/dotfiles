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
