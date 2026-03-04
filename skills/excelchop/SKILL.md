---
name: 'excelchop'
description: |
  `excelchop` is a CLI utility that I have written. It's purpose is to be able to get data out of Excel files out to standard output to
  then be used with traditional shell utilities and pipelines.
---

`excelchop` is a CLI utility that I have written. It's purpose is to be able to get data out of Excel files out to standard output to
then be used with traditional shell utilities and pipelines.

Here is the usage help:

Usage: excelchop [options...] excel_file

Options:
        --sigfigs <sigfigs>         Integer significant figures for numeric cells. Default is to print using current excel format.
        --all-sheets                Extract data from all sheets in the Workbook
        --no-strip                  Don't strip whitespace from beginning and end of cell contents
        --csv                       Output in RFC 4180 CSV format (UTF-8)
    -A  --all-fields-all-blank      Stop reading when all fields in complete range are blank before stopping.
    -D  --dateformat <dateformat>   Output format for date cells, .NET style [yyyy-MM-dd]
    -S  --stop-any <stop-any>       Stop reading when any columns specified are empty. Specify columns as comma separated list.
    -d  --delim <delim>             Output field delimiter [tab]
    -e  --escape                    Escape newlines with '\n' characters
    -h  --help                      Show help and exit
    -i  --in-place                  Write to .tsv with same name as input xlsx file rather than standard output
    -p  --print <print>             Print information about workbook. w = worksheet names
    -r  --range <range>             Specify range (A1:B2 or 2:A:B style) [A1:B10]
    -s  --stop-all <stop-all>       Stop reading when all columns specified are empty. Specify columns as comma separated list.
    -v  --version                   Show version and exit
    -w  --sheet <sheet>             Worksheet name [first sheet]

excelchop extracts data out of Microsoft Excel files and sends it to
standard output. From here, you can pipe the data through other filters
to achieve your goals.

By default, excelchop will return all the data within the first
worksheet. Using the '-r' option, you can specify a subset range. You
can either specify the range like

excelchop -r A1:B10 excelfile.xlsx

or you can allow excelchop to automatically find the last row. You can
use the special range syntax 'startrow:startcolumn:endcolumn'.

excelchop -r 2:A:D excelfile.xlsx

This will start at row 2, extracting data from columns A to D, stopping
once it reaches a row in which ANY of the values are empty or
whitespace. You can use the options -A, -s, or -S, to change this
stopping behavior.

The default delimiter is a tab character and output records are
separated by a Unix newline. excelchop also removes any newline
characters within a field.

## Getting the names of all the worksheets

```sh
excelchop -p w myfile.xlsx
```
