# `redo`

```
exec >&2
```

```
$1: target name
$2: target name minus extension - only for default do files? This is
whatever has replaced `default`, so if target script was:
default.ext1.ext2 and was called with redo file1.ext1.ext2,
$2 is file1.
$3: temp file name - it is not absolute, so if there is a change of
directory, script must account for that.
```
