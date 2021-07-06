# Excel VBA

```vb
Range("A1:C1")
Range("NamedRange")
Workbooks("File.xlsx").Worksheets("Sheet 1").Range("A1")
Range("3:3")
Range("D:D")
Range("A1:B2,D1:E2") ' Non contiguous

Cells(1, 2)
Worksheets("Sheet 1").Cells(row, col)

' Range object Properties
Value
Text
Count
Address
HasFormula
Font -> Object
Interior -> Object
Formula
NumberFormat
' Range object methods
Select
Copy
Paste
Clear
Delete
```
