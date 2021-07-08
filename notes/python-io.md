# Python IO

[List files in directory](https://stackoverflow.com/a/3207973/5932184)

```python
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
```

Don't forget the UTF-8 or you'll get hit with issues for °F in Windows

```python
with open('file path', encoding="utf-8") as file:
   lines = file.readlines()
```


```python
import os.path

# split :: path -> (head, tail) tail never has slash.
split(path) # '/folder/file.txt' -> ('/folder', 'file.txt')
basename(path) # tail of split
dirname(path) # head of split

isfile(path)
isdir(path)
splitext(path) # 'file.txt' -> ('file', '.txt'), '.file' -> ('.file', '')
```
