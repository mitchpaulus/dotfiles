# Taskwarrior

`task <filter> command <mods>`
`task <filter> annotate <mods>`
`task <filter> modify <mods>`

## Common Mods

`priority:<H|M|L|>`
`project:<text>`
`due:<due-date>`

## Search with regular expressions

`task /regex/ list`

## Files

 - `~/.taskrc` or `TASKRC` environment variable, configuration
 - '~/.task' or `TASKDATA` environment variable, data directory
     - ~/.task/pending.data, not finished tasks
     - ~/.task/completed.data, done tasks
     - ~/.task/undo.data, data for undoing things

## Annoying header on TASKRC override

See <https://github.com/GothenburgBitFactory/taskwarrior/issues/442>. Should be fixed in 2.6.
See <https://unix.stackexchange.com/questions/367151/how-to-override-warning-in-taskwarrior>
