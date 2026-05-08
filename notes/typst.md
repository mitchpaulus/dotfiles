```
#set text(font: "Times New Roman")

// Table captions on top
#show figure.where(
  kind: table
): set figure.caption(position: top)

= Header
== Level 2 Header
<labelforpreviousheader>

#let solid_blue = rgb(0, 84, 166)
#grid(
  columns: (1fr, 1fr), // or columns: (auto, 1fr)
  stroke: 0.5pt, // gridlines
  content1, content2
  [content3], [content4],
  table.cell(colspan: 2)[Wide content],
)

#set grid(row-gutter: 10pt, column-gutter: 5pt) // Set global properties for the element function

#strong[bold text]
#emph[italic text]

#set page(flipped: true) // landscape

// Center all tables
#show table: it => align(center, it)

// CCLLC color headers
#set table(fill: (x, y) => if y == 0 { rgb(0, 73, 135) })
#show table.cell.where(y: 0): it => {
  set text(fill: white, weight: "bold")
  it
}

#table(
    columns: (auto, auto, auto, auto, auto),
    fill: (x, y) => if y == 0 { rgb(0, 73, 135) },
    align: (left, center, center, center, center),
  table.header(repeat: true, ..content),

  "More content"
)

// Table captions
#figure(
 table(
  ...
 ),
 figure.caption(
  position: top,
  [Caption]
))


- List item 1
- List item 2

+ Numbered item 1
+ Numbered item 2

`code` in text.

// Call a function.
#list([A], [B])

// Named arguments and trailing content blocks. The `][` must touch with no space.
#enum(start: 2)[A][B]
// https://typst.app/docs/reference/model/enum/
#set enum(numbering: "(a)") // https://typst.app/docs/reference/model/numbering/

// Version without parentheses.
#list[A][B]

#set text(fill: color) // <https://typst.app/docs/reference/text/text/>

// Can also do positional parameters *by type*
#set text(blue) // Works because "fill" is the first parameter that can take that type

#align(alignment, content)
// start: Aligns at the start of the text direction.
// end: Aligns at the end of the text direction.
// left: Align at the left.
// center: Aligns in the middle, horizontally.
// right: Aligns at the right.
// top: Aligns at the top.
// horizon: Aligns in the middle, vertically.
// bottom: Align at the bottom.

#figure(
  image("glacier.jpg", width: 80%),
  caption: [A curious figure.],
) <glacier>

#pagebreak()
#super[3]
#sub[2]

// 3 modes:

// Code, prefixed with '#'
// Math, $
// Content, [ ... ]

// Bookmark a page without having anything really there:
#let bookmark(title, level: 1) = {
  place(top + left)[
    #box(width: 0pt, height: 0pt)[
      #hide[#heading(level: level, outlined: false, bookmarked: true)[#title]]
    ]
  ]
}

// Allow breaks in long tables

#[
  #show figure: set block(breakable: true)
  #figure(
    caption: [Estimated AHU and IRCU capacities.],
    include "ahu_table.typ"
  )
]



```

Set and Show

```
#set element_function(optionalParma1: newValue, optionalParma2: newValue..)
```

Set is basically resetting the defaults on element functions.

Show is an arbitrary transformation.
