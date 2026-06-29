---
name: redo
description: 'redo is a build system, a competitor to make. It relies on simple script files, written in any language.'
---

`redo` is a build system that is extremely powerful, yet simple.
There are many different implementations of the basic idea, similar to `make`.
The original idea can be found at <https://cr.yp.to/redo.html>.

Build targets are set by `.do` files that define how the target is made. It can be any interpreted script.

In the Apenwarr implementation, which only works on Unix-like systems, a shebang can be set.

The key commands are:

```
redo
redo-ifchange
redo-always
```
