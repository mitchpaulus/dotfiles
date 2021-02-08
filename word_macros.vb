
Sub AutoFitTables()

    Dim tbl As Table

    For Each tbl In ActiveDocument.Tables
        tbl.AutoFitBehavior wdAutoFitContent
    Next tbl

End Sub

Sub CCLLCFigures()
    Dim pgh As Paragraph

    For Each pgh In ActiveDocument.Paragraphs
        ' Images are part of the "InlineShapes"
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
' This routine adds a new Figure caption, including period and space.
'
' Typically bound to Alt-c
'
'
    Selection.InsertCaption Label:="Figure", TitleAutoText:="InsertCaption1", _
        Title:="", Position:=wdCaptionPositionBelow, ExcludeLabel:=0
    Selection.TypeText Text:=". "
End Sub

Sub TableCaption()
' This routine adds a new Table caption, including period and space.
'
' Typically bound to Alt-t
'
'
    Selection.InsertCaption Label:="Table", TitleAutoText:="InsertCaption1", _
        Title:="", Position:=wdCaptionPositionAbove, ExcludeLabel:=0
    Selection.TypeText Text:=". "
End Sub

Sub UpdateCaptionStyling()
' This procedure searches through paragrpahs for those that have the
' default "Caption" style. It then checks for the word "Figure" or "Table" in
' text of that paragraph to apply a more specific caption style for either
' Figures or Tables. This is important, as usually tables have the caption placed above
' and figures have the caption placed below. The "Spacing After" property should be
' small for the table, and larger for the figure.

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
' Typically bound to Alt-o

Dim TableNumber As String
Dim TrimmedTableNubmer As String

TableNumber = Selection.Text

TrimmedTableNumber = Trim(TableNumber)


Selection.InsertCrossReference ReferenceType:="Table", ReferenceKind:= _
        wdOnlyLabelAndNumber, ReferenceItem:=TrimmedTableNumber, InsertAsHyperlink:=True, _
        IncludePosition:=False, SeparateNumbers:=False, SeparatorString:=" "

End Sub

Sub CrossReferenceFigure()
'
' This macro allows for fast cross referencing of figures
' USAGE:
'   Type number of figure, select/highlight it
'   Run this macro
'
' Typically bound to Alt-d (for [d]iagram)

Dim Number As String

FigureNumber = Selection.Text

Selection.InsertCrossReference ReferenceType:="Figure", ReferenceKind:= _
        wdOnlyLabelAndNumber, ReferenceItem:=FigureNumber, InsertAsHyperlink:=True, _
        IncludePosition:=False, SeparateNumbers:=False, SeparatorString:=" "

End Sub


Sub FixSectionNumbering()
'
' By default, Word has the inane behavior to restart page numbering
' on every section break.
'

Dim Section As Section
Dim Footer As HeaderFooter

For Each Section In ActiveDocument.Sections
    For Each Footer In Section.Footers

        Footer.PageNumbers.RestartNumberingAtSection = False

    Next Footer
Next Section

End Sub

Sub GenTable()
' Bound to CTRL-SHIFT-T
    Selection.ConvertToTable Separator:=wdSeparateByTabs, AutoFitBehavior:=wdAutoFitContent, AutoFit:=True
     With Selection.Tables(1)
        .Style = "ccxtable"
    End With
End Sub

