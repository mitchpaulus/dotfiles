
<https://learn.microsoft.com/en-us/office/vba/api/excel.shape>

```
ActiveSheet.Shapes.AddConnector(msoConnectorStraight, 1357.1427559055, _
        271.5715748031, 1585.7142519685, 285.7142519685).Select
        Selection.ShapeRange.Line.EndArrowheadStyle = msoArrowheadTriangle
    Selection.ShapeRange.ConnectorFormat.BeginConnect ActiveSheet.Shapes("Rectangle 2"), 4
    Selection.ShapeRange.ConnectorFormat.EndConnect ActiveSheet.Shapes("Rectangle 4"), 2
```
