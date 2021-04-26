# LaTex

## Arrows

![Latex Arrows](img/latex_arrows.png)


## Hyperref warning - Token not allowed in a PDF string

Solution: [Stack Exchange](https://tex.stackexchange.com/questions/10555/hyperref-warning-token-not-allowed-in-a-pdf-string)

Appears to normally be caused by having TeX commands in a location that
get turned into a hyperref link. For `elsarticle`s, the place it showed
up for me is in the `\author` command. Use `\texorpdfstring{tex
stuff}{pdf stuff - normally empty}` to get around the issue.

```tex
\author{Mitchell T. Paulus \texorpdfstring{\corref{cor1}\fnref{fn1}}{}}
```

## TeX Live

- Update `tlmgr`: `[sudo] tlmgr update --self`
- Update all packages: `[sudo] tlmgr update --all`
- List what would be updated: `[sudo] tlmgr update --list`

Based on my testing, `\maketitle{}` has to be after the abstract
definition.

## Abstract

```latex
\begin{abstract}

\end{abstract}
\maketitle{}
```

## Fonts

```latex
\usepackage{fontspec}
\setmonofont{fontname}[Scale=0.8]
```

I don't think Latex has the concept of setting a different font size
outside of the main one set at the beginning of the document class.
Generally can use commands like `\big` etc. For `fontspec`, the concept
is similar, you can just apply a `Scale`, which is a fraction of the
main document size.

## Bibliographies

Stack Exchange answer: https://tex.stackexchange.com/questions/25701/bibtex-vs-biber-and-biblatex-vs-natbib

Packages: biblatex, natbib
Preprocessing Programs (.bib -> .bbl): biber, BibTeX

Database files: .bib (biber has extended options vs. BibTeX)

biber and biblatex are the newer programs. Key features for `biber`:

1. Full Unicode support (huge)
2. Can better handle names (given, family, prefix, etc.)

### `.bib` file format

4 types of entries:

1. @STRING { identifier = "Value" }
2. @PREAMBLE { ? }
3. @COMMENT { "Any comment" }
4. @entry { tags = "values", ... }

**Tags**

- Case insensitive
- Can surround with either curly braces or quotations. Escape either of these with '\' if required.

### Biblatex compilation

Normally goes:

1. `pdflatex` or `lualatex`, etc. -> should generate .bcf file during
   compilation if the `biblatex` package is used.
2. `biber <basename>`
3. `pdflatex` or `lualatex`, etc. until convergence.

