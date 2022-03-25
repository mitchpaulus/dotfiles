
<http://visguy.com/vgforum/index.php?topic=8810.0>

```vba
Visio.Application.Addons("VisRpt").Run("/rptDefName=ReportDefinition_2.vrd /rptOutput=EXCEL /rptOutputFilename=C:\Users\me\Desktop\visio\Report_1.xml /rptSilent=True")
```

C:\Program Files\Microsoft Office\root\Office16\1033\ShapeReport.vrd

Activating a page in Visio (From <C:\Program Files\Microsoft Office\root\Office16\1033\ShapeReport.vrd>)

```
theApplication.ActiveWindow.Page = theSelection.ContainingPage.Name
```


```vba
Sub reports()

    ' Visio.Application.Addons("VisRpt").Run ("/rptDefName=ShapeReport.vrd /rptOutput=EXCEL /rptOutputFilename=""C:\Users\mpaulus\visio\Refrigerant Fans.xlsx"" /rptSilent=True")


    Dim pg As Visio.Page
    Dim Arguments As String

    For Each pg In Application.ActiveDocument.Pages
        Application.ActiveWindow.Page = pg

        Arguments = "/rptDefName=ShapeReport.vrd /rptOutput=EXCEL /rptOutputFilename=""C:\Users\mpaulus\visio\" & pg.Name & ".xlsx"" /rptSilent=True"
       Visio.Application.Addons("VisRpt").Run (Arguments)

    Next pg



End Sub
```

# Creating Reports Wizard

<https://argondigital.com/blog/product-management/my-favorite-hidden-visio-feature-extracting-data-from-visio-drawings/>

Review -> Shape Reports


By default, reports saved to "Documents" will automatically be loaded.

# Data Structure

<https://hub.packtpub.com/understanding-shapesheet-microsoft-visio-2010/>
Shapes -> broken down into Sections/Rows/Columns


Section.Count == Number of Rows

## Report File Structure

`VisioRptDefField`: Per column.
  - `ID` is unique int.
  - `Display` is always 1.
  - `Tag`: 2 = Shape Data (aka CustomProp), 3 = User-Defined Cells
  - `Type`: 0 = String? 2 = Floating/Integer?


```xml
<VisioRptDefField ID="60" Display="1" DisplayOrder="28" Type="2" SummaryTypes="0" Tag="3">
        <Name>FunctionCode</Name>
        <DisplayName>FunctionCode</DisplayName>
</VisioRptDefField>
```

<https://docs.microsoft.com/en-us/previous-versions/office/developer/office-2003/aa221330(v=office.11)>
Value	Description	Automation constant
-----|-----------|--------------------
0 String. This is the default. visPropTypeString
1 Fixed list. Displays the list items in a drop-down combo box in the Custom Properties dialog box. Specify the list items in the Format cell. Users can select only one item from the list. visPropTypeListFix
2 Number. Includes date, time, duration, and currency values as well as scalars, dimensions, and angles. Specify a format picture in the Format cell. visPropTypeNumber
3 Boolean. Displays FALSE and TRUE as items users can select from a drop-down list box in the Custom Properties dialog box. visPropTypeBool
4 Variable list. Displays the list items in a drop-down combo box in the Custom Properties dialog box. Specify the list items in the Format cell. Users can select a list item or enter a new item that is added to the current list in the Format cell. visPropTypeListVar
5 Date or time value. Displays days, months, and years, or seconds, minutes, and hours, or a combined date and time value. Specify a format picture in the Format cell. visPropTypeDate
6 Duration value. Displays elapsed time. Specify a format picture in the Format cell. visPropTypeDuration
7 Currency value. Uses the system's current Regional Settings. Specify a format picture in the Format cell. visPropTypeCurrency


# Visio Sections/Cell Indices
<https://docs.microsoft.com/en-us/office/vba/api/visio.vissectionindices>

<https://docs.microsoft.com/en-us/office/vba/api/visio.viscellindices>
