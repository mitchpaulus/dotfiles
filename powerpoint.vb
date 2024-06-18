Sub ExtractShapeData()
    Dim ppt As Presentation
    Dim sld As Slide
    Dim shp As Shape
    Dim pts As ShapeNodes
    Dim Node As ShapeNode

    Dim i As Integer
    Dim pointData As String
    Dim outStr As String

    Set ppt = ActivePresentation

    FileNum = FreeFile
    Open "C:\Users\mpaulus\point_data.txt" For Output As #FileNum

    For Each sld In ppt.Slides
        For Each shp In sld.Shapes
            If shp.Type = msoFreeform Then
                Set pts = shp.Nodes
                outStr = "FreeForm," & sld.SlideIndex & "," & shp.Name & "," & shp.TextFrame.TextRange.Text
                Print #FileNum, outStr

                For Each Node In pts
                    Print #FileNum, Node.Points(1, 1) & "," & Node.Points(1, 2)
                Next Node

            ElseIf shp.Type = msoAutoShape Then
                If shp.AutoShapeType = msoShapeRectangle Then
                    Set pts = shp.Nodes
                    outStr = "Rectangle," & sld.SlideIndex & "," & shp.Name & "," & shp.TextFrame.TextRange.Text
                    Print #FileNum, outStr
                    Print #FileNum, shp.Left & "," & shp.Top & "," & shp.Width & "," & shp.Height
                End If
            End If
        Next shp
    Next sld

    Close #FileNum

End Sub
