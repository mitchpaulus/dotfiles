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
            If InStr(tbl.Cell(1, 1).Range.text, "Field") Or InStr(tbl.Cell(1, 1).Range.text, "Test") Then
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
    Selection.TypeText text:=". "
End Sub

Sub TableCaption()
' This routine adds a new Table caption, including period and space.
'
' Typically bound to Alt-t
'
'
    Selection.InsertCaption Label:="Table", TitleAutoText:="InsertCaption1", _
        Title:="", Position:=wdCaptionPositionAbove, ExcludeLabel:=0
    Selection.TypeText text:=". "

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

        ' Caption is default style, "Image Caption" is from pandoc generated figure captions, "Table Caption" for pandoc generated tables
        If pgh.Style = "Caption" Or pgh.Style = "Image Caption" Or pgh.Style = "Table Caption" Then

            If InStr(pgh.Range.text, "Figure") Then
                pgh.Style = "figure-caption"
            ElseIf InStr(pgh.Range.text, "Table") Then
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

TableNumber = Selection.text

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

FigureNumber = Selection.text

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

Sub ReplaceFigureCaptions()
'
' This macro is for replacing the "dumb" captions coming
' from a pandoc generated file.
' IMPORTANT: The only way this works is by having a Figure caption
' in the clipboard, relying on the ^c
'

    Selection.Find.ClearFormatting
    Selection.Find.Style = ActiveDocument.Styles("Image Caption")
    With Selection.Find
        .text = "Figure [0-9]{1,}:"
        .Replacement.text = "^c"
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchAllWordForms = False
        .MatchSoundsLike = False
        .MatchWildcards = True
    End With
    Selection.Find.Execute Replace:=wdReplaceAll


End Sub

Sub ReplaceTableCaptions()
'
' This macro is for replacing the "dumb" captions coming
' from a pandoc generated file.
' IMPORTANT: The only way this works is by having a Table caption
' in the clipboard, relying on the ^c
'

    Selection.Find.ClearFormatting
    Selection.Find.Style = ActiveDocument.Styles("Table Caption")
    With Selection.Find
        .text = "Table [0-9]{1,}:"
        .Replacement.text = "^c"
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchAllWordForms = False
        .MatchSoundsLike = False
        .MatchWildcards = True
    End With
    Selection.Find.Execute Replace:=wdReplaceAll


End Sub

Sub Level1AlphabeticStart()
'
' Level1Alphabetic Macro
'
'
    Selection.Fields.Add Range:=Selection.Range, Type:=wdFieldEmpty, _
        PreserveFormatting:=False
    Selection.TypeText text:="seq level1 \r 1 \* ALPHABETIC"
    Selection.Fields.Update
    Selection.MoveRight Unit:=wdCharacter, Count:=1
    Selection.TypeText text:="." & vbTab
End Sub

Sub Level1AlphabeticNext()
    Selection.Fields.Add Range:=Selection.Range, Type:=wdFieldEmpty, PreserveFormatting:=False
    Selection.TypeText text:="seq level1 \* ALPHABETIC"
    Selection.Fields.Update
    Selection.MoveRight Unit:=wdCharacter, Count:=1
    Selection.TypeText text:="." & vbTab
End Sub

Sub Level2Start()
    Selection.Fields.Add Range:=Selection.Range, Type:=wdFieldEmpty, PreserveFormatting:=False
    Selection.TypeText text:="seq level2 \r 1"
    Selection.Fields.Update
    Selection.MoveRight Unit:=wdCharacter, Count:=1
    Selection.TypeText text:="." & vbTab
End Sub

Sub Level2Next()
    Selection.Fields.Add Range:=Selection.Range, Type:=wdFieldEmpty, PreserveFormatting:=False
    Selection.TypeText text:="seq level2"
    Selection.Fields.Update
    Selection.MoveRight Unit:=wdCharacter, Count:=1
    Selection.TypeText text:="." & vbTab
End Sub


Sub LevelN(levelNum As String, isStart As Boolean)
'
' Level1Alphabetic Macro
    Selection.Fields.Add Range:=Selection.Range, Type:=wdFieldEmpty, _
        PreserveFormatting:=False
    If isStart Then
        Selection.TypeText text:="seq level" & levelNum & " \r 1"
    Else
        Selection.TypeText text:="seq level" & levelNum
    End If

    Selection.Fields.Update
    Selection.MoveRight Unit:=wdCharacter, Count:=1
    Selection.TypeText text:="." & vbTab
End Sub

Sub Level3Start()
    Call LevelN("3", True)
End Sub
Sub Level3Next()
    Call LevelN("3", False)
End Sub
Sub Level4Start()
    Call LevelN("4", True)
End Sub
Sub Level4Next()
    Call LevelN("4", False)
End Sub
Sub Level5Start()
    Call LevelN("5", True)
End Sub
Sub Level5Next()
    Call LevelN("5", False)
End Sub

Sub TocPrint()
    Dim pgh As Paragraph
    Dim text As String

    For Each pgh In ActiveDocument.Paragraphs
        If pgh.Style = "Heading 1" Then
            ' Remove final newline character
            text = text.Substring(0, text.Length - 1)
            text = Trim(pgh.Range.text)
            text = text & vbTab & pgh.Range.Information(wdActiveEndPageNumber) & vbLf
            Selection.InsertAfter (text)
        End If
    Next pgh
End Sub

Sub Heading1Num()
    ActiveDocument.Fields.Add Selection.Range, wdFieldSequence, "h1", False
    Selection.TypeText ". "
End Sub

Sub Heading2Num()
    ActiveDocument.Fields.Add Selection.Range, wdFieldSequence, "h1 \c", False
    Selection.TypeText "."
    ActiveDocument.Fields.Add Selection.Range, wdFieldSequence, "h2 \s 1", False
    Selection.TypeText ". "
End Sub

Sub Heading3Num()
    ActiveDocument.Fields.Add Selection.Range, wdFieldSequence, "h1 \c", False
    Selection.TypeText "."
    ActiveDocument.Fields.Add Selection.Range, wdFieldSequence, "h2 \c", False
    Selection.TypeText "."
    ActiveDocument.Fields.Add Selection.Range, wdFieldSequence, "h3 \s 2", False
    Selection.TypeText ". "
End Sub

Sub Heading4Num()
    ActiveDocument.Fields.Add Selection.Range, wdFieldSequence, "h1 \c", False
    Selection.TypeText "."
    ActiveDocument.Fields.Add Selection.Range, wdFieldSequence, "h2 \c", False
    Selection.TypeText "."
    ActiveDocument.Fields.Add Selection.Range, wdFieldSequence, "h3 \c", False
    Selection.TypeText "."
    ActiveDocument.Fields.Add Selection.Range, wdFieldSequence, "h4 \s 3", False
    Selection.TypeText ". "
End Sub

Sub RemoveHeaderNumbering()
    ActiveDocument.Styles("Heading 1").LinkToListTemplate ListTemplate:=Nothing
    ActiveDocument.Styles("Heading 2").LinkToListTemplate ListTemplate:=Nothing
    ActiveDocument.Styles("Heading 3").LinkToListTemplate ListTemplate:=Nothing
    ActiveDocument.Styles("Heading 4").LinkToListTemplate ListTemplate:=Nothing
    ActiveDocument.Styles("Heading 5").LinkToListTemplate ListTemplate:=Nothing
End Sub

Sub AddSooLevelStyle(Level As Integer, HangingIndent As Single, LeftIndent As Single)

    Dim Style As Style
    LevelName = "Level" & CStr(Level) & "SOO"

    On Error GoTo AddStyle
    Set Style = ActiveDocument.Styles(LevelName)
AddStyle:
    Set Style = ActiveDocument.Styles.Add(Name:=LevelName, Type:=wdStyleTypeParagraph)
    On Error GoTo 0


    Style.ParagraphFormat.LeftIndent = InchesToPoints((Level - 1) * LeftIndent + HangingIndent)
    Style.ParagraphFormat.FirstLineIndent = InchesToPoints(-HangingIndent)
    Style.ParagraphFormat.TabStops.Add Position:=InchesToPoints((Level - 1) * LeftIndent + HangingIndent), Alignment:=wdAlignTabLeft, Leader:=wdTabLeaderSpaces
    Style.QuickStyle = True
End Sub


Sub AddSooStyles()
    Dim HangingIndent As Single
    Dim LeftIndent As Single

    HangingIndent = 0.2
    LeftIndent = 0.25

    AddSooLevelStyle 1, HangingIndent, LeftIndent
    AddSooLevelStyle 2, HangingIndent, LeftIndent
    AddSooLevelStyle 3, HangingIndent, LeftIndent
    AddSooLevelStyle 4, HangingIndent, LeftIndent
    AddSooLevelStyle 5, HangingIndent, LeftIndent
    AddSooLevelStyle 6, HangingIndent, LeftIndent


End Sub

Sub DeleteSooLevelStyle(Level As Integer)
    On Error Resume Next
    LevelName = "Level" & CStr(Level) & "SOO"
    ActiveDocument.Styles(LevelName).Delete
End Sub


Sub DeleteSooStyles()
    DeleteSooLevelStyle 1
    DeleteSooLevelStyle 2
    DeleteSooLevelStyle 3
    DeleteSooLevelStyle 4
    DeleteSooLevelStyle 5
    DeleteSooLevelStyle 6
End Sub


Sub UpdateDates()
    InsertDateInExistingTableInHeaders
    ReplaceDateOnFirstPageUsingLoopNoRegex
End Sub

Sub InsertDateInExistingTableInHeaders()

    Dim oSection As Section
    Dim oHeader As HeaderFooter
    Dim oTable As Table
    Dim currentDate As String

    ' Format the current date as YYYY-MM-DD
    currentDate = Format(Now, "yyyy-mm-dd")

    For Each oSection In ActiveDocument.Sections
        For Each oHeader In oSection.Headers
            ' Skip first page headers
            If oHeader.Index <> wdHeaderFooterFirstPage Then
                If oHeader.Range.Tables.Count > 0 Then
                    ' Access the existing table
                    Set oTable = oHeader.Range.Tables(1)

                    ' Insert the current date in the first row, first column
                    oTable.Cell(1, 1).Range.text = currentDate
                End If
            End If
        Next oHeader
    Next oSection

End Sub

Sub ReplaceDateOnFirstPageUsingLoopNoRegex()

    Dim oPara As Paragraph
    Dim currentDate As String
    Dim monthName As String
    Dim monthList(1 To 12) As String
    Dim i As Integer
    Dim foundDate As Boolean

    ' Define the list of months
    monthList(1) = "January"
    monthList(2) = "February"
    monthList(3) = "March"
    monthList(4) = "April"
    monthList(5) = "May"
    monthList(6) = "June"
    monthList(7) = "July"
    monthList(8) = "August"
    monthList(9) = "September"
    monthList(10) = "October"
    monthList(11) = "November"
    monthList(12) = "December"

    ' Format the current date
    currentDate = Format(Now, "MMMM d, yyyy")

    foundDate = False

    For Each oPara In ActiveDocument.Paragraphs
        ' Check if the paragraph is on the second page or beyond
        If oPara.Range.Information(wdActiveEndAdjustedPageNumber) > 1 Then
            Exit For
        End If

        ' Check if the paragraph text contains a month name
        For i = LBound(monthList) To UBound(monthList)
            monthName = monthList(i)
            If InStr(1, oPara.Range.text, monthName, vbTextCompare) > 0 Then
                ' Create a range that excludes the last character (paragraph mark)
                Set rangeWithoutParaMark = oPara.Range
                rangeWithoutParaMark.MoveEnd wdCharacter, -1

                ' Replace the range text without the paragraph mark
                rangeWithoutParaMark.text = currentDate

                foundDate = True
                Exit For
            End If
        Next i

        ' Exit the loop if the date has been found
        If foundDate Then
            Exit For
        End If
    Next oPara

End Sub
