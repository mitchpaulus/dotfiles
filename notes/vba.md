# VBA Visual Basic for Applications

VBA doesn't have short circuiting logic operators. This saddens me.
[link](https://nolongerset.com/short-circuiting-vba/).

```vba
Dim Variable as Type
```

```vba
For i = 0 to N
Next i

For Each Item in Collection

Next Item

If Something = Other Then

End If
```

Writing to a file:

[Open Statement](https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/open-statement)

Modes = Append Binary Input Output Random
Access = Read, Write, Read Write

`Open pathname For mode [ Access access ] [ lock ] As [ # ] filenumber [ Len = reclength ]`

```vba
FileNum = FreeFile
Open "C:\Users\mpaulus\properties.txt" For Output As #FileNum
' Print is an append
Print #FileNum, Output
Close #FileNum
```

Variable Types: `VarType`: <https://docs.microsoft.com/en-us/office/vba/Language/Reference/user-interface-help/vartype-function>


```vba
MsgBox "String"

"String" & "Concatenation"

' String constants
vbCrLf ' Chr(13) + Chr(10)
vbTab  ' Chr(9)

Trim("String   ") ' "String"

Len("String") = 6
Left("string", 2) = "st"
```

## Parenthesis

- <https://learn.microsoft.com/en-us/office/vba/language/concepts/getting-started/using-parentheses-in-code>
- <https://stackoverflow.com/questions/5413765/what-are-the-rules-governing-usage-of-parenthesis-in-vba-function-calls>

If return value is not used, do not use parenthesis.

Use `:=` syntax for named parameters, otherwise, just separate with commas.

## Write vs. Print

Print is what I would expect, write literally what I tell it to.
Write will make you what pass it into a CSV form. If that's what you're into.
In actuality it's more for compatibility with the corresponding `Input` function.
<https://wellsr.com/vba/2016/excel/vba-write-to-text-file-print-statement/>

On the text file encoding: <https://stackoverflow.com/questions/40376951/which-string-encoding-do-the-vba-built-in-file-operations-use>
By default looks like Windows-1252.

## Error Handling

From [Here](ErrorHandling):

> The Err object is automatically reset when either a Resume, Exit Sub, Exit Function, Exit Property, or On Error statement is executed.

[ErrorHandling]: https://www.oreilly.com/library/view/vb-vba/1565923588/1565923588_ch07-677-fm2xml.html#:~:text=The%20Err%20object%20is%20automatically,On%20Error%20statement%20is%20executed.

## Break/Continue

```vba
' Break
For Each Item in Collection
    If Item = "Something" Then
        Exit For
    End If
Next Item

' Continue
For Each Item in Collection
    If Item = "Something" Then
        GoTo Continue
    End If
    ' Do something
Continue:
Next Item
```
