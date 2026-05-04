---
name: cpmodel
description: |
  cpmodel is a skill for creating linear change point models that are often used in the the monitoring and verification of whole building energy use.
  It is a CLI tool that aids in completing the required regressions.
---

`cpmodel` is a CLI tool for linear change point model regressions.

It's usage is like:

```
cpmodel

USAGE:
cpmodel <options>... <file>

OPTIONS

 -c                       Print model coordinates, not coefficients
 -d, --delimeter <delim>  Delimiter to split lines by [whitespace]
 --json                   Print outputs in JSON format
 -p <model type>          Model type: 2p, 3h, 3c, 3h_new, 3c_new, 4, 5 [4]
 --skip n                 Skip n header records [0]
 --x-col <int col>        Set X column number, 1-based integer [1]
 --y-col <int col>        Set Y column number, 1-based integer [2]
 -h, --help               Show this help message and exit

It is assumed that the first column is X and the second column is Y.
The default delimiter is whitespace.
The file can be '-' to read from standard input.
```

Example usage:

```
cpmodel -p 5 --skip 1 --x-col 2 --y-col 4 --json myfile.tsv
```
