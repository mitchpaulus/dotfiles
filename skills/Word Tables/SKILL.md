---
name: 'Word Table'
description: 'This skill is for generating Microsoft Word VBA code from data using Python.'
---

I have a personal Python library that you can expect to be on the Python path as a module named `word_vba`.
You can read through the actual source code in `word_vba.py` in this directory to view everything.

Here's an example of how it's used.

```python
def test():
    table = Table()
    table.set_data([
        ['Data'],
        ['Name', 'Age', 'City'],
        ['Alice', '25', 'New York'],
        ['Bob', '30', 'San Francisco'],
    ])
    table.merge_cells(1, 1, 1, 3)
    table.set_background_color(Cell(1, 1), CCLLC_BLUE)
    table.bold(Row(1), True).bold(Row(2), True).vertical_align(Row(1), WordVerticalAlignment.wdCellAlignVerticalBottom).vertical_align(Row(2), WordVerticalAlignment.wdCellAlignVerticalBottom)
    table.horizontal_align(Row(1), WordParagraphAlignment.wdAlignParagraphCenter).horizontal_align(Row(2), WordParagraphAlignment.wdAlignParagraphCenter)

    print(table.compile())
```

This is my library. If you run into issues or things that would make things simpler, STOP. PLEASE LET ME KNOW so I can improve the library code itself.
