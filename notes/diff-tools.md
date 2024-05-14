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
