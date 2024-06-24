This is what I want out of document editing, mostly paper/report editing:

1. GUI for editing, programmable, easily editable text data format backing it.
2. Cross-referencing
    - Figures, tables, equations.
3. Mathematical Equations
4. Basic styling
    - Bold, Italic, Underline, etc.
5. Tables, with FULL control
    - Merged cells, alignment, column widths etc.
6. Reference management
7. Numbered lists
8. Should be brutally simple to parse

Nice to haves:

1. Compile to Word
    - Maybe through compile to VBA code?
2. Compile to Latex
3. Title pages?


# Grammar

Line/block based like asciidoc

```
block : props? block_type

block_type
    : header_block
    | paragraph_block
    | list_block
    | table_block
    | figure_block
    | equation_block
    ;

header_block : header_level text
header_level : '#' | '##' | '###' | '####' | '#####' | '######'
paragraph_block : text
list_block : list_item+
```
