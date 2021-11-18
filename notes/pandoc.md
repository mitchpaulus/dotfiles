# Pandoc

## Syntax Highlighting

- Uses KDE syntax, definition [here](https://docs.kde.org/stable5/en/kate/katepart/highlight.html)

## Tex target

Will need `\tightlist` command. Default definition is:

```tex
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
```

## Plain Text Target

`--to plain`

## Setting margins or other PDF/Latex options from command line

```sh
pandoc -V geometry:margin=1in
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
```
