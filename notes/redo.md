# `redo`

Now trying the rust port by zombiezen. See <https://github.com/zombiezen/redo-rs>.

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

## Depending on n number of files

Can do something like:

foo.deps
```sh
find -name '*.txt' | redo-stamp
redo-always
```

And then use that somewhere else like

```sh
redo-ifchange foo.deps

for file in *.txt; do
    ...
done
```

## Issues building on WSL

I've come across some issues building `redo` using the bootstrap `do` script.
I think some of the issue has to do with default file permissions given within WSL.

One thing is that the redirection for the `redo/version/vars.do` file does not seem to work with base install.
Was able to solve it by forcing redirect to unique temporary file instead of passing file descriptors around.


### Tests

1. Clean clone, metadata enabled in WSL. `./do build` fails in \_version.py

### Files installed by apenwarr/redo

1. bunch of `redo`s installed to PREFIX/bin/\*
2. `$PREFIX/lib/redo/*`
3. `$PREFIX/share/doc/redo`
4. Man page to `$PREFIX/share/man/man1/`


