# Installation errors

When installing on WSL Ubuntu, get error

`qpdf: error while loading shared libraries: libqpdf.so.28: cannot open shared object file: No such file or directory`

Resolve the issue by adding `/usr/local/lib` to the `LD_LIBRARY_PATH`
variable. See [here](https://github.com/qpdf/qpdf/issues/175) for
discussion. From looking at the `/etc/ld.so.conf` contents, it looks
like `/usr/local/lib` should be getting picked up, but it's not.

In fish config added:

```
set -gx LD_LIBRARY_PATH "/usr/local/lib" $LD_LIBRARY_PATH
```

Can use `ldd` command to check whether things link correctly.

Used like:

```sh
ldd /usr/local/bin/qpdf
```

## Update: Tuesday 2020-11-10

After rechecking these paths that were listed in the
`/etc/ld.so.conf.d/` folder, I came across
[this post](https://stackoverflow.com/a/47929012/5932184), which
mentioned running

```sh
sudo ldconfig
```

to update the LD configuration. Things seemed to now work without the
explicit path being set. I'm not sure if something didn't update when I
updated Ubuntu versions or what.

# Examples

Print number of pages in PDF: `qpdf --show-npages file.pdf`

Get useful document information in JSON form:

```sh
qpdf --json [--json-key=key]
```

Get bookmark details:
```sh
qpdf --json --json-key=outlines
```

Concatenate pages from multiple pdfs:

Page selection:

```sh
--pages input-file [ --password=password ] [ page-range ] [ ... ] --
```

Concatenate all pages of PDFs:

```
qpdf --empty out.pdf --pages *.pdf --
```

## Joining various pages from separate files

Note that only *one* `--pages` option should be given, terminated with
a `--`.

```sh
qpdf --pages file1.pdf 1-2 file2.pdf 3-4 -- --empty output.pdf
```

The page range is a set of numbers separated by commas, ranges of
numbers separated dashes, or combinations of those.  The character
"z" represents the last page.  A number preceded by an "r" indicates
to count from the end, so "r3-r1" would be the last three pages of the
document.  Pages can appear in any order.  Ranges can appear with a
high number followed by a low number, which causes the pages to appear in
reverse.  Numbers may be repeated.  A page range may be appended with :odd
to indicate odd pages in the selected range or :even to indicate even
pages.

