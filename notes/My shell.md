If I were to make a shell-like scripting language, it would need:

- Pipelines
- Redirection
- Variables
- Many built in string manipulation functions, path manipulation
- Dictionaries, associative arrays, probably awk-style, needing no instantiation. Lists, but do it like lua where everything is technically a list/dict?
- Normal looping constructs
- Basic math (increments, etc.)
- Functions/Macros
- Some level of type safety?
- Globbing?

I'm not targeting CLI use, this is for short scripts (think 10-50 LOC)

Concatenative? Lisp like?

A command is literally a list data structure of strings, then executed, or pipelined?

Also see [cosh](https://github.com/tomhrr/cosh/blob/main/doc/all.md)

```
[ command1 ]  [ command2 ] |
[ command3 ] .

[ command ] "New path" < "output" > .

[ ls -al ] .

# Variable loading

x 1 store

[ 1 ] 2 append

```
