
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
            If InStr(tbl.Cell(1, 1).Range.Text, "Field") Or InStr(tbl.Cell(1, 1).Range.Text, "Test") Then
                tbl.Style = "ccxtable"
            End If
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


Sub SelectColumn()
'
' Macro2 Macro
'
'
    Selection.SelectColumn
End Sub

Sub CrossReferenceTable()
'
' This macro allows for fast cross referencing of tables
' USAGE:
'   Type number of table, select/highlight it
'   Run this macro
'

Dim Number As String

TableNumber = Selection.Text

Selection.InsertCrossReference ReferenceType:="Table", ReferenceKind:= _
        wdOnlyLabelAndNumber, ReferenceItem:=TableNumber, InsertAsHyperlink:=True, _
        IncludePosition:=False, SeparateNumbers:=False, SeparatorString:=" "

End Sub

Sub CrossReferenceFigure()
'
' This macro allows for fast cross referencing of figures
' USAGE:
'   Type number of figure, select/highlight it
'   Run this macro
'

Dim Number As String

FigureNumber = Selection.Text

Selection.InsertCrossReference ReferenceType:="Figure", ReferenceKind:= _
        wdOnlyLabelAndNumber, ReferenceItem:=FigureNumber, InsertAsHyperlink:=True, _
        IncludePosition:=False, SeparateNumbers:=False, SeparatorString:=" "

End Sub

