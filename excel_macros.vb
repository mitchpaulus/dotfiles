Sub CommandHeader()
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .Color = 8866048
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With

    Selection.Font.Color = RGB(255, 255, 255)
    Selection.Font.Bold = True
End Sub


Sub FormatThousands()
    Selection.NumberFormat = "#,##0"
End Sub
