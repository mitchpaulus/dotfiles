# `asciinema`

`asciinema` is fabulous program for recording terminal sessions.

## Important Options

Recording:

 - `-c COMMAND`: specify a particular command, rather than `$SHELL`.
 - `-i IDLE_TIME`: specify the maximum idle time in seconds.
 - `--overwrite`: overwrite file if exists
 - `-t TITLE`: set title

On Playback:

 - theme
    - asciinema
    - tango
    - solarized-dark
    - solarized-light
    - monokai
 - cols: number of columns in terminal
 - rows: number of rows in the terminal
 - size: font size, small, medium, or big
 - t: playback start time, either `ss`, `mm:ss`, or `hh:mm:ss`.

