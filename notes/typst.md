```
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

#table(
  table.header(repeat: true, ..content),
  "More content"
)


- List item 1
- List item 2

`code` in text.

// Call a function.
#list([A], [B])

// Named arguments and trailing content blocks.
#enum(start: 2)[A][B]

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

```
