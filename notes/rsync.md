# `rsync`

- Need the `-r` flag to recursively sync directories. `-a` also implies this

```
--progress
-n --dry-run
-a, --archive == -rlptgoD


# Trailing slash on source is critical. Without it, copies the directory, not files within.
rsync -avz foo:src/bar/ /data/tmp
```
