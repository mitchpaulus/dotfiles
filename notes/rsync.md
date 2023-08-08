# `rsync`

- Need the `-r` flag to recursively sync directories. `-a` also implies this

```
rsync [OPTION]... SRC [SRC]... DEST
rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
--progress
-n --dry-run
-a, --archive == -rlptgoD


# Trailing slash on source is critical. Without it, copies the directory, not files within.
rsync -avz foo:src/bar/ /data/tmp
```
