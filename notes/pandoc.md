# Pandoc

## Syntax Highlighting

- Uses KDE syntax, definition [here](https://docs.kde.org/stable5/en/kate/katepart/highlight.html)

- Can use in Kate, possibly putting in this directory? From <https://github.com/jgm/highlighting-kate/blob/master/xml/maxima.xml>

  - `Usage: place maxima.xml in $KDEDIR/share/apps/katepart/syntax`

Based on this [page](https://api.kde.org/frameworks/syntax-highlighting/html/#syntax-definition-files),

For local user 	$HOME/.local/share/org.kde.syntax-highlighting/syntax/
For Flatpak packages 	$HOME/.var/app/package-name/data/org.kde.syntax-highlighting/syntax/
For Snap packages 	$HOME/snap/package-name/current/.local/share/org.kde.syntax-highlighting/syntax/
On Windows® 	&#37;USERPROFILE&#37;&#92;AppData&#92;Local&#92;org.kde.syntax-highlighting&#92;syntax&#92;
On macOS® 	$HOME/Library/Application Support/org.kde.syntax-highlighting/syntax/

Also described in <https://docs.kde.org/trunk5/en/kate/katepart/highlight.html>

## Tex target

Will need `\tightlist` command. Default definition is:

```tex
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
```

## Plain Text Target

`--to plain`

## Setting margins or other PDF/Latex options from command line

<https://unix.stackexchange.com/a/397495/296724>

```sh
pandoc -V geometry:"margin=1in, landscape"
```


## Templates

- Used with the `standalone` option.
- Syntax:

```
$--   // Comment
$......$ or ${  }   // Delimiters to put special stuff

Variables:
$foo$
$foo.bar.baz$
$foo_bar.baz-bim$
$ foo $
${foo}
${foo.bar.baz}
${foo_bar.baz-bim}
${ foo }

Conditionals:
$if(foo)$bar$endif$

$if(foo)$
  $foo$
$endif$

$if(foo)$
part one
$else$
part two
$endif$

${if(foo)}bar${endif}

${if(foo)}
  ${foo}
${endif}

${if(foo)}
${ foo.bar }
${else}
no foo!
${endif}

```
[For loops](https://pandoc.org/MANUAL.html#for-loops)

Pipes: Simple Transformations

- pairs
- uppercase
- lowercase
- length
- reverse
- first
- last
- rest
- allbutlast
- chomp
- nowrap
- alpha
- roman
- <left|center|right> n "leftborder" "rightborder"


## Columns in Presentations

```
# Use fenced divs

:::: columns

:::: column
Stuff
::::

:::: column
Stuff
::::
```

## Default MS Word Template

```
pandoc -o custom-reference.docx --print-default-data-file reference.docx
# Put a reference.docx at $HOME/.local/share/pandoc
pandoc --reference-doc=reference.docx -o output.docx input.md
```

## Image Width

`![](file.jpg){ width=50% }`

## Custom MS Word Styles Pandoc

<https://pandoc.org/MANUAL.html#custom-styles>

Can wrap in fenced divs:

```
::: {custom-style="My Style"}
Stuff
:::

Inline [stuff]{custom-style="My Style"}
```

## Keeping Tab characters

Use `&#9;`

## Table Captions

`Table:` at the beginning of a paragraph.

## Custom syntax highlighting

`--syntax-definition`

## Single line

--wrap=none (auto, preserve, none)

## Equation Numbering

Can use `\tag{123}` to manually number equations. Thanks <https://stackoverflow.com/a/78389640>

Or use `pandoc-crossref`. Also see <https://github.com/lierdakil/pandoc-crossref/issues/343#issuecomment-1471971878>

## `pandoc-crossref`

```
pandoc -F pandoc-crossref -F pandoc-citeproc -o output.pdf input.md

# Figure references
![Caption](image.png){#fig:label}
As seen in @fig:label.
```

Default docx extensions (`pandoc --list-extensions=docx`)

```
-ascii_identifiers
+auto_identifiers
-citations
-east_asian_line_breaks
-empty_paragraphs
-gfm_auto_identifiers
-native_numbering
-styles
```
