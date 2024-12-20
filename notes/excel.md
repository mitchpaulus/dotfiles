# Excel

## Pitfalls when copying text to Excel
 - Excel will use current settings from 'Data to Columns' dialog
 - Excel will use quotes to escape your delimited string.
    - You can escape the quote character by using 3 quotes `"""`
    - This bit me on points dump from Andover where units have '"w.g.'
      as a unit.

## Move entire rows with mouse

[From link](https://trumpexcel.com/move-rows-columns/)

1. Make selection
2. Hold Shift
3. Click and drag when your have 4 directional arrow (✥)


## Listing all Keybindings

[Turns out this is not easy](https://stackoverflow.com/questions/16862306/excel-vba-to-list-key-bindings-onkey)

## Key Shortcuts

Delete: Ctrl-(minus)
Delete Row: Shift-Spacebar, Ctrl-(minus)
Insert Row: ALT-i, r
Insert, move right: CTRL-+ (or CTRL-SHIFT-=)
Insert Column: Shift-Spacebar, CTRL-+
Insert Column: ALT-i, c

For inserting row, typically use 'SHIFT-<Space>, then <CTRL-SHIFT++>'

## Default Encoding

The default encoding for CSV files is Windows-1252. Close to, but not
exactly the same as ISO-8859-1 (Latin alphabet no. 1).

In LaTeX packages, CP-1252 is referred to as "ansinew".

Converting to/from

```sh
 iconv -f WINDOWS-1252 -t UTF-8 filename.txt
```

## String Contains

Source: [https://exceljet.net/formula/cell-contains-specific-text](https://exceljet.net/formula/cell-contains-specific-text)

```
=ISNUMBER(SEARCH(substring, text))
```

## String Splitting

Typically use combination of `LEFT`, `RIGHT`, `MID`, and `SEARCH`.

## Delete Pivot Table

1. Click in Pivot Table
2. On Ribbon, Analyze -> Select -> Entire Pivot Table
3. Press Delete.

## Copying Data to New XY Series

If shared X-Axis, can copy columns directly onto plot. Else, Copy the 2
columns, click on chart, Paste Special.

- Set 'Add cells as': to 'New Series'
- Make sure 'Categories (X Values) in First Column


## Dynamic Range for Pivot Table

- Make sure that it's a fully absolute range in the `INDIRECT` function.
  - Like, sheet name and everything: `Sheet1!$A$1:$B$2`

## Dynamic arrays reference total range

- Can use upper left cell with '#' after to get reference to entire array dynamically.

## Set Difference

IF(
    NOT(
         IFNA(
             MATCH(A2,$B$2:$B$42,0)
             ,FALSE
             )
       ),
    IF(A2,A2,""),
    ""
)

## Custom Sorting in Pivot Table

<https://www.extendoffice.com/documents/excel/2025-excel-pivot-table-sort-custom-list.html>

## MySQL in Excel

Needed to get both the 64-bit OBDC driver and the 32-bit ADO.NET driver.
Not sure which versions were the ones that actually worked, since I installed a whole bunch.

[ADO.NET](https://downloads.mysql.com/archives/c-net/)
[ODBC](https://downloads.mysql.com/archives/c-odbc/)
