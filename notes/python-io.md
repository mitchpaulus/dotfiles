# Python IO

[List files in directory](https://stackoverflow.com/a/3207973/5932184)

```python
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

os.listdir(path='.') # Name of entries in the path, only filename component, not full path
```

Don't forget the UTF-8 or you'll get hit with issues for °F in Windows

[Open function documentation](https://docs.python.org/3/library/functions.html#open)

```python
with open('file path', encoding="utf-8") as file:
   lines = file.readlines() # These have the newlines in the string, may need to .strip()
```

Character | Meaning
----------|--------
   'r'    | open for reading (default)
   'w'    | open for writing, truncating the file first
   'x'    | open for exclusive creation, failing if the file already exists
   'a'    | open for writing, appending to the end of the file if it exists
   'b'    | binary mode
   't'    | text mode (default)
   '+'    | open for updating (reading and writing)


`newline` parameter controls how newlines are handled in 'text' mode.
The default is 'Universal newlines', meaning all newlines are converted to Unix '\n'.

`newline` determines how to parse newline characters from the stream. It can be None, '', '\n', '\r', and '\r\n'. It works as follows:

When reading input from the stream, if newline is None, universal newlines mode is enabled.
Lines in the input can end in '\n', '\r', or '\r\n', and these are translated into '\n' before being returned to the caller.
If it is '', universal newlines mode is enabled, but line endings are returned to the caller untranslated.
If it has any of the other legal values, input lines are only terminated by the given string, and the line ending is returned to the caller untranslated.

When writing output to the stream, if newline is None, any '\n' characters written are translated to the system default line separator, os.linesep.
If newline is '' or '\n', no translation takes place.
If newline is any of the other legal values, any '\n' characters written are translated to the given string.



[os.path](https://docs.python.org/3/library/os.path.html)

```python
import os.path

# split :: path -> (head, tail) tail never has slash.
split(path) # '/folder/file.txt' -> ('/folder', 'file.txt')
basename(path) # tail of split
dirname(path) # head of split

isfile(path) # Can accept relative paths
isdir(path)  # Can accept relative paths
splitext(path) # 'file.txt' -> ('file', '.txt'), '.file' -> ('.file', ''), 'foo.bar.txt' -> ('foo.bar', '.txt')
```

## Creating Directory

[os documentation](https://docs.python.org/3/library/os.html)

```python
os.makedirs(name: str, mode=0o777, exist_ok=False) -> None:
```

## Moving Files

```python
# os versions need to be file -> file or dir -> dir.
os.rename(src: path-like, dst: path-like)  # only real difference is how this is handled on Windows?
os.replace(src: path-like, dst: path-like)
shutil.move
```

## Walking Directories

[os.walk](https://docs.python.org/3/library/os.html#os.walk)

## `stdin`

```python
for line in sys.stdin:
  ... # line has trailing '\n'

whole_file: str = sys.stdin.read()
```

```
splitlines() # No newline at end of line
```
