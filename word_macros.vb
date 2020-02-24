Sub AutoFitTables()

    Dim tbl As Table

    For Each tbl In ActiveDocument.Tables
        tbl.AutoFitBehavior wdAutoFitContent
    Next tbl

End Sub
