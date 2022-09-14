# Unison Programming Language

## Installation

Followed steps from Slack:

```
mkdir -p unisonlanguage
curl -# -L https://github.com/unisonweb/unison/releases/download/M2-Linux/unison-Linux.tar.gz --output unisonlanguage/ucm.tar.gz
tar -xzf unisonlanguage/ucm.tar.gz -C unisonlanguage
./unisonlanguage/ucm
```

Ran into issue on Manjaro:

```
./ucm: /usr/lib/libtinfo.so.6: no version information available (required by ./ucm)
```

after installation. Has to do with how the ncurses library was compiled.

So had to compile an ncurses library myself.

Downloaded from FTP like:

```
curl --output ncurses.tar.gz ftp://ftp.invisible-island.net/ncurses/ncurses.tar.gz
tar -xvf ncurses.tar.gz
```

```
./configure --prefix $HOME/repos/ncurses/output/ncurses --with-versioned-syms --with-termlib --with-shared
make -j
make install
```

Then make sure to prepend that install location to `LD_LIBRARY_PATH`.
For fish:

```
set -gxp 'LD_LIBRARY_PATH' $HOME/repos/ncurses/output/ncurses/lib/
```

Debugged using:
https://stackoverflow.com/a/63730734/5932184
