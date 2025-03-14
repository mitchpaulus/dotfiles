# Terminals

Keystrokes with the control key are often indistinguishable from keys without to the terminal.
For example, CTRL-I sends *exactly* the same bits to the terminal as tab.

Here's a table of escape sequences for various keys. From [here](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html)

Generally see the items in the 'Numeric' column. Example in alacritty:

Right Arrow sends 1B (esc) - 5B ('[' which is CSI) - 43 ('C')

```
Key              Numeric    Application   Terminfo   Termcap
---------------+----------+-------------+----------+----------
Space          | SP       | SS3 SP      | -        | -
Tab            | TAB      | SS3 I       | -        | -
Enter          | CR       | SS3 M       | kent     | @8
PF1            | SS3 P    | SS3 P       | kf1      | k1
PF2            | SS3 Q    | SS3 Q       | kf2      | k2
PF3            | SS3 R    | SS3 R       | kf3      | k3
PF4            | SS3 S    | SS3 S       | kf4      | k4
* (multiply)   | *        | SS3 j       | -        | -
+ (add)        | +        | SS3 k       | -        | -
, (comma)      | ,        | SS3 l       | -        | -
- (minus)      | -        | SS3 m       | -        | -
. (Delete)     | .        | CSI 3 ~     | -        | -
/ (divide)     | /        | SS3 o       | -        | -
0 (Insert)     | 0        | CSI 2 ~     | -        | -
1 (End)        | 1        | SS3 F       | kc1      | K4
2 (DownArrow)  | 2        | CSI B       | -        | -
3 (PageDown)   | 3        | CSI 6 ~     | kc3      | K5
4 (LeftArrow)  | 4        | CSI D       | -        | -
5 (Begin)      | 5        | CSI E       | kb2      | K2
6 (RightArrow) | 6        | CSI C       | -        | -
7 (Home)       | 7        | SS3 H       | ka1      | K1
8 (UpArrow)    | 8        | CSI A       | -        | -
9 (PageUp)     | 9        | CSI 5 ~     | ka3      | K3
= (equal)      | =        | SS3 X       | -        | -
---------------+----------+-------------+----------+----------
```

- <https://terminalguide.namepad.de/>

[Escape codes](https://github.com/dylanaraps/pure-bash-bible#escape-sequences)


## Text Colors

**NOTE:** Sequences requiring RGB values only work in True-Color Terminal Emulators.

| Sequence               | What does it do?                        | Value         |
| --------               | ----------------                        | -----         |
| `\e[38;5;<NUM>m`       | Set text foreground color.              | `0-255`       |
| `\e[48;5;<NUM>m`       | Set text background color.              | `0-255`       |
| `\e[38;2;<R>;<G>;<B>m` | Set text foreground color to RGB color. | `R`, `G`, `B` |
| `\e[48;2;<R>;<G>;<B>m` | Set text background color to RGB color. | `R`, `G`, `B` |

Base 16 colors:

```
\e[<attribute>;<fg/bg>m

Black 30 90 40 100
Red 31 91 41 101
Green 32 92 42 102
Yellow 33 93 43 103
Blue 34 94 44 104
Magenta 35 95 45 105
Cyan 36 96 46 106
White 37 97 47 107
```





## Text Attributes

**NOTE:** Prepend 2 to any code below to turn it's effect off
(examples: 21=bold text off, 22=faint text off, 23=italic text off).

| Sequence | What does it do?                  |
| -------- | ----------------                  |
| `\e[m`   | Reset text formatting and colors. |
| `\e[1m`  | Bold text.                        |
| `\e[2m`  | Faint text.                       |
| `\e[3m`  | Italic text.                      |
| `\e[4m`  | Underline text.                   |
| `\e[5m`  | Blinking text.                    |
| `\e[7m`  | Highlighted text.                 |
| `\e[8m`  | Hidden text.                      |
| `\e[9m`  | Strike-through text.              |


## Cursor Movement

| Sequence              | What does it do?                      | Value            |
| --------              | ----------------                      | -----            |
| `\e[<LINE>;<COLUMN>H` | Move cursor to absolute position.     | `line`, `column`
| `\e[H`                | Move cursor to home position (`0,0`). |
| `\e[<NUM>A`           | Move cursor up N lines.               | `num`
| `\e[<NUM>B`           | Move cursor down N lines.             | `num`
| `\e[<NUM>C`           | Move cursor right N columns.          | `num`
| `\e[<NUM>D`           | Move cursor left N columns.           | `num`
| `\e[s`                | Save cursor position.                 |
| `\e[u`                | Restore cursor position.              |
| `\e[<NUM>G`            | Move cursor to column N (1-based).              | `num`


## Erasing Text

| Sequence    | What does it do?                                         |
| --------    | ----------------                                         |
| `\e[K`      | Erase from cursor position to end of line.               |
| `\e[1K`     | Erase from cursor position to start of line.             |
| `\e[2K`     | Erase the entire current line.                           |
| `\e[J`      | Erase from the current line to the bottom of the screen. |
| `\e[1J`     | Erase from the current line to the top of the screen.    |
| `\e[2J`     | Clear the screen.                                        |
| `\e[2J\e[H` | Clear the screen and move cursor to `0,0`.               |


## Cursor shape

[Source](https://superuser.com/a/607479/685547)

```sh
echo -e -n "\x1b[\x30 q" # changes to blinking block
echo -e -n "\x1b[\x31 q" # changes to blinking block also
echo -e -n "\x1b[\x32 q" # changes to steady block
echo -e -n "\x1b[\x33 q" # changes to blinking underline
echo -e -n "\x1b[\x34 q" # changes to steady underline
echo -e -n "\x1b[\x35 q" # changes to blinking bar
echo -e -n "\x1b[\x36 q" # changes to steady bar
```

### Issue with Neovim

See:
  - <https://github.com/neovim/neovim/issues/4867#issuecomment-291249173>
  - <https://github.com/neovim/neovim/issues/12283>
  - <https://github.com/neovim/neovim/issues/6779>
  - <https://github.com/neovim/neovim/issues/4396>
  - <https://github.com/neovim/neovim/wiki/FAQ#cursor-style-isnt-restored-after-exiting-or-suspending-and-resuming-nvim>

### Showing/Hiding Cursor

<https://stackoverflow.com/questions/2649733/hide-cursor-on-remote-terminal>

```
\e[?25h   // Show cursor
\e[?25l   // Hide cursor
```

<https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#writing-a-command-line>

### OSCs

```
printf '\033]8;;http://example.com\033\\This is a link\033]8;;\033\\\n'

```

Set progress status
```
ESC ] 9 ; 4 ; [0 thru 4] ; [0-100] ST
```

`ST` is usually either bell ('\a') or escape followed by a backslash ('\033\\').

## CSI u

- ghostty has by default

## References

- [ASCII control characters in my terminal](https://jvns.ca/blog/2024/10/31/ascii-control-characters/)
- [Keyboard handling from kitty](https://sw.kovidgoyal.net/kitty/keyboard-protocol/)
- `:h tui-modifyOtherKeys` in Neovim help
- [CSI u spec?](https://www.leonerd.org.uk/hacks/fixterms/)
- [The VT100 manual](https://vt100.net/docs/vt100-ug/chapter1.html)
- [Terminal Frustrations](https://jvns.ca/blog/2025/02/05/some-terminal-frustrations/)
- [The TTY demystified](https://www.linusakesson.net/programming/tty/)
- [Terminfo rant](https://twoot.site/@bean/113056942625234032)

- Man page for `termios`
