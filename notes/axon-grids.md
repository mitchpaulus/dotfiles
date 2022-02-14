## Grids

```axon
// create grid from list of dicts
g: [{dis:"Site-A", area:2300ft²},
    {dis:"Site-B", area:3100ft²},
    {dis:"Site-C", area:1950ft²}].toGrid

g.isEmpty                     >>  false
g.size                        >>  3
g.has("area")                 >>  true
g.missing("foo")              >>  true
g.meta                        >>  grid level meta data
g.cols                        >>  [ Col("dis"), Col("area") }
g.colNames                    >>  ["dis", "area"]
g.col("dis").name             >>  "dis"
g.col("dis").meta             >>  meta data for column "dis"
g.col("foo")                  >>  throws UnknownNameErr
g.col("foo", false)           >>  null
g.first                       >>  {dis:"Site-A", area:2300ft²}
g.last                        >>  {dis:"Site-C", area:1950ft²}
g[1]                          >>  {dis:"Site-B", area:3100²}
g[-2]                         >>  {dis:"Site-B", area:3100²}
g[0..1]                       >>  slice to new grid of Site-A, Site-B
g.each(row=>...)              >>  iterate each row as a dict
g.foldCol("area", sum)        >>  7350ft²
g.any r => r->area > 2000ft²  >> true
g.all r => r->area > 2000ft²  >> false

g.sort("area")                             >> sort by area column
g.sortr("area")                            >> reverse sort by area column
g.sort((a,b)=>...)                         >> sort with function
g.map r => r.set("area", r->area.to(1m²))  >> area ft² -> m²  // https://skyfoundry.com/doc/lib-axon/func~map
g.find r => r->dis == "Site-A"             >> find row where dis == "Site-A"
g.findAll r => r->area < 2000              >> grid with rows where area < 2000
rowToName: (r) => r->dis[-1..-1].lower     >> func to map "Site-A" -> "a"
g.gridRowsToDict(rowToName, r=>r->area)    >> {a:2300ft², b:3100², c: 1950ft²}
g.gridColsToDict(c=>c.name,c=>c.name.size) >> {dis:3, area:4}
g.addMeta({title:"Sites"})                 >> adds grid level meta data
g.addColMeta("area", {dis:"Sq Footage"})   >> add column level meta data
g.addCol("areaM2") r => r->area.to(1m²)    >> add new column which is area in m²
g.renameCol("area", "sqFt")                >> rename column area -> sqFt
g.reorderCols(["dis", "area"])             >> force specific column ordering
g.removeCol("area")                        >> remove a column
g.removeCols(["area"])                     >> remove a list of columns
g.keepCols(["dis"])                        >> remove all cols except given list
g.addRow({dis:"Site-D", area: 4000ft²})    >> add new row to end of grid
g.addRows([{dis:"Site-D"},{dis:"Site-E"}]) >> add list of new rows to grid
```

## History Grid Transformations

```axon
grid.hisRollup(grid,
grid.hisMap(grid, (val: value, ts: DateTime, his: Point Dictionary, haystack::GbRow) => T) // https://skyfoundry.com/doc/lib-hisKit/func~hisMap
grid.hisFindAll(grid, (val: value, ts: DateTime, his: Point Dictionary, haystack::GbRow) => bool) // https://skyfoundry.com/doc/lib-hisKit/func~hisFindAll
grid.hisFindPeriods(
grid.hisFoldCols(
grid.hisJoin(
grid.hisPeriodIntersection(
grid.hisPeriodUnion(
```
