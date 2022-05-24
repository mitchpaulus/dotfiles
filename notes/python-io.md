# Python IO

[List files in directory](https://stackoverflow.com/a/3207973/5932184)

```python
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

os.listdir(path='.') # Name of entries in the path
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

