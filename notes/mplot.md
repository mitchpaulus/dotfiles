`default.png.do`

```sh
#!/bin/sh
set -e
mplot -d "$2".mplot | tr '\n' '\0' | xargs -0 redo-ifchange "$2".mplot
mplot "$2".mplot | gnuplot -
```

```mshell
#!/usr/bin/env mshell
soe
$"{$2}.mplot" file!
[redo-ifchange @file [mplot -d @file]o;];
[ [mplot @file] [gnuplot '-'] ] | ;
```

```mplot
f sarg1 sarg2
ignore $x 2 <
stdin // Read from stdin
w 10-1/2 // Width in inches
top above right upperright upperleft bottomright bottomleft aboveright // legend positions

x 3 #3
```
