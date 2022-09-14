# Vim Colorschemes

- `:h :colorscheme`

- In directory `colors/{name}.(vim|lua)`.
- See `$VIMRUNTIME/colors/README.txt`

- `:highlight` to find out current colors.

- Source the `$VIMRUNTIME/tools/check_colors.vim` script to check for common mistakes.

- Often will want to use the option `set termguicolors` for newer terminals.

## `highlight` command

```
cterm=<attr-list>
attr-list=attr[,attr]*
attr=bold | underline | undercurl | strikethrough | reverse | inverse | italic | standout | nocombine | NONE

ctermfg=<color-nr>
color-nr = <digit> | <color-name>
digit = '0' .. '16'
color-name = See table below

guifg=<color>
color=#rrggbb
```

NR-16   NR-8    COLOR NAME
0	      0	      Black
1	      4	      DarkBlue
2	      2	      DarkGreen
3	      6	      DarkCyan
4	      1	      DarkRed
5	      5	      DarkMagenta
6	      3	      Brown, DarkYellow
7	      7	      LightGray, LightGrey, Gray, Grey
8	      0\*	    DarkGray, DarkGrey
9	      4\*	    Blue, LightBlue
10	    2\*	    Green, LightGreen
11	    6\*	    Cyan, LightCyan
12	    1\*	    Red, LightRed
13	    5\*	    Magenta, LightMagenta
14	    3\*	    Yellow, LightYellow
15	    7\*	    White
