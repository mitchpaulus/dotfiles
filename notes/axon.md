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

