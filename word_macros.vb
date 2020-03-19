

Sub AutoFitTables()

    Dim tbl As Table

    For Each tbl In ActiveDocument.Tables
        tbl.AutoFitBehavior wdAutoFitContent
    Next tbl

End Sub

Sub CCLLCFigures()


    Dim pgh As Paragraph

    For Each pgh In ActiveDocument.Paragraphs

        If pgh.Range.InlineShapes.Count > 0 Then

            pgh.Style = "CCLLC Figure"

        End If


    Next pgh


End Sub

Sub CCLLCTables()

    Dim tbl As Table

    For Each tbl In ActiveDocument.Tables
            tbl.Style = "ccxtable"
    Next tbl



End Sub

Sub FigureCaption()
'
' FigureCaption Macro
'
'
    Selection.InsertCaption Label:="Figure", TitleAutoText:="InsertCaption1", _
        Title:="", Position:=wdCaptionPositionBelow, ExcludeLabel:=0
    Selection.TypeText Text:=". "
End Sub

Sub TableCaption()
'
' TableCaption Macro
'
'
    Selection.InsertCaption Label:="Table", TitleAutoText:="InsertCaption1", _
        Title:="", Position:=wdCaptionPositionAbove, ExcludeLabel:=0
    Selection.TypeText Text:=". "
End Sub

Sub UpdateCaptionStyling()


    Dim pgh As Paragraph

    For Each pgh In ActiveDocument.Paragraphs

        If pgh.Style = "Caption" Then

            If InStr(pgh.Range.Text, "Figure") Then
                pgh.Style = "figure-caption"
            ElseIf InStr(pgh.Range.Text, "Table") Then
                pgh.Style = "table-caption"
            End If
        End If
    Next pgh


End Sub

Sub ClearExistingTableFormats()

    Dim tbl As Table

    For Each tbl In ActiveDocument.Tables
            tbl.Select
            Selection.ClearFormatting
    Next tbl
End Sub

Sub ListCustomKeyBindings()

    CustomizationContext = NormalTemplate

    For Each aKey In KeyBindings
     Selection.InsertAfter aKey.Command & vbTab & aKey.KeyString & vbCr
     Selection.Collapse Direction:=wdCollapseEnd
    Next aKey

End Sub



