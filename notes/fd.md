# fd

Find all results: `fd -H -I`. -H for hidden, -I for ignored. Smart Case
by default.

```
{} path
{/} basename (aka filename)
{//} parent directory
{.} path without file extension
{/.} basename without file extension
```

```sh
-d, --max-depth <depth>
-t, --type <type>  f, d, l, x, e (empty)
-x, --exec <cmd>

# Example of printing filename only
fd 'pattern' -x printf '%s\n' '{/}'

# With dir
fd [FLAGS/OPTIONS] [<pattern>] [<path>...]
```
