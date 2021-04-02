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

Note that `URI` is essentially a IO_Handle

```
ioReadLines :: IO_Handle -> Opts -> List[Str]
ioZipDir :: URI -> Grid (Grid has columns `path`, `size`, and `mod`)
ioZipEntry :: IO_Handle -> Str -> IO_Handle
```

## CRUD Operations

`toRecList` is an important function to turn a grid into a list.

```
// add new record
newRec: commit(diff(null, {dis:"New Rec!"}, {add}))

// add someTag to some group of records
readAll(filter).toRecList.map(r => diff(r, {someTag})).commit
```


```
// create new record
diff(null, {dis:"New Rec", someMarker}, {add})

// create new record with explicit id like Diff.makeAdd
diff(null, {id:151bd3c5-6ce3cb21, dis:"New Rec"}, {add})

// set/add dis tag and remove oldTag
diff(orig, {dis:"New Dis", -oldTag})

// set/add val tag transiently
diff(orig, {val:123}, {transient})
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

```
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


## Folds

Takes a function `fold Tval Tacc :: (Tval -> Tacc) -> Tacc`.

Can use special markers `foldStart()` and `foldEnd()` to build custom
fold function.
