CPR = Cursor position report

Request: CSI 6 n
Response: CSI <1-based LINE> : <1 based COL> R

Terminals typically are:

- Unicode code point based
- Extended grapheme cluster based

Impossible to enumerate all possible grapheme clusters, some constructions are recursive.


https://www.jeffquast.com/post/perfecting-terminal-character-width-using-correction-tables/
https://bugzilla.gnome.org/show_bug.cgi?id=767529#c12
https://lists.nongnu.org/archive/html/bug-gnu-emacs/2025-06/msg01637.html
https://mitchellh.com/writing/grapheme-clusters-in-terminals

https://github.com/kovidgoyal/kitty/issues/8226
https://github.com/ghostty-org/ghostty/discussions/5563
https://github.com/jquast/wcwidth/issues/104

https://www.jeffquast.com/post/terminal_wcwidth_solution/

https://thottingal.in/blog/2026/03/22/complex-scripts-in-terminal/
https://www.unicode.org/L2/L2023/23107-terminal-suppt.pdf
https://www.unicode.org/L2/L2025/25179-ttwg.pdf
https://github.com/ratatui/ratatui/discussions/1438
https://github.com/charmbracelet/lipgloss/releases/tag/v2.0.6
