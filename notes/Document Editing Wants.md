This is what I want out of document editing, mostly paper/report editing:

1. Cross-referencing
    - Figures, tables, equations.
2. Mathematical Equations
3. Basic styling
    - Bold, Italic, Underline, etc.
4. Tables, with FULL control
    - Merged cells, alignment, column widths etc.
5. Reference management
6. Numbered lists
7. Should be brutally simple to parse
8. Macros

Nice to haves:

1. GUI for editing, programmable, easily editable text data format backing it.
2. Compile to Word
    - Maybe through compile to VBA code?
3. Compile to Latex
4. Title pages?


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
