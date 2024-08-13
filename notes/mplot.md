`default.png.do`

```sh
#!/bin/sh
set -e
mplot -d "$2".mplot | tr '\n' '\0' | xargs -0 redo-ifchange "$2".mplot
mplot "$2".mplot | gnuplot -
```
