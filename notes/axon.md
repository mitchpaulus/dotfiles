# Axon

Notes for the Axon programming language. Used in SkySpark
application.

Debug Type of variable: `debugType(object)`

```
# map :: Grid -> (Dict -> Dict) -> [Grid | null]
```

Can update an existing Dict using `set` function.

```
# set Val :: Dict -> Str -> Val
dict.set(key, value)

dict.set("navName", "name")
dict.set("his", marker())
```

## String Literals

Raw string: `r"raw\\\@\"`

## Id string format

The default string output for id types is `@idxxxx disMacro`. This is
annoying when you want to reference by just the actual id portion. See
response from Brain [here](https://skyfoundry.com/forum/topic/1301).
Should be able to split on space character.

## IO

Note that `URI` is essentially a IO_Handle. If referencing directory,
must end in trailing slash '/'.

```
ioReadLines :: IO_Handle -> Opts -> List[Str]
ioZipDir :: URI -> Grid (Grid has columns `path`, `size`, and `mod`)
ioZipEntry :: IO_Handle -> Str -> IO_Handle
ioDir :: URI -> Grid (uri, name, mimeType, dir, size, mod)
```

## CRUD Operations

`toRecList` is an important function to turn a grid into a list.

```axon
// add new record
newRec: commit(diff(null, {dis:"New Rec!"}, {add}))

// add someTag to some group of records
readAll(filter).toRecList.map(r => diff(r, {someTag})).commit
```


```axon
// create new record
diff(null, {dis:"New Rec", someMarker}, {add})

// create new record with explicit id like Diff.makeAdd
diff(null, {id:151bd3c5-6ce3cb21, dis:"New Rec"}, {add})

// set/add dis tag and remove oldTag
diff(orig, {dis:"New Dis", -oldTag})

// set/add val tag transiently
diff(orig, {val:123}, {transient})

// diff :: orig_dict -> dict -> flag_dict
// diff :: orig, changes, flags

// flag_dict :: dict with 'add', 'remove', 'transient', or 'force' tags
```

## List Functions

`find`: return first element matching predicate. `FindAll` is the same
but returns all the elements matching the predicate.
```
find T :: List T -> (T -> bool) -> List T
find T :: List T -> ((T -> int) -> bool) -> List T
find T :: Dict -> (T -> bool) -> Dict T
find T :: Dict -> ((T -> int) -> bool) -> Dict T

```

`contains`: return whether list


## String Functions

```axon
123.toStr                      >>  "123"    // convert any object to string
"num=" + 3                     >>  "num=3"  // use '+' for concat
"hi world".isEmpty             >>  false
"hi world".size                >>  8
"hi world"[5]                  >>  114      // unicode char for 'w'
"hi world"[3..-2]              >>  "worl"   // get with range is slice
"root toot".index("oo")        >>  1
"root toot".indexr("oo")       >>  6
"hi world".contains("hi")      >>  true
"Abc".upper                    >>  "ABC"
"Abc".lower                    >>  "abc"
"a,b,c".split(",")             >>  ["a", "b", "c"]
"fooBar".capitalize            >>  "FooBar"
"FooBar".decapitalize          >>  "fooBar"
" xyz ".trim                   >>  "xyz"
"abcd".startsWith("ab")        >>  true
"abcd".endsWith("cd")          >>  true
"foo bar".isTagName            >>  false
"foo bar".toTagName            >>  "fooBar"
"root toot".replace("oo", "a") >> "rat tat"
```

## List Functions

```axon
x: [10, 20, 30]
y: ["chat", "apple", "bee"]
x.isEmpty          >>  false
x.size             >>  3
x[2]               >>  30
x[1..-1]           >>  [20, 30]  // get with range is slice
x.first            >>  10
x.index(30)        >>  2
x.index(40)        >>  null
x.contains(20)     >>  true
x.fold(sum)        >>  60
x.any v => v < 20  >>  true
x.all v => v < 20  >>  false
x.concat(";")      >>  "10;20;30"
// All functions which modify list return a new list (original is immutable)
x.add(40)                      >>  [10, 20, 30, 40]
x.addAll([40, 50])             >>  [10, 20, 30, 40, 50]
x.set(2, 99)                   >>  [10, 20, 99]
x.insert(0, 99)                >>  [99, 10, 20, 30]
x.insertAll(0, [88,99])        >>  [88, 99, 10, 20, 30]
x.remove(1)                    >>  [10, 30]
y.sort                         >>  ["apple", "bee", "chart"]
y.sortr                        >>  ["chart", "bee", "apple"]
y.sort((a,b)=>a.size<=>b.size) >>  ["bee", "chat", "apple"]
y.each s => echo(s)            >>  iterator
y.map s => s.size              >>  [4, 5, 3]
y.flatMap s => [s, s.size]     >>  ["chat", 4, "apple", 5, "bee", 3]
y.find s => s.size == 3        >>  "bee"
y.findAll s => s.size <= 4     >>  ["chat", "bee"]
y.moveTo("chat", -1)           >>  ["apple", "bee", "chat"]
```

## Dicts

```axon
d: {dis:"Bob", bday:1980-06-01}
d.isEmpty            >>  false
d["bday"]            >>  1980-06-01
d["foo"]             >>  null
d->dis               >>  "Bob"
d->foo               >>  UnknownNameErr exception
d.has("bday")        >>  true
d.missing("bday")    >>  false
d.names              >>  ["dis", "bday"]
d.vals               >>  ["Bob", 1980-06-01]
d.dis                >>  "Bob"
d.dis("bday")        >>  "1-Jun-1980"
d.any v => v.isDate  >>  true
d.all(isDate)        >>  false

// iterate keys, vals
d.each((v, k) => echo(k + ": " + v))

d.set("person", marker())  >>  {dis:"Bob", bday:1980-06-01, person}
d.remove("bday")           >>  {dis:"Bob"}
d.map v => v + "!"         >>  {dis:"Bob!", bday:"1980-06-01!"}
d.find v => v.isDate       >>  1980-06-01
d.findAll v => v.isDate    >>  {bday:1980-06-01}
```

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
g.map r => r.set("area", r->area.to(1m²))  >> area ft² -> m²
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

## Folds

Takes a function `fold Tval Tacc :: (Tval -> Tacc) -> Tacc`.

Can use special markers `foldStart()` and `foldEnd()` to build custom
fold function. See [doc](https://skyfoundry.com/doc/lib-axon/func~fold)

Life cycle:

    Call fn(foldStart, null), return initial accumulator state
    Call fn(item, acc) for every item, return new accumulator state
    Call fn(foldEnd, acc) return final result

Example:
```axon
 average: (val, acc) => do
  if (val == foldStart()) return {sum:0, count:0}
  if (val == foldEnd()) return acc->sum / acc->count
  if (val == na()) return na()
  return {sum: acc->sum + val, count: acc->count + 1}
end
```

## Parsing

```axon
parseNumber :: Str -> Bool -> Number | null
parseNumber(text, checked: true)
parseNumber("12kW", false)
```

## Regex

```axon
// Uses Java regular expression syntax.
// Case sensitive by default. Can use flags within pattern,
// https://skyfoundry.com/forum/topic/4716
//
// check match for ENTIRE string
reMatches(r"AHU-(\d+)", "AHU")     // false
reMatches(r"AHU-(\d+)", "AHU-10")  // true

// find substring in a regex
reFind(r"AHU-(\d+)",  "Store-2")        // null
reFind(r"AHU-(\d+)",  "Store-2 AHU-3")  // "AHU-3"

// find all substring groups in a regex
reGroups(r"(Clg|Hgt)-(\d+)", "foo")     // null
reGroups(r"(Clg|Hgt)-(\d+)", "Hgt-7")   // ["Hgt-7", "Hgt", "7"]
reGroups(r"(Clg|Hgt)-(\d+)", "<Hgt-7>") // ["Hgt-7", "Hgt", "7"]
```

`toStr` to make string version.

## Functional Programming

filter: `findAll`
firstOrDefault: `find`
# map :: Grid -> (Dict -> Dict) -> [Grid | null]
SelectMany: `flatMap`

Can use `toRecList` to map to things that aren't Dicts.
See https://skyfoundry.com/forum/topic/2111

`grid.each `

## Grammer

[link](https://skyfoundry.com/doc/docSkySpark/AxonGrammar)

## Exception Handling

`try`, `catch`, `throw`

```axon
throw {dis:"deep doo-doo!"}  // as dict
throw "deep doo-doo!"        // convenience for above
```

## Spark Rules

Important reminders:

- `hisFindPeriods` only takes into account the *first* column of a
  history grid. So will typically need to use a interpolate into a `map`
  function first.

- Can use the built in function `matchPointVal` to help convert
  non-boolean values to booleans.

- [hisFindPeriods and NA() values](https://skyfoundry.com/forum/topic/2827)
