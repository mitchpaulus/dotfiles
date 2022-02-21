# awk

```awk
gsub(regex, substitution, [text=$0]) = num substitutions
substr(string, start-pos-1-based, [numChars])
split(string, array, [fieldsep], [seps]) = Num Elements
match(string, regex) = 1-based Start Index # Also sets RSTART/RLENGTH
```

## `printf`

```
%[N$][-][ ][+][#][0]['][width][.prec][(a|A)|c|(d|i)|e|f|F|g|G|o|s||u|x]
```

```
aA: some crazy floating number format
c: number as character -> 65 -> 'A'
d,i: decimal integer
eE: scientific
fF: Floating point
gG: Shorter of scientific or floating
```

## AWKPATH (gawk)

Can use `AWKPATH` environment variable to easily specify files on the
command line. This can be used to easily load library's of functions.

Default value is `.:/usr/local/share/awk`

Use like:
```awk
@include "file.awk"
```

## Time

```awk
mktime("YYYY MM DD HH MM SS [DST]", [utc-flag]) # Returns Unix time, seconds since 1970
strftime("format", [unix_timestamp], [utc-flag]) # Return formatted time
systime() # Return current Unix time
```

To split on whitespace runs, use `FS=" "`

## Regular Expression Meta Characters

```
\ ^ $ .  [ ] | ( ) * ?
```

## Sorting

```awk
asort(source, dest, how) # Sort by values
asorti(source, dest, how) # Sort by indices
```

## Command line arguments

```awk
# awk -f file.awk 1 2 3
ARGC = 4
Arg 0: 'awk'
Arg 1: '1'
Arg 2: '2'
Arg 3: '3'

# Remove argument as file to process, set to ""
ARGV[1] = ""
```

Set `ARGV[i]` to `''` to remove as a file name.
