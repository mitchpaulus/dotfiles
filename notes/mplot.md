`default.png.do`

```sh
#!/bin/sh
set -e
mplot -d "$2".mplot | tr '\n' '\0' | xargs -0 redo-ifchange "$2".mplot
mplot "$2".mplot | gnuplot -
```

```mplot
f sarg1 sarg2
ignore $x 2 <
stdin // Read from stdin
w 10-1/2 // Width in inches
```
