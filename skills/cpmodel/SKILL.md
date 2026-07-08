---
name: cpmodel
description: |
  cpmodel is a skill for creating linear change point models that are often used in the the monitoring and verification of whole building energy use.
  It is a CLI tool that aids in completing the required regressions.
---

`cpmodel` is a CLI tool for linear change point model regressions.

Get current usage from the help output: `cpmodel --help`.

Example usage:

```
cpmodel -p 5 --skip 1 --x-col 2 --y-col 4 --json myfile.tsv
```
