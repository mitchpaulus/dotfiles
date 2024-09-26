#!/usr/bin/env python3

from enum import IntEnum

"""Table documentation:
https://learn.microsoft.com/en-us/office/vba/api/word.table

Methods:

ApplyStyleDirectFormatting
AutoFitBehavior
AutoFormat
Cell
ConvertToText
Delete
Select
Sort
SortAscending
SortDescending
Split
UpdateAutoFormat

Properties:

AllowAutoFit
Application
ApplyStyleColumnBands
ApplyStyleFirstColumn
ApplyStyleHeadingRows
ApplyStyleLastColumn
ApplyStyleLastRow
ApplyStyleRowBands
AutoFormatType
Borders
BottomPadding
Columns
Creator
Descr
ID
LeftPadding
NestingLevel
Parent
PreferredWidth
PreferredWidthType
Range
RightPadding
Rows
Shading
Spacing
Style
TableDirection
Tables
Title
TopPadding
Uniform
"""

#   Name                          Value   Description
#   wdAlignParagraphCenter        1       Center-aligned.
#   wdAlignParagraphDistribute    4       Paragraph         characters   are   distributed   to           fill          the      entire   width   of   the   paragraph.
#   wdAlignParagraphJustify       3       Fully             justified.
#   wdAlignParagraphJustifyHi     7       Justified         with         a     high          character    compression   ratio.
#   wdAlignParagraphJustifyLow    8       Justified         with         a     low           character    compression   ratio.
#   wdAlignParagraphJustifyMed    5       Justified         with         a     medium        character    compression   ratio.
#   wdAlignParagraphLeft          0       Left-aligned.
#   wdAlignParagraphRight         2       Right-aligned.
#   wdAlignParagraphThaiJustify   9       Justified         according    to    Thai          formatting   layout.

# Word Paragraph Alignment
# https://learn.microsoft.com/en-us/office/vba/api/word.wdparagraphalignment
class WordParagraphAlignment(IntEnum):
    wdAlignParagraphLeft        = 0
    wdAlignParagraphCenter      = 1
    wdAlignParagraphRight       = 2
    wdAlignParagraphJustify     = 3
    wdAlignParagraphDistribute  = 4
    wdAlignParagraphJustifyMed  = 5
    wdAlignParagraphJustifyHi   = 7
    wdAlignParagraphJustifyLow  = 8
    wdAlignParagraphThaiJustify = 9

# https://learn.microsoft.com/en-us/office/vba/api/Word.WdCellVerticalAlignment
# Name	                    Value	Description
# wdCellAlignVerticalTop	0	    Text is aligned to the top border of the cell.
# wdCellAlignVerticalCenter	1	    Text is aligned to the center of the cell.
# wdCellAlignVerticalBottom	3	    Text is aligned to the bottom border of the cell.

class WordVerticalAlignment(IntEnum):
    wdCellAlignVerticalTop     = 0
    wdCellAlignVerticalCenter  = 1
    wdCellAlignVerticalBottom  = 3

# https://learn.microsoft.com/en-us/office/vba/api/Word.WdRowAlignment
# wdAlignRowCenter	1	Centered.
# wdAlignRowLeft	0	Left-aligned. Default.
# wdAlignRowRight	2	Right-aligned.

class WordHorizontalRowAlignment(IntEnum):
    wdAlignRowLeft   = 0
    wdAlignRowCenter = 1
    wdAlignRowRight  = 2


class WordBorderType(IntEnum):
    wdBorderBottom       = -3
    wdBorderDiagonalDown = -7
    wdBorderDiagonalUp   = -8
    wdBorderHorizontal   = -5
    wdBorderLeft         = -2
    wdBorderRight        = -4
    wdBorderTop          = -1
    wdBorderVertical     = -6

# https://learn.microsoft.com/en-us/office/vba/api/word.wdbordertype
# Name	Value	Description
# wdBorderBottom	-3	A bottom border.
# wdBorderDiagonalDown	-7	A diagonal border starting in the upper-left corner.
# wdBorderDiagonalUp	-8	A diagonal border starting in the lower-left corner.
# wdBorderHorizontal	-5	Horizontal borders.
# wdBorderLeft	-2	A left border.
# wdBorderRight	-4	A right border.
# wdBorderTop	-1	A top border.
# wdBorderVertical	-6	Vertical borders.

# Borders Object.
# https://learn.microsoft.com/en-us/office/vba/api/word.borders

class Row:
    # https://learn.microsoft.com/en-us/office/vba/api/word.row
    # Methods:
    # ConvertToText Delete Select
    # SetHeight SetLeftIndent

    # Properties:
    # Alignment AllowBreakAcrossPages Application Borders Cells Creator
    # HeadingFormat Height HeightRule ID Index IsFirst IsLast LeftIndent NestingLevel
    # Next Parent Previous Range Shading SpaceBetweenColumns
    def __init__(self, row: int) -> None:
        self.row = row

class Column:
    # Methods:
    # AutoFit Delete Select SetWidth Sort
    # Properties:
    # Application Borders Cells Creator Index IsFirst IsLast
    # NestingLevel Next Parent PreferredWidth PreferredWidthType Previous Shading Width
    def __init__(self, column: int) -> None:
        self.column = column

class Cell:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column


class Range:
    def __init__(self, start_row: int, start_col: int, end_row: int, end_col: int) -> None:
        self.start_row = start_row
        self.start_col = start_col
        self.end_row = end_row
        self.end_col = end_col

class Color:
    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

CCLLC_BLUE = Color(0, 73, 135)

class Table:
    def __init__(self) -> None:
        self._merges = []
        self._background_colors = []
        self._bolds = []
        self._vertical_alignments = []
        self._horizontal_alignments = []
        self.font_sizes = []
        self._col_widths = []
        self._autofits = []
        self.decimal_tabs = []

        self.current_cell_range = None

        self._borders = True

    def row(self, row: int):
        self.current_cell_range = Row(row)

    def column(self, column: int):
        self.current_cell_range = Column(column)

    def no_borders(self):
        self._borders = False

    def num_rows(self):
        return len(self.data)

    def num_cols(self):
        if not self.data:
            return 0
        return max([len(row) for row in self.data])

    def merge_cells(self, start_row: int, start_col: int, end_row: int, end_col: int):
        self._merges.append((start_row, start_col, end_row, end_col))
        return self

    def set_data(self, data: list[list[str]]):
        self.data = data
        return self

    def set_background_color(self, cell_range, color: Color):
        self._background_colors.append((cell_range, color))
        return self

    def bold(self, cell_range, bold: bool):
        self._bolds.append((cell_range, bold))
        return self

    def font_size(self, *args):
        if len(args) == 1:
            if self.current_cell_range is None:
                raise ValueError("No cell range set")
            cell_range = self.current_cell_range
            font_size = args[0]
        elif len(args) == 2:
            cell_range = args[0]
            font_size = args[1]
        else:
            raise ValueError("Invalid number of arguments")

        self.font_sizes.append((cell_range, font_size))
        return self

    def vertical_align(self, cell_range, alignment: WordVerticalAlignment):
        self._vertical_alignments.append((cell_range, alignment))
        return self

    def horizontal_align(self, cell_range, alignment: WordParagraphAlignment):
        self._horizontal_alignments.append((cell_range, alignment))
        return self

    def decimal_tab(self, cell_range, position):
        self.decimal_tabs.append((cell_range, position))
        return self

    def col_width(self, col, width_inches):
        if isinstance(col, int):
            self._col_widths.append((col, width_inches))
        elif isinstance(col, Column):
            self._col_widths.append((col.column, width_inches))

        return self

    def col_autofit(self, col = None):
        if col is None:
            for i in range(1, self.num_cols() + 1):
                self._autofits.append(i)
        elif isinstance(col, int):
            self._autofits.append(col)
        elif isinstance(col, Column):
            self._autofits.append(col.column)

        return self

    def obj_from_cell_range(self, cell_range):
        if isinstance(cell_range, Cell):
            row = self.eval_row(cell_range.row)
            col = self.eval_col(cell_range.column)
            return f'tbl.Cell({row}, {col})'
        elif isinstance(cell_range, Row):
            row = self.eval_row(cell_range.row)
            return f'tbl.Rows({row})'
        elif isinstance(cell_range, Column):
            col = self.eval_col(cell_range.column)
            return f'tbl.Columns({col})'
        elif isinstance(cell_range, Table):
            return 'tbl'
        else:
            raise ValueError(f"Cell range type not supported yet: {type(cell_range).__name__}")

    def eval_row(self, row):
        if row == 0:
            raise ValueError("Row index is 1-based")
        if row < 0:
            return self.num_rows() + row + 1
        return row

    def eval_col(self, col):
        if col == 0:
            raise ValueError("Column index is 1-based")
        if col < 0:
            return self.num_cols() + col + 1
        return col

    def apply_to_range(self, cell_range, vba):
        if not vba.startswith('.'):
            vba = '.' + vba
        lines = []
        if isinstance(cell_range, Column):
            # Columns don't have Range property, so we have to use Cells
            lines.append(f'For Each C In {self.obj_from_cell_range(cell_range)}.Cells')
            lines.append(f'  C.Range{vba}')
            lines.append('Next C')
            pass
        elif isinstance(cell_range, Range):
            lines.append(f'For IntRow = {self.eval_row(cell_range.start_row)} To {self.eval_row(cell_range.end_row)}')
            lines.append(f'  For IntCol = {self.eval_col(cell_range.start_col)} To {self.eval_col(cell_range.end_col)}')
            lines.append(f'    tbl.Cell(IntRow, IntCol).Range{vba}')
            lines.append('  Next IntCol')
            lines.append('Next IntRow')
        else:
            lines.append(f'{self.obj_from_cell_range(cell_range)}.Range{vba}')

        return lines


    def compile(self):
        """Compile table information into the required Word VBA"""
        lines = []
        lines.append("Dim tbl As Table")
        lines.append(f'Set tbl = ActiveDocument.Tables.Add(Range:=Selection.Range, NumRows:={self.num_rows()}, NumColumns:={self.num_cols()}, DefaultTableBehavior:=wdWord9TableBehavior, AutoFitBehavior:=wdAutoFitFixed)')

        for cell_range, color in self._background_colors:
            lines.extend(self.apply_to_range(cell_range, f'.Shading.BackgroundPatternColor = RGB({color.r}, {color.g}, {color.b})'))

        for cell_range, bold in self._bolds:
            vba_bool = 'True' if bold else 'False'
            lines.extend(self.apply_to_range(cell_range, f'.Font.Bold = {vba_bool}'))

        for cell_range, alignment in self._vertical_alignments:
            if isinstance(cell_range, Row):
                lines.append(f'{self.obj_from_cell_range(cell_range)}.Cells.VerticalAlignment = {alignment}')
            elif isinstance(cell_range, Column):
                lines.append(f'{self.obj_from_cell_range(cell_range)}.Cells.VerticalAlignment = {alignment}')
            elif isinstance(cell_range, Table):
                lines.append(f'tbl.Range.Cells.VerticalAlignment = {alignment}')
            elif isinstance(cell_range, Range):
                lines.append(f'For row = {self.eval_row(cell_range.start_row)} To {self.eval_row(cell_range.end_row)}')
                lines.append(f'  For col = {self.eval_col(cell_range.start_col)} To {self.eval_col(cell_range.end_col)}')
                lines.append(f'    tbl.Cell(row, col).VerticalAlignment = {alignment}')
                lines.append('  Next col')
                lines.append('Next row')
            elif isinstance(cell_range, Cell):
                lines.append(f'{self.obj_from_cell_range(cell_range)}.VerticalAlignment = {alignment}')
            else:
                raise ValueError(f"Cell range type not supported yet: {type(cell_range)}")

        for cell_range, alignment in self._horizontal_alignments:
            if isinstance(cell_range, Column):
                # Columns don't have Range property, so we have to use Cells
                lines.append(f'For Each c In {self.obj_from_cell_range(cell_range)}.Cells')
                lines.append(f'  c.Range.ParagraphFormat.Alignment = {alignment}')
                lines.append('Next c')
                pass
            elif isinstance(cell_range, Range):
                lines.append(f'For IntRow = {self.eval_row(cell_range.start_row)} To {self.eval_row(cell_range.end_row)}')
                lines.append(f'  For IntCol = {self.eval_col(cell_range.start_col)} To {self.eval_col(cell_range.end_col)}')
                lines.append(f'    tbl.Cell(IntRow, IntCol).Range.ParagraphFormat.Alignment = {alignment}')
                lines.append('  Next IntCol')
                lines.append('Next IntRow')
            else:
                lines.append(f'{self.obj_from_cell_range(cell_range)}.Range.ParagraphFormat.Alignment = {alignment}')

        for cell_range, font_size in self.font_sizes:
            lines.append(f'{self.obj_from_cell_range(cell_range)}.Range.Font.Size = {font_size}')

        for i, row in enumerate(self.data):
            statements = [f'tbl.Cell({i+1}, {j+1}).Range.Text = "{cell}"' for j, cell in enumerate(row)]
            lines.append(" : ".join(statements))

        for cell_range, position in self.decimal_tabs:
            if isinstance(cell_range, Column):
                # Columns don't have Range property, so we have to use Cells
                lines.append(f'For Each C In {self.obj_from_cell_range(cell_range)}.Cells')
                lines.append(f'  c.Range.ParagraphFormat.TabStops.Add Position:={position}, Alignment:=wdAlignTabDecimal Leader:=wdTabLeaderSpaces')
                lines.append('Next C')
            elif isinstance(cell_range, Range):
                lines.append(f'For IntRow = {self.eval_row(cell_range.start_row)} To {self.eval_row(cell_range.end_row)}')
                lines.append(f'  For IntCol = {self.eval_col(cell_range.start_col)} To {self.eval_col(cell_range.end_col)}')
                lines.append(f'    tbl.Cell(IntRow, IntCol).Range.ParagraphFormat.TabStops.Add Position:={position}, Alignment:=wdAlignTabDecimal, Leader:=wdTabLeaderSpaces')
                lines.append('  Next IntCol')
                lines.append('Next IntRow')
            else:
                lines.append(f'{self.obj_from_cell_range(cell_range)}.Range.ParagraphFormat.TabStops.Add Position:={position}, Alignment:=wdAlignTabDecimal, Leader:=wdTabLeaderSpaces')
            #  for j, cell in enumerate(row):
                #  lines.append(f'tbl.Cell({i+1}, {j+1}).Range.Text = "{cell}"')

        for col in self._autofits:
            lines.append(f'tbl.Columns({col}).AutoFit')

        if self._col_widths:
            # Clear 'PreferredWidth on table width. Remove AllowAutoFit
            lines.append('tbl.PreferredWidthType = wdPreferredWidthAuto')
            lines.append('tbl.PreferredWidth = 0')
            lines.append('tbl.AllowAutoFit = False')

        for col, width in self._col_widths:
            lines.append(f'tbl.Columns({col}).Width = InchesToPoints({width})')

        if self._col_widths:
            lines.append('tbl.AllowAutoFit = True')

        for merge in self._merges:
            start_row = merge[0] if merge[0] > 0 else self.num_rows() + merge[0] + 1 # 1-based index
            start_col = merge[1] if merge[1] > 0 else self.num_cols() + merge[1] + 1 # 1-based index
            end_row = merge[2] if merge[2] > 0 else self.num_rows() + merge[2] + 1 # 1-based index
            end_col = merge[3] if merge[3] > 0 else self.num_cols() + merge[3] + 1

            lines.append(f'tbl.Cell({start_row}, {start_col}).Merge MergeTo:=tbl.Cell({end_row}, {end_col})')

        if not self._borders:
            lines.append('tbl.Borders.Enable = False')

        return "\n".join(lines) + "\n"


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

if __name__ == "__main__":
    test()
