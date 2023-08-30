# Python

## Basics

- Opening a file:
    - `with open('File path') as file:`
    - Read lines with `file.readlines()`
- String operations
    - Trim/Strip: `str_object.strip()`
    - Split: `str_object.split(string_to_split_on)`
    - Replace `str_object.replace(old, new[, max])` returns new string
- Truthiness
    - Object is `True` unless it defines a `__bool__()` method that
      returns `False` or a `__len__()` method that returns 0.
    - All values are considered "truthy" except for the following, which are "falsy":
            1. None
            2. False
            3. 0
            4. 0.0
            5. 0j
            6. Decimal(0)
            7. Fraction(0, 1)
            8. [] - an empty list
            9. {} - an empty dict
            10. () - an empty tuple
            11. '' - an empty str
            12. b'' - an empty bytes
            13. set() - an empty set
            14. an empty range, like range(0)
            15. objects for which
                1. obj.__bool__() returns False
                2. obj.__len__() returns 0

- lambda syntax, `lambda var1, var2: expression`

- Write to File:

  ```python
  with open('Path', 'wt') as file:
    file.write(string_var)
  ```

- Binary operations operate like JavaScript, they can be thought more of
  as "selectors". It doesn't covert expression to boolean upon output.
  Therefore, you can do things like:

  `variable = <expr> or <default>`

## Sorting

`sorted` function.

```python
sorted(iterable, *, key=None, reverse=False)
```

## Math

```python
import math
math.exp(x)
abs(x)
```

Set value to 'NaN': `float('NaN')`


## Unit Testing

```python
import unittest

# Must begin with Test
class TestSomeStuff(unittest.TestCase):
    # Must begin with Test
    def test_something(self):
        ...
        self.assertTrue(expr)

if __name__ == '__main__':
  unittest.main()
```

```sh
python -m unittest myfile.TestSomeStuff.test_something
```

## Tuples

Index like lists: `tuple = (item1, item2); tuple[0] == item1`

## Range

`range(start, stop, step)`. `stop` value is exclusive.
`range(stop)` gives 0 to 1 less than stop.
`range(4)` gives [0, 1, 2, 3]

## Lists

```python
list.append(item)
list.extend(other_list)
list.insert(i, x)
list.remove(x)
list.pop([i])
list.clear()
list.sort(*,key=None,reverse=False)
list.copy() # shallow copy
```


## Typing

Typing functions

```python
def myfunction(input: type) -> return_type:
```

Use `None` as return type for "void" functions.

Type Aliasing:

```python
Vector = List[float]
```

Other examples:

```python
Callable[[input_type1, input_type2], return_type]  # For function typing
arg: int = 1  # Variable typing python 3.6+
a: int  # Don't need to initialize to type
```

Also see [mypy documentation](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## String Formatting
https://docs.python.org/3/library/string.html#format-string-syntax
https://docs.python.org/3/library/string.html#formatspec
https://docs.python.org/3/library/string.html#format-specification-mini-language

```
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

Common formats:
`.3f`, `.3g`
Can put in thousands separator with something like:
`,.0f`

Example: `'{.3f}'.format(1.00023)`

Can use double or single quotes, doesn't change things except for
escaping themselves

Raw strings, put 'r' in front.

String literals can be concatenated when next to each other `'string 1'`
`'string 2'`

## Binary Operator Overloading
```python
Binary Operators

Operator           Method
+                  object.__add__(self, other)
-                  object.__sub__(self, other)
*                  object.__mul__(self, other)
//                 object.__floordiv__(self, other)
/                  object.__div__(self, other)
%                  object.__mod__(self, other)
**                 object.__pow__(self, other[, modulo])
<<                 object.__lshift__(self, other)
>>                 object.__rshift__(self, other)
&                  object.__and__(self, other)
^                  object.__xor__(self, other)
|                  object.__or__(self, other)

Assignment Operators:

Operator          Method
+=                object.__iadd__(self, other)
-=                object.__isub__(self, other)
*=                object.__imul__(self, other)
/=                object.__idiv__(self, other)
//=               object.__ifloordiv__(self, other)
%=                object.__imod__(self, other)
**=               object.__ipow__(self, other[, modulo])
<<=               object.__ilshift__(self, other)
>>=               object.__irshift__(self, other)
&=                object.__iand__(self, other)
^=                object.__ixor__(self, other)
|=                object.__ior__(self, other)

Unary Operators:

Operator          Method
-                 object.__neg__(self)
+                 object.__pos__(self)
abs()             object.__abs__(self)
~                 object.__invert__(self)
complex()         object.__complex__(self)
int()             object.__int__(self)
long()            object.__long__(self)
float()           object.__float__(self)
oct()             object.__oct__(self)
hex()             object.__hex__(self)

Comparison Operators

Operator          Method
<                 object.__lt__(self, other)
<=                object.__le__(self, other)
==                object.__eq__(self, other)
!=                object.__ne__(self, other)
>=                object.__ge__(self, other)
>                 object.__gt__(self, other)

```

## Module Loading

My frustration with the Python module loading system cannot be understated.
Example: [Importing files from different folder](https://stackoverflow.com/q/4383571/5932184).
Viewed 2 MILLION TIMES. By default, you CAN'T and are forced to play games with the path.

- <https://leemendelowitz.github.io/blog/how-does-python-find-packages.html>
- <https://realpython.com/absolute-vs-relative-python-imports/#a-quick-recap-on-imports>

In order:

1. From above, Python first searches `sys.modules`, cache of previous imported modules
2. Searches through list of built in modules
3. Python searches directories in `sys.path`. Can check current value using:

   ```python
   import sys
   print("\n".join(sys.path))
   ```

From <https://docs.python.org/3/library/sys.html#sys.path>:

- `python -m module` command line: prepend the current working directory.
- `python script.py` command line: prepend the script’s directory. If it’s a symbolic link, resolve symbolic links.
- `python -c code` and python (REPL) command lines: prepend an empty string, which means the current working directory.

Default: Current Directory (see above), `PYTHONPATH`, directories filled by `site` module.

Good resource on path modification best practice: <https://docs.python.org/3/install/index.html#modifying-python-s-search-path>

Appears easiest way to add path locations is the use of special "path configuration files".
These have an extension of `.pth` and are simply newline separated directories of paths to add.

Gets more complicated when using PyCharm as an IDE.
To add paths to the project interpreter so that the IDE knows about them, use the dialog in the settings, see
<https://www.jetbrains.com/help/pycharm/python-interpreters.html#paths>

1. Ctrl-Alt-S for project settings
2. Project: <project> -> Python Interpreter -> Dropdown -> "Show All"
3. Click icon for more paths, add to that.

From [here](https://packaging.python.org/guides/tool-recommendations/),
`Pipenv` is hot new thing for managing packages for a project.

Packages = a folder with python files
Modules  = a file with a .py extension (or it's built-in or is in C and dynamically loaded).

> A module is a file containing Python definitions and statements. The
> file name is the module name with the suffix .py appended. Within a
> module, the module’s name (as a string) is available as the value of
> the global variable `__name__`.

Other useful links:
 - <https://towardsdatascience.com/taming-the-python-import-system-fbee2bf0a1e4>

From SO: <https://stackoverflow.com/a/16985066/5932184>, found this link. And <https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time>
From Guido himself: <https://mail.python.org/pipermail/python-3000/2007-April/006793.html>
TLDR: running scripts *within* a module is an antipattern.

For Pyright, from <https://github.com/microsoft/pyright/issues/283#issuecomment-538678102>:

> Pyright doesn't know which files are "scripts" and which are source files that will be imported by other files.
> It doesn't have that context. This is a case where python's dynamic nature makes it difficult for a static type checker.
>
> Pyright assumes that sys.path will contain the root of your source tree.
> So if you're script and the files it imports are located in the root directory, it will work as you expect.
> If you have files that you plan to execute as scripts deeper in the source tree, you need to provide those paths.
> That's why pyright supports multiple "executionEnvironments" within its config file.

Key statement is it will add the root of the *source* tree (i.e. root of git).
Otherwise add it as a path in the config file under the `executionEnvironments` key.

## Linear Regression

package: scikit-learn

```python
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
data = ....
regressor.fit(x, y)
# regressor.intercept_, regressor.coeff_, etc.

prediction = regressor.predict(new_x)
```

## `matplotlib`

- Uses `numpy.array`s

```python
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
plt.show()

fig.savefig('filename.ext', format='png')
```


## Virtual Environments

- However, `pipenv` is now the suggested way to manage environments?
```sh
python -m venv /path/to/proj/venv
source /path/to/proj/venv/bin/activate  # (or activate.fish if in fish shell)
deactivate
```

## Processes/System Calls

[subprocess docs](https://docs.python.org/3/library/subprocess.html#subprocess.run)

```python
import subprocess

subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False,
               cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None,
               universal_newlines=None, **other_popen_kwargs) -> CompletedProcess

# CompletedProcess:
#   args: List[str] | str
#   returncode: int
#   stdout
#   stderr

completed_process = subprocess.run(["command", "arg1", "arg2"])
```

## Delimited Data

```python
import csv
with open('file') as file:
    reader = csv.reader(file)
    for row in reader:
        row # row :: [Str]
```

## Pipenv

- Latest recommendation for project package management.
- Run script using `pipenv run python <file>`
- Enter shell environment using `pipenv shell`.
  This set ups the proper Python paths, so that editors like Vim and pyright can resolve modules properly.
- get out of `pipenv` shell with `exit`, NOT `deactivate`.

## Reading Command Line Arguments

```python
# python myscript arg1 arg2

import sys

sys.argv[0] == "myscript"
sys.argv[1] == "arg1"
```

## Path Manipulation

- `pathlib` is a nice, high level utility.

```python
path = pathlib.Path('sample/path.txt')
path.stem == "path"
```

## Parsing HTML

Best recommendation appears to be 'Beautiful Soup'. Documentation found
[here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<head>asdf<head>")

elements = soup.findAll("tag_type", id="an id", anyattribute=true,
attrs={"nonvalid_python_attribute": "value to test"})
# get_text :: Element -> Str
elements[0].get_text()
elements["attribute name"] # returns attribute value
```

## Pycharm File Encodings

Few places to check:

- [VM options](https://www.jetbrains.com/help/pycharm/working-with-consoles.html):
  - Add `-Dconsole.encoding=UTF-8` to `PYCHARM_HOME/bin/pycharm.exe.vmoptions` or `PYCHARM_HOME/bin/pycharm.vmoptions`
  - Can get there from Help -> Edit Custom VM Options
- Set File encodings in general settings: File | Settings | File Encodings
- Make sure to explicitly open files with desired encoding: `open("file", encoding='utf-8')`

## `requests`

```python
import requests


```

## JSON

[JSON docs](https://docs.python.org/3/library/json.html)

The `s` stands for [s]tring.
Have `load` and `dump`.

```python
`import json`
# load from string
python_obj = json.loads('[ "a string" ]')
# from file
python_obj = json.load(file_handle)
# Writing to JSON
string_output = json.dumps(python_object)

# Custom Encoder
def my_encoder(obj):
  if isinstance(obj, MyClass):
     return {
       'specical key': 'special value'
     }
  else:
    pass

output = json.dumps(python_obj, default=my_encoder)


```

Conversion Table:

JSON          | Python
--------------|---------
object        | dict
array         | list
string        | str
number (int)  | int
number (real) | float
true          | True
false         | False
null          | None



## Classes

[Official python documentation](https://docs.python.org/3/tutorial/classes.html)

*namespace*: Mapping from names to objects

```python
# Simple class
class ClassName:
    <Statement 1>
    <Statement 2>
    ...

    def __init__(self, other_params):
        <Statements>...
```

## String Operations

`str.lower()`
`str.endswith('example')`
`str.strip()`


## OS operations

```python
os.mkdir('dirname')
os.path.join('path/', 'file')
os.remove('file')
```

## Check type of object

```python
print(type(my_object))
```

## Variable Scoping

"LEGB" rule - Python searches namespaces going up from Local, Enclosing,
Global, to Built in.

## Read Standard Input

```python
import sys
lines = sys.stdin.readlines()
```

## Date and Time operations

`datetime` module.

```python
from datetime import time
my_time = time(11, 37)
```

## CSE Common SubExpression Elimination

<https://docs.sympy.org/latest/modules/simplify/simplify.html?highlight=cse#module-sympy.simplify.cse_main>

## `Pipfile`

`Pipfile.lock` should be put into version control. <https://stackoverflow.com/a/46303305>
