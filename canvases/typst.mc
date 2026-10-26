{
  "version": 1,
  "grid": 8.0,
  "preamble": "",
  "page": "c639556d",
  "pages": [
    {
      "id": "c639556d",
      "name": "Page 1",
      "view": {
        "x": 1805.1741943359375,
        "y": 621.2307739257812,
        "zoom": 0.8055410385131836
      },
      "nodes": [
        {
          "id": "206d6d28",
          "type": "typst",
          "x": -1840.0,
          "y": -672.0,
          "width": 640.0,
          "height": null,
          "source": "```typst\n#set text(font: \"Times New Roman\")\n#show link: underline\n#link(\"https://url.com\")[Description]\n\n// Table captions on top\n#show figure.where(\n  kind: table\n): set figure.caption(position: top)\n\n#let solid_blue = rgb(0, 84, 166)\n#grid(\n  columns: (1fr, 1fr), // or columns: (auto, 1fr)\n  stroke: 0.5pt, // gridlines\n  content1, content2\n  [content3], [content4],\n  table.cell(colspan: 2)[Wide content],\n)\n\n#set grid(row-gutter: 10pt, column-gutter: 5pt) // Set global properties for the element function\n\n#set page(flipped: true) // landscape\n\n// Center all tables\n#show table: it => align(center, it)\n\n// CCLLC color headers\n#set table(fill: (x, y) => if y == 0 { rgb(0, 73, 135) })\n#show table.cell.where(y: 0): it => {\n  set text(fill: white, weight: \"bold\")\n  it\n}\n\n#table(\n    columns: (auto, auto, auto, auto, auto),\n    fill: (x, y) => if y == 0 { rgb(0, 73, 135) },\n    align: (left, center, center, center, center),\n  table.header(repeat: true, ..content),\n\n  \"More content\"\n)\n\n// Table captions\n#figure(\n table(\n  ...\n ),\n figure.caption(\n  position: top,\n  [Caption]\n))\n\n// Call a function.\n#list([A], [B])\n\n// Version without parentheses.\n#list[A][B]\n\n#set text(fill: color) // <https://typst.app/docs/reference/text/text/>\n\n// Can also do positional parameters *by type*\n#set text(blue) // Works because \"fill\" is the first parameter that can take that type\n\n#align(alignment, content)\n// start: Aligns at the start of the text direction.\n// end: Aligns at the end of the text direction.\n// left: Align at the left.\n// center: Aligns in the middle, horizontally.\n// right: Aligns at the right.\n// top: Aligns at the top.\n// horizon: Aligns in the middle, vertically.\n// bottom: Align at the bottom.\n\n#figure(\n  image(\"glacier.jpg\", width: 80%),\n  caption: [A curious figure.],\n) <glacier>\n\n# Valid image types: \"png\", \"jpg\", \"gif\", \"svg\", \"pdf\", \"webp\"\n\n#pagebreak()\n#super[3]\n#sub[2]\n\n#quote(block: true)[My block quote content like > in markdown]\n\n// 3 modes:\n\n// Code, prefixed with '#'\n// Math, $\n// Content, [ ... ]\n\n// Bookmark a page without having anything really there:\n#let bookmark(title, level: 1) = {\n  place(top + left)[\n    #box(width: 0pt, height: 0pt)[\n      #hide[#heading(level: level, outlined: false, bookmarked: true)[#title]]\n    ]\n  ]\n}\n\n\n// User defined function:\n\n#let my_func(content) = block(sticky: true)[ #strong[#content] ]\n\n```\n\nSet and Show\n\n```\n#set element_function(optionalParma1: newValue, optionalParma2: newValue..)\n```\n\nSet is basically resetting the defaults on element functions.\n\nShow is an arbitrary transformation.\n\n\n== Math Syntax\n\nhttps://typst.app/docs/reference/math/\n\n```\n\"text\"\ntimes # (\"x\")\n```\n"
        },
        {
          "id": "9896a9f1",
          "type": "typst",
          "x": -2176.0,
          "y": -672.0,
          "width": 320.0,
          "height": null,
          "source": "= Basics\n\n```typst\n- List item 1\n- List item 2\n\n+ Numbered item 1\n+ Numbered item 2\n\n`code` in text.\n\n= Header\n== Level 2 Header\n<labelforpreviousheader>\n\n#strong[bold text]\n#emph[italic text]\n```"
        },
        {
          "id": "b0834f5d",
          "type": "typst",
          "x": -1184.0,
          "y": -672.0,
          "width": 744.0,
          "height": null,
          "source": "= Numbering\n\n```typst\n// Named arguments and trailing content blocks. The `][` must touch with no space.\n#enum(start: 2)[A][B]\n// https://typst.app/docs/reference/model/enum/\n#set enum(numbering: \"(a)\", indent: 5pt) // https://typst.app/docs/reference/model/numbering/\n#set heading(numbering: \"1.a.\")\n\n```"
        },
        {
          "id": "95232902",
          "type": "typst",
          "x": -1184.0,
          "y": -536.0,
          "width": 488.0,
          "height": null,
          "source": "= Arrays\n\n```typst\n#let numbers = (1, 2, 3)\r\n#let names = (\"Alice\", \"Bob\", \"Charlie\")\r\n#let mixed = (1, \"hello\", true)\n#let empty = ()       // Empty array\r\n#let single = (42,)   // One-element array\r\n#let grouped = (42)   // Just the number 42, NOT an array\n#let items = (\"a\", \"b\", \"c\")\r\n\r\n#items.at(0)    // \"a\"\r\n#items.at(1)    // \"b\"\r\n#items.first()  // \"a\"\r\n#items.last()   // \"c\"\r\n#items.len()    // 3\n#let items = (1, 2, 3)\r\n\r\n#let doubled = items.map(x => x * 2)\r\n#let filtered = items.filter(x => x > 1)\r\n#let extended = (..items, 4, 5)\n\n#let cells = (\r\n  [Name],\r\n  [Age],\r\n  [Alice],\r\n  [30],\r\n)\r\n\r\n#table(columns: 2, ..cells)\n```"
        },
        {
          "id": "e56d0284",
          "type": "typst",
          "x": -672.0,
          "y": -528.0,
          "width": 424.0,
          "height": null,
          "source": "= Tables\n\n```typst\n// Allow breaks in long tables\n\n#[\n  #show figure: set block(breakable: true)\n  #figure(\n    caption: [Estimated AHU and IRCU capacities.],\n    include \"ahu_table.typ\"\n  )\n]\n```"
        },
        {
          "id": "275e88ee",
          "type": "typst",
          "x": -1184.0,
          "y": 8.0,
          "width": 320.0,
          "height": null,
          "source": "= Scripts\n\n```typst\nfor value in array {..}\nfor pair in dict {..}\nfor letter in \"string\" {..}\nfor byte in  bytes(\"😀\") {..}\n```"
        }
      ]
    }
  ]
}
