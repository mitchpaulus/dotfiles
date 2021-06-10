# awk

```awk
gsub(regex, substitution, [text=$0]) = num substitutions
substr(string, start-pos-1-based, [numChars])
split(string, array, [fieldsep], [seps]) = Num Elements
```

## `printf`

```
%[N$][-][ ][+][#][0]['][width][.prec][a||c|d|e|f|F|g|G|o|s||u|x]
```

## AWKPATH (gawk)

Can use `AWKPATH` environment variable to easily specify files on the
command line. This can be used to easily load library's of functions.

Default value is `.:/usr/local/share/awk`

Use like:
```awk
@include "file.awk"
```

