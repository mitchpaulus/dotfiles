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
