#!/usr/bin/env python3
import sys
from enum import IntEnum
from dataclasses import dataclass, field
from typing import Optional, Union

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

def escape_string(input_str: str) -> str:
    """
    Escape a string for use in Word VBA. String is return with double quotes
    """
    new_str = []
    max_line_length = 500

    nLines, rem = divmod(len(input_str), max_line_length)

    line_groups = [input_str[i*max_line_length:min(len(input_str), (i+1)*max_line_length)] for i in range(nLines + 1)]
    end_line_str = "\" _\n  & "

    for g in line_groups:
        new_str.append('"')
        for c in g:
            if c == '"':
                new_str.append('""')
            elif c == '\r':
                pass
            elif c == '\n':
                new_str.append('" & vbCrLf & "')
            else:
                new_str.append(c)

        new_str.append(end_line_str)

    new_str.pop()

    new_str.append('"')

    return "".join(new_str)


def _rtf_escape(text: str) -> str:
    """Escape text for use in RTF content."""
    result = []
    for ch in text:
        if ch == '\\':
            result.append('\\\\')
        elif ch == '{':
            result.append('\\{')
        elif ch == '}':
            result.append('\\}')
        elif ch == '\n':
            result.append('\\line ')
        elif ord(ch) > 127:
            result.append(f'\\u{ord(ch)}?')
        else:
            result.append(ch)
    return ''.join(result)


def _cell_in_range(cell_range, row_1: int, col_1: int, table: 'Table') -> bool:
    """Check if a 1-based (row, col) is within the given cell range."""
    if isinstance(cell_range, Row):
        return table.eval_row(cell_range.row) == row_1
    elif isinstance(cell_range, Column):
        return table.eval_col(cell_range.column) == col_1
    elif isinstance(cell_range, Cell):
        return table.eval_row(cell_range.row) == row_1 and table.eval_col(cell_range.column) == col_1
    elif isinstance(cell_range, Range):
        return (table.eval_row(cell_range.start_row) <= row_1 <= table.eval_row(cell_range.end_row) and
                table.eval_col(cell_range.start_col) <= col_1 <= table.eval_col(cell_range.end_col))
    elif isinstance(cell_range, Table):
        return True
    elif isinstance(cell_range, ColumnMinusHeader):
        return table.eval_col(cell_range.column) == col_1 and row_1 > 1
    return False


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
    # One based Row

    # https://learn.microsoft.com/en-us/office/vba/api/word.row
    # Methods:
    # ConvertToText Delete Select
    # SetHeight SetLeftIndent

    # Properties:
    # Alignment AllowBreakAcrossPages Application Borders Cells Creator
    # HeadingFormat Height HeightRule ID Index IsFirst IsLast LeftIndent NestingLevel
    # Next Parent Previous Range Shading SpaceBetweenColumns
    def __init__(self, row: int) -> None:
        "Row: 1-based index"
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

class ColumnMinusHeader:
    def __init__(self, column: int) -> None:
        self.column = column


type IRange = Row | Column | Cell | Range | Table | ColumnMinusHeader

class Color:
    def __init__(self, r: int, g: int, b: int) -> None:
        """These are 0-255 integer values"""
        self.r = r
        self.g = g
        self.b = b

CCLLC_BLUE = Color(0, 73, 135)


@dataclass
class RtfFragment:
    """A piece of RTF content with associated colors that need color table entries."""
    body: str
    colors: list[Color] = field(default_factory=list)
    font_name: Optional[str] = None


def rtf_document(*fragments: Union[str, RtfFragment]) -> str:
    """Assemble a complete RTF document from fragments (strings or RtfFragments).

    Builds a unified color table from all fragments and adjusts color indices
    so that \\clcbpat references are correct in the merged document.
    """
    # Collect all unique colors across fragments, preserving order
    all_colors: list[Color] = []
    color_set: dict[tuple[int, int, int], int] = {}
    # Map from (fragment_index, old_color_index) -> new_color_index
    remap: list[dict[int, int]] = []

    for frag in fragments:
        frag_remap: dict[int, int] = {}
        if isinstance(frag, RtfFragment):
            for i, color in enumerate(frag.colors):
                key = (color.r, color.g, color.b)
                if key not in color_set:
                    color_set[key] = len(all_colors) + 1  # 1-based
                    all_colors.append(color)
                frag_remap[i + 1] = color_set[key]  # old 1-based -> new 1-based
        remap.append(frag_remap)

    # Build color table
    colortbl = '{\\colortbl ;'
    for color in all_colors:
        colortbl += f'\\red{color.r}\\green{color.g}\\blue{color.b};'
    colortbl += '}'

    # Build body, remapping color indices
    import re
    body_parts = []
    for i, frag in enumerate(fragments):
        if isinstance(frag, str):
            body_parts.append(frag)
        else:
            text = frag.body
            if remap[i]:
                def _replace(m, rm=remap[i]):
                    old_idx = int(m.group(1))
                    new_idx = rm.get(old_idx, old_idx)
                    return f'\\clcbpat{new_idx}'
                text = re.sub(r'\\clcbpat(\d+)', _replace, text)
            body_parts.append(text)

    # Determine font name from fragments (use first specified, fallback to Calibri)
    font_name = 'Calibri'
    for frag in fragments:
        if isinstance(frag, RtfFragment) and frag.font_name:
            font_name = frag.font_name
            break
    fonttbl = '{\\fonttbl{\\f0 ' + font_name + ';}}'

    return '{\\rtf1\\ansi\\deff0\n' + fonttbl + '\n' + colortbl + '\n' + '\n'.join(body_parts) + '\n}'

class TextRun:
    def __init__(self, text: str, *, style = None, bold = None, italic = None, font_size = None):
        self.text = text
        self.style = style
        self.bold = bold
        self.italic = italic
        self.font_size = font_size

    def vba(self) -> list[str]:
        lines = []
        if self.style is not None:
            lines.append(f"Selection.Style = ActiveDocument.Styles(\"{self.style}\")")
        if self.bold is not None:
            lines.append(f"Selection.Font.Bold = {'True' if self.bold else 'False'}")
        if self.italic is not None:
            lines.append(f"Selection.Font.Italic = {'True' if self.italic else 'False'}")
        if self.font_size is not None:
            lines.append(f"Selection.Font.Size = {self.font_size}")

        lines.append(f'Selection.TypeText Text:={escape_string(self.text)}')
        return lines
        


class Table:
    def __init__(self) -> None:
        self._merges: list[tuple[int, int, int, int]] = [] # List of tuples (start_row, start_col, end_row, end_col), all on 1-based index
        self._background_colors = []
        self._bolds = []
        self._vertical_alignments = []
        self._horizontal_alignments = []
        self.font_sizes = []
        self._col_widths = []
        self._autofits = []
        self.decimal_tabs = []
        self._left_padding = None
        self._right_padding = None
        self._top_padding = None
        self._bottom_padding = None
        self._style: Optional[str] = None
        self._header_repeat_rows = 0
        self._table_alignment: Optional[WordParagraphAlignment] = None
        self._font_name: Optional[str] = None
        self._horizontal_cell_margin: Optional[float] = None

        self.current_cell_range = None

        self._borders: Optional[bool] = None

    def row(self, row: int):
        self.current_cell_range = Row(row)

    def column(self, column: int):
        self.current_cell_range = Column(column)

    def borders(self):
        """Enable borders for the table."""
        self._borders = True
        return self

    def no_borders(self):
        self._borders = False
        return self

    def header_repeat_rows(self, num_rows: int):
        """Set the number of header rows to repeat at the top of the table."""
        if num_rows < 0:
            self._header_repeat_rows = 0
        self._header_repeat_rows = num_rows
        return self

    def num_rows(self):
        return len(self.data)

    def num_cols(self):
        if not self.data:
            return 0
        return max([len(row) for row in self.data])

    def merge_cells(self, start_row_one_based: int, start_col_one_based: int, end_row_one_based_inc: int, end_col_one_based_inc: int):
        self._merges.append((start_row_one_based, start_col_one_based, end_row_one_based_inc, end_col_one_based_inc))
        return self

    def set_data(self, data: list[list[str]]):
        self.data = data
        return self

    def set_background_color(self, cell_range, color: Color):
        self._background_colors.append((cell_range, color))
        return self

    def bold(self, cell_range: IRange, bold: bool):
        self._bolds.append((cell_range, bold))
        return self

    def left_padding(self, padding_in):
        self._left_padding = padding_in
        return self

    def right_padding(self, padding_in):
        self._right_padding = padding_in
        return self

    def top_padding(self, padding_in):
        self._top_padding = padding_in
        return self

    def bottom_padding(self, padding_in):
        self._bottom_padding = padding_in
        return self

    def horizontal_cell_margin(self, margin_inches: float) -> 'Table':
        self._horizontal_cell_margin = margin_inches
        return self

    def font_size(self, *args) -> 'Table':
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

    def font_name(self, name: str) -> 'Table':
        self._font_name = name
        return self

    def vertical_align(self, cell_range, alignment: WordVerticalAlignment):
        self._vertical_alignments.append((cell_range, alignment))
        return self

    def vertical_align_bottom(self, cell_range: IRange):
        """Align the cell range vertically to the bottom."""
        self._vertical_alignments.append((cell_range, WordVerticalAlignment.wdCellAlignVerticalBottom))
        return self
    
    def vertical_align_center(self, cell_range: IRange):
        """Align the cell range vertically to the center."""
        self._vertical_alignments.append((cell_range, WordVerticalAlignment.wdCellAlignVerticalCenter))
        return self

    def horizontal_align(self, cell_range, alignment: WordParagraphAlignment):
        self._horizontal_alignments.append((cell_range, alignment))
        return self

    def horizontal_align_center(self, cell_range: IRange):
        """Align the cell range horizontally to the center."""
        self._horizontal_alignments.append((cell_range, WordParagraphAlignment.wdAlignParagraphCenter))
        return self

    def decimal_tab(self, cell_range: IRange, position):
        """position is in units of points"""
        self.decimal_tabs.append((cell_range, position))
        return self

    def style(self, word_table_style: str):
        self._style = word_table_style
        return self

    def col_width(self, col: Union[int, Column], width_inches: float):
        """Col is 1-based index of column number"""
        if isinstance(col, int):
            self._col_widths.append((col, width_inches))
        elif isinstance(col, Column):
            self._col_widths.append((col.column, width_inches))

        return self

    def col_autofit(self, col = None):
        """Autofit the column(s). If col is None, all columns are autofitted"""
        if col is None:
            for i in range(1, self.num_cols() + 1):
                self._autofits.append(i)
        elif isinstance(col, int):
            self._autofits.append(col)
        elif isinstance(col, Column):
            self._autofits.append(col.column)
        elif isinstance(col, list) or isinstance(col, range):
            for c in col:
                self.col_autofit(c)
        else:
            raise ValueError(f"Invalid column type: {type(col).__name__}")

        return self

    def center_table(self):
        """Center the table in the document (Table Properties alignment)."""
        self._table_alignment = WordParagraphAlignment.wdAlignParagraphCenter
        return self

    def obj_from_cell_range(self, cell_range: IRange):
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

    def ccllc_header(self):
        self.set_background_color(Row(1), CCLLC_BLUE)
        self.bold(Row(1), True)
        self.horizontal_align_center(Row(1))
        self.vertical_align(Row(1), WordVerticalAlignment.wdCellAlignVerticalBottom)
        return self

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


    def compile_rtf(self, standalone: bool = True) -> Union[str, RtfFragment]:
        """Compile table to RTF format.

        Args:
            standalone: If True, returns a complete RTF document string with
                headers (font table, color table). If False, returns an
                RtfFragment containing the table body and its required colors,
                which can be combined with other fragments via rtf_document().
        """
        num_rows = self.num_rows()
        num_cols = self.num_cols()

        # Collect unique colors for the color table
        colors: list[Color] = []
        color_map: dict[tuple[int, int, int], int] = {}
        for _cr, color in self._background_colors:
            key = (color.r, color.g, color.b)
            if key not in color_map:
                color_map[key] = len(colors) + 1  # 1-based; index 0 is auto
                colors.append(color)

        # Build merge maps (0-based indexing)
        # h_merge[r][c]: 'first' = start of horizontal merge, 'cont' = continuation
        # v_merge[r][c]: 'first' = start of vertical merge, 'cont' = continuation
        h_merge = [[None] * num_cols for _ in range(num_rows)]
        v_merge = [[None] * num_cols for _ in range(num_rows)]

        for sr, sc, er, ec in self._merges:
            sr0 = self.eval_row(sr) - 1
            sc0 = self.eval_col(sc) - 1
            er0 = self.eval_row(er) - 1
            ec0 = self.eval_col(ec) - 1
            for r in range(sr0, er0 + 1):
                for c in range(sc0, ec0 + 1):
                    if c == sc0:
                        if ec0 > sc0:
                            h_merge[r][c] = 'first'
                    else:
                        h_merge[r][c] = 'cont'
                    if r == sr0:
                        if er0 > sr0:
                            v_merge[r][c] = 'first'
                    else:
                        v_merge[r][c] = 'cont'

        # Column widths in twips (1 inch = 1440 twips)
        col_width_map = {col: w for col, w in self._col_widths}
        default_width = 1440
        col_widths_twips = []
        for c in range(1, num_cols + 1):
            if c in col_width_map:
                col_widths_twips.append(int(col_width_map[c] * 1440))
            else:
                col_widths_twips.append(default_width)

        # Lookup helpers for per-cell properties
        def get_bg_color_index(row1, col1):
            result = None
            for cr, color in self._background_colors:
                if _cell_in_range(cr, row1, col1, self):
                    result = color_map[(color.r, color.g, color.b)]
            return result

        def is_bold(row1, col1):
            result = False
            for cr, bold in self._bolds:
                if _cell_in_range(cr, row1, col1, self):
                    result = bold
            return result

        def get_font_size_hs(row1, col1):
            result = None
            for cr, fs in self.font_sizes:
                if _cell_in_range(cr, row1, col1, self):
                    result = int(fs * 2)  # RTF uses half-points
            return result

        def get_h_align(row1, col1):
            result = None
            for cr, alignment in self._horizontal_alignments:
                if _cell_in_range(cr, row1, col1, self):
                    result = alignment
            return result

        def get_v_align(row1, col1):
            result = None
            for cr, alignment in self._vertical_alignments:
                if _cell_in_range(cr, row1, col1, self):
                    result = alignment
            return result

        # Padding in twips
        def pad_twips(inches):
            return int(inches * 1440) if inches is not None else None

        lpad = pad_twips(self._left_padding)
        rpad = pad_twips(self._right_padding)
        tpad = pad_twips(self._top_padding)
        bpad = pad_twips(self._bottom_padding)

        # Build RTF rows
        lines = []

        for r in range(num_rows):
            row_def = '\\trowd\\trgaph108'

            # Row-level padding
            if lpad is not None:
                row_def += f'\\trpaddl{lpad}\\trpaddfl3'
            if rpad is not None:
                row_def += f'\\trpaddr{rpad}\\trpaddfr3'
            if tpad is not None:
                row_def += f'\\trpaddt{tpad}\\trpaddft3'
            if bpad is not None:
                row_def += f'\\trpaddb{bpad}\\trpaddfb3'

            # Table alignment
            if self._table_alignment == WordParagraphAlignment.wdAlignParagraphCenter:
                row_def += '\\trqc'
            elif self._table_alignment == WordParagraphAlignment.wdAlignParagraphRight:
                row_def += '\\trqr'

            # Row-level borders
            if self._borders:
                bdr = '\\brdrs\\brdrw10'
                row_def += f'\\trbrdrt{bdr}\\trbrdrb{bdr}\\trbrdrl{bdr}\\trbrdrr{bdr}'

            # Determine visible columns and their cellx right-edge positions.
            # For horizontally merged cells, the first cell's cellx must be at the
            # right edge of the last continuation column.
            visible_cols = []
            visible_cellx = []
            cellx_pos = 0
            for c in range(num_cols):
                cellx_pos += col_widths_twips[c]
                if h_merge[r][c] != 'cont':
                    visible_cols.append(c)
                    visible_cellx.append(cellx_pos)
                else:
                    # Continuation: extend the previous visible cell's right edge
                    visible_cellx[-1] = cellx_pos

            # Cell definitions (only for visible columns)
            for i, c in enumerate(visible_cols):
                cell_props = ''

                # Vertical alignment
                va = get_v_align(r + 1, c + 1)
                if va == WordVerticalAlignment.wdCellAlignVerticalCenter:
                    cell_props += '\\clvertalc'
                elif va == WordVerticalAlignment.wdCellAlignVerticalBottom:
                    cell_props += '\\clvertalb'

                # Vertical merge
                if v_merge[r][c] == 'first':
                    cell_props += '\\clvmgf'
                elif v_merge[r][c] == 'cont':
                    cell_props += '\\clvmrg'

                # Cell borders
                if self._borders:
                    bdr = '\\brdrs\\brdrw10'
                    cell_props += f'\\clbrdrt{bdr}\\clbrdrb{bdr}\\clbrdrl{bdr}\\clbrdrr{bdr}'

                # Horizontal cell margin
                if self._horizontal_cell_margin is not None:
                    hm = int(self._horizontal_cell_margin * 1440)
                    cell_props += f'\\clpadl{hm}\\clpadfl3\\clpadr{hm}\\clpadfr3'

                # Background color
                ci = get_bg_color_index(r + 1, c + 1)
                if ci is not None:
                    cell_props += f'\\clcbpat{ci}'

                row_def += f'{cell_props}\\cellx{visible_cellx[i]}'

            lines.append(row_def)

            # Cell contents (only for visible columns)
            for c in visible_cols:
                content = '\\pard\\intbl\\sa0\\keepn'

                # Paragraph alignment
                ha = get_h_align(r + 1, c + 1)
                if ha == WordParagraphAlignment.wdAlignParagraphCenter:
                    content += '\\qc'
                elif ha == WordParagraphAlignment.wdAlignParagraphRight:
                    content += '\\qr'
                elif ha == WordParagraphAlignment.wdAlignParagraphJustify:
                    content += '\\qj'

                content += ' '

                # Character formatting
                bold = is_bold(r + 1, c + 1)
                if bold:
                    content += '\\b '

                fs = get_font_size_hs(r + 1, c + 1)
                if fs is not None:
                    content += f'\\fs{fs} '

                # Cell text
                if r < len(self.data) and c < len(self.data[r]):
                    cell_val = self.data[r][c]
                    if isinstance(cell_val, str):
                        content += _rtf_escape(cell_val)
                    elif isinstance(cell_val, TextRun):
                        content += _rtf_escape(cell_val.text)
                    elif isinstance(cell_val, list):
                        for tr in cell_val:
                            content += _rtf_escape(tr.text)

                if bold:
                    content += '\\b0'

                content += '\\cell'
                lines.append(content)

            lines.append('\\row')

        table_rtf = '\n'.join(lines)

        if standalone:
            font_name = self._font_name or 'Calibri'
            fonttbl = '{\\fonttbl{\\f0 ' + font_name + ';}}'
            colortbl = '{\\colortbl ;'
            for color in colors:
                colortbl += f'\\red{color.r}\\green{color.g}\\blue{color.b};'
            colortbl += '}'

            return '{\\rtf1\\ansi\\deff0\n' + fonttbl + '\n' + colortbl + '\n' + table_rtf + '\n}'
        else:
            return RtfFragment(body=table_rtf, colors=colors, font_name=self._font_name)

    def compile(self) -> str:
        """Compile table information into the required Word VBA"""
        lines = []
        lines.append("Dim tbl As Table")
        lines.append(f'Set tbl = ActiveDocument.Tables.Add(Range:=Selection.Range, NumRows:={self.num_rows()}, NumColumns:={self.num_cols()}, DefaultTableBehavior:=wdWord9TableBehavior, AutoFitBehavior:=wdAutoFitFixed)')

        if self._style:
            lines.append(f'tbl.Style = "{self._style}"') # Probably need some escaping here
        if self._table_alignment is not None:
            lines.append(f'tbl.Range.ParagraphFormat.Alignment = {self._table_alignment}')

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

        if self._font_name is not None:
            lines.append(f'tbl.Range.Font.Name = "{self._font_name}"')

        for cell_range, font_size in self.font_sizes:
            lines.append(f'{self.obj_from_cell_range(cell_range)}.Range.Font.Size = {font_size}')

        for i, row in enumerate(self.data):
            statements = []
            for j, cell in enumerate(row):
                # If cell is str, then do Range.Text. If cell is list of TextRun, then print out the vba for those, else throw
                if isinstance(cell, str):
                    statements.append(f'tbl.Cell({i+1}, {j+1}).Range.Text = {escape_string(cell)}')
                elif isinstance(cell, TextRun):
                    # If cell is a TextRun, then we need to apply the text run properties
                    statements.append(f'tbl.Cell({i+1}, {j+1}).Range.Select')
                    statements.extend(cell.vba())
                elif isinstance(cell, list):
                    # If cell is a list of TextRun, then we need to apply each text run
                    statements.append(f'tbl.Cell({i+1}, {j+1}).Range.Select')
                    for text_run in cell:
                        statements.extend(text_run.vba())
                else:
                    raise ValueError(f"Unsupported cell type: {type(cell).__name__}")

            # statements = [f'tbl.Cell({i+1}, {j+1}).Range.Text = {escape_string(cell)}' for j, cell in enumerate(row)]
            joined = " : ".join(statements)

            # Too lazy to make this dynamic
            if len(joined) > 1000:
                group1 = statements[0:len(statements) // 2]
                group2 = statements[len(statements) // 2:]
                joined1 = " : ".join(group1)
                joined2 = " : ".join(group2)
                lines.append(joined1)
                lines.append(joined2)
            else:
                lines.append(joined)

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
        
        lines.append('tbl.Range.ParagraphFormat.SpaceBeforeAuto = True')
        lines.append('tbl.Range.ParagraphFormat.SpaceAfterAuto = True')
        lines.append('tbl.Range.ParagraphFormat.KeepWithNext = True')


        if self._col_widths:
            # Clear 'PreferredWidth on table width. Remove AllowAutoFit
            lines.append('tbl.PreferredWidthType = wdPreferredWidthAuto')
            lines.append('tbl.PreferredWidth = 0')
            lines.append('tbl.AllowAutoFit = False')


        if self._borders is not None:
            if self._borders:
                lines.append('tbl.Borders.Enable = True')
            else:
                lines.append('tbl.Borders.Enable = False')

        if self._horizontal_cell_margin is not None:
            lines.append(f'tbl.LeftPadding = InchesToPoints({self._horizontal_cell_margin})')
            lines.append(f'tbl.RightPadding = InchesToPoints({self._horizontal_cell_margin})')

        if self._left_padding is not None:
            lines.append(f'tbl.LeftPadding = InchesToPoints({self._left_padding})')

        if self._right_padding is not None:
            lines.append(f'tbl.RightPadding = InchesToPoints({self._right_padding})')

        if self._top_padding is not None:
            lines.append(f'tbl.TopPadding = InchesToPoints({self._top_padding})')

        if self._bottom_padding is not None:
            lines.append(f'tbl.BottomPadding = InchesToPoints({self._bottom_padding})')


        for i in range(1, self._header_repeat_rows + 1):
            lines.append(f'tbl.Rows({i}).HeadingFormat = True')

        # Auto fit before merges, otherwise you get hit with an error.
        for col in self._autofits:
            lines.append(f'tbl.Columns({col}).AutoFit')

        for col, width in self._col_widths:
            lines.append(f'tbl.Columns({col}).Width = InchesToPoints({width})')

        # Do merge from bottom right to left top because otherwise it all gets mangled.
        sorted_merges = sorted(self._merges, key=lambda x: (x[1], x[0]), reverse=True)
        for merge in sorted_merges:
            start_row = merge[0] if merge[0] > 0 else self.num_rows() + merge[0] + 1 # 1-based index
            start_col = merge[1] if merge[1] > 0 else self.num_cols() + merge[1] + 1 # 1-based index
            end_row = merge[2] if merge[2] > 0 else self.num_rows() + merge[2] + 1 # 1-based index
            end_col = merge[3] if merge[3] > 0 else self.num_cols() + merge[3] + 1

            lines.append(f'tbl.Cell({start_row}, {start_col}).Merge MergeTo:=tbl.Cell({end_row}, {end_col})')

        if self._col_widths:
            lines.append('tbl.AllowAutoFit = True')

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
    i = 1
    while i < len(sys.argv):
        a = sys.argv[i]
        i += 1

        if a == '--test':
            test()
            sys.exit(0)
        elif a == '-h' or a == '--help':
            print(f"Usage: word_vba.py --test")
            print(f"       word_vba.py < TSV_DATA")
            sys.exit(0)

    # Else read in TSV data, and print a default table
    table = Table()
    data = [line.split("\t") for line in sys.stdin.read().splitlines()]
    table.set_data(data)
    table.bold(Row(1), True).set_background_color(Row(1), CCLLC_BLUE).col_autofit()

    print(table.compile())
