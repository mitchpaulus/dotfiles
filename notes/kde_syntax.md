# KDE Syntax Highlighting

[link](https://docs.kde.org/stable5/en/kate/katepart/highlight.html)

Root element: `language`
Required Attributes
    - name
    - section
    - extensions="\*.ext",
    - version
    - kateversion="2.4"

Optional Attributes
    - author

Then `highlighting` element, with required elements `contexts` and
`itemdatas`. Optional `list` elements.

## Detection Rules

2 required XML attributes:

1. `attribute` - maps to item defined in `itemData`. Sets the style.
2. `context` - sets the context to use.



## KDE Regex

[link](https://docs.kde.org/stable5/en/kate/katepart/regular-expressions.html)


