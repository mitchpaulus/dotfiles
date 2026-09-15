---
name: "PDF Bookmarks"
description: 'Scripts to get and set bookmarks for PDFs.'
---

I have two simple scripts to help manage PDF bookmarks, `get_bookmarks` and `set_bookmarks`.
You can use the `--help` on each of those to get the latest help.
They both use `uv` and `PyMuPDF` underneath.

The output of `get_bookmarks` works with the input of `set_bookmarks`, so it can be used like:

```
get_bookmarks FILE | set_bookmarks -o NEWFILE FILE
```

as a no-op, other than it can clean up bad ways of bookmarking that sometimes cause issues on certain PDF readers like Bluebeam.
