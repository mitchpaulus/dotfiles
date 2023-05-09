# Zinc

1:1 with Haystack grids

```
ver:"3.0"
col1,col2
```

Null: N
Marker: M
Remove: R
NA: NA
Bool: T or F (for true, false)
Number: 1, -34, 10_000, 5.4e-45, 9.23kg, 74.2°F, 4min, INF, -INF, NaN
Str: "hello", "foo\nbar\" (uses all standard escape chars as C like languages)
Uri: `http://project-haystack.com/`
Ref: @17eb0f3a-ad607713, @xyz "Display Name"
Symbol: ^hot-water
Date: 2010-03-13 (YYYY-MM-DD)
Time: 08:12:05 (hh:mm:ss.FFF)
DateTime: 2010-03-11T23:55:00-05:00 New_York or 2009-11-09T15:39:00Z
Coord: C(37.55,-77.45)
XStr: Type("value")
List: [1, 2, 3]
Dict: {dis:"Building" site area:35000ft²}
Grid: <<ver:"3.0" ... >>
