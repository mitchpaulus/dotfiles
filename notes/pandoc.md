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
