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
     ```
     with open('Path') as file:
        file.write(string_var)
     ```

- Binary operations operate like JavaScript, they can be thought more of
  as "selectors". It doesn't covert expression to boolean upon output.
  Therefore, you can do things like:

  `variable = <expr> or <default>`

## Sorting

`sorted` function.

```
sorted(iterable, *, key=None, reverse=False)
```

## Math

```
import math
math.exp(x)
abs(x)
```

Set value to 'NaN': `float('NaN')`


## Unit Testing

```
import unittest

class MyTest(unittest.TestCase):
    def mytest(self):
        ...
        self.assertTrue(expr)
```

## Tuples

Index like lists: `tuple = (item1, item2); tuple[0] == item1`

## Range

`range(start, stop, step)`. `stop` value is exclusive.
`range(stop)` gives 0 to 1 less than stop.
`range(4)` gives [0, 1, 2, 3]


## Typing

Typing functions

```
def myfunction(input: type) -> return_type:
```

Use `None` as return type for "void" functions.

Type Aliasing:

```
Vector = list[float]
```

## String Formatting
https://docs.python.org/3/library/string.html#format-string-syntax
https://docs.python.org/3/library/string.html#formatspec
https://docs.python.org/3/library/string.html#format-specification-mini-language

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
```
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

- https://leemendelowitz.github.io/blog/how-does-python-find-packages.html

Python searches directories in `sys.path`. Can check current value
using:

```python
import sys
print("\n".join(sys.path))
```

Default: Current Directory, PYTHONPATH, directories filled by `site`
module.

Good resource on path modification best practice:
https://docs.python.org/3/install/index.html#modifying-python-s-search-path

Appears easiest way to add path locations is the use of special "path
configuration files". These have an extension of '.pth' and are simply
newline separated directories of paths to add.

Gets more complicated when using PyCharm as an IDE. To add paths to the
project interpreter so that the IDE knows about them, use the dialog in
the settings, see
[https://www.jetbrains.com/help/pycharm/python-interpreters.html#paths](https://www.jetbrains.com/help/pycharm/python-interpreters.html#paths)

1. Ctrl-Alt-S for project settings
2. Project: <project> -> Python Interpreter -> Dropdown -> "Show All"
3. Click icon for more paths, add to that.

From [here](https://packaging.python.org/guides/tool-recommendations/),
`Pipenv` is hot new thing for managing packages for a project.

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

```
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
plt.show()

fig.savefig('filename.ext', format='png')
```


## Virtual Environments

- However, `pipenv` is now the suggested way to manage environments?
```
python -m venv /path/to/proj/venv
source /path/to/proj/venv/bin/activate    (or activate.fish if in fish shell)
deactivate
```

## Processes/System Calls

```python
import subprocess

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
- Enter shell environment using `pipenv shell`. This set ups the proper
  Python paths, so that editors like Vim and pyright can resolve modules
  properly.
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
- Set File encodings in general settings: File | Settings | File
  Encodings
- Make sure to explicitly open files with desired encoding: `open("file", encoding='utf-8')`

## `requests`


## JSON

`import json`
```
# load from string
python_obj = json.loads('[ "a string" ]')
# from file
python_obj = json.load(file_handle)
```

## Classes

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


