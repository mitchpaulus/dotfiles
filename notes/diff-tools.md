# Diff Tools

[From tecmint](https://www.tecmint.com/best-linux-file-diff-tools-comparison/)

1. Unix diff
2. colordiff
3. wdiff
4. Vimdiff
5. Kompare (KDE) - GUI, Linux
6. DiffMerge - GUI, Cross Platform
7. Meld
8. Diffuse - Linux
9. XXdiff
10. KDiff3
11. TkDiff

## Ignore whitespace

```sh
diff -w file1 file2
diff -r -q dir1 dir2 # Recursively compare directories, just at file level.
```

## `diff2html`

Great tool to show diffs in HTML format, using the output from the Unix `diff`tool.
[GitHub for main program](https://github.com/rtfpessoa/diff2html).
[GitHub for CLI](https://github.com/rtfpessoa/diff2html-cli).

Can use like:

```sh
diff -u --label AHU.08C/CoolingDemand "$old_dir"/AHU.08C --label AHU.08C/CoolingDemand AHU.08C | diff2html -i stdin -o stdout -s side > AHU.08C.html

diff -ru dir1/ dir2/ | diff2html -i stdin -o stdout -s side > diff.html
```

The `-u` (unified) option is important to make the tool work.

Install with:

```sh
npm install -g diff2html-cli
```

Also, using `git diff` is often better for things with additions/deletions.


## Getting names right

The unified diff format only consist of the following (<https://www.gnu.org/software/diffutils/manual/html_node/Detailed-Unified.html>):

2 line header
chunks

```
--- from-file from-file-modification-time
+++ to-file to-file-modification-time

@@ from-file-line-numbers to-file-line-numbers @@
 line-from-either-file
 line-from-either-file…

All lines begin with one of:
' ' no change
'-' line removed
'+' line added
```

Information about files being deleted/modes, etc. can be added arbitrarily by other software.

For example, git adds things like:

```
deleted file mode 100644
```

on deletion of a file. (This is what diff2html looks for to determine deletions.)

# Tabular Diff

<https://specs.frictionlessdata.io/tabular-diff/#language>
