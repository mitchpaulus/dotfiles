# CMD.EXE

- Reference: `%variable%`
    - Helpful built in variables:
        - `%date%`, uses current time/date settings from computer, so
          not portable, still useful.
        - `%time%` same comments as `%date%`
- String Variable manipulation
    - `%VarName:~ZeroBasedPosition,Count%` - Can use negative value in
      the position.
    - `%~1` - Expands `%1` and removes any surrounding quotation marks
      ("")
    - `%~f1` - Expands `%1` to a fully qualified path name.
    - `%~d1` - Expands `%1` to a drive letter.
    - `%~p1` - Expands `%1` to a path.
    - `%~n1` - Expands `%1` to a file name.
    - `%~x1` - Expands `%1` to a file extension.
    - `%~s1` - Expands `%1` to a file extension.
    - `%~a1` - Expands `%1` to file attributes.
    - `%~t1` - Expands `%1` to date and time of file.
    - `%~z1` - Expands `%1` to size of the file.

- Shutdown/Restart
    - `shutdown /s`: Shutdown
    -  `shutdown /r`: Restart
