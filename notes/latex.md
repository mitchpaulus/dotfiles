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
