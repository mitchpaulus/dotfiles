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
Left("string", 2) = 2
```

## Parenthesis

- <https://learn.microsoft.com/en-us/office/vba/language/concepts/getting-started/using-parentheses-in-code>
- <https://stackoverflow.com/questions/5413765/what-are-the-rules-governing-usage-of-parenthesis-in-vba-function-calls>

If return value is not used, do not use parenthesis.

## Write vs. Print

Print is what I would expect, write literally what I tell it to.
Write will make you what pass it into a CSV form. If that's what you're into.
In actuality it's more for compatibility with the corresponding `Input` function.
<https://wellsr.com/vba/2016/excel/vba-write-to-text-file-print-statement/>

On the text file encoding: <https://stackoverflow.com/questions/40376951/which-string-encoding-do-the-vba-built-in-file-operations-use>
By default looks like Windows-1252.
