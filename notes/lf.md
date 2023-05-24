# `lf`

<https://pkg.go.dev/github.com/gokcehan/lf>

Multiple commands for mapping, need to follow instructions from this line in the help:

> An explicit ':' can be provided to group statements until a newline which is especially useful for 'map' and 'cmd' commands:

Example:

```
map J down; down; down
```

doesn't work.

```
map J :down; down; down
```

does work.

Although the better way to map the example above is to use a "push"
modifier.

```
map J push 5j
```


## Variables

```
f Current file selection as full path
fs Selected files with `filesep`, full paths
fx  Same as `fs` if it makes sense, otherwise f
```

## Prefixes

```
:  read (default)  builtin/custom command
$  shell           shell command
%  shell-pipe      shell command running with the ui
!  shell-wait      shell command waiting for key press
&  shell-async     shell command running asynchronously
```
