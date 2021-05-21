# Terminals

- Keystrokes with the control key are often indistinguishable from keys
  without to the terminal. For example, CTRL-I sends *exactly* the same
  bits to the terminal as tab.

Here's a table of escape sequences for various keys. From [here](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html)

Generally see the items in the 'Numeric' column. Example in alacritty:

Right Arrow sends 1B (esc) - 5B ('[' which is CSI) - 43 ('C')

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


