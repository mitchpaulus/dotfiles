# Indentation in Vim

[Amazing blog
post](https://vimways.org/2019/indentation-without-dents/).

There are several slightly overlapping indentation settings in Vim

1. 'autoindent' - default on
2. 'smartindent' - default off
3. 'cindent' - default off
4. 'indentexpr' - default "" (empty string)
5. 'lisp' - default off

Other useful Vim functions:

1. `indent(lineNum)` - Returns the indentation in number of spaces.
2. `shiftwidth()`

Can view built in indentation scripts in `runtime/indent/` directory in
the source code.


