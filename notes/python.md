# Python

- Opening a file:
    - `with open('File path') as file:`
    - Read lines with `file.readlines()`
- String operations
    - Trim/Strip: `str_object.strip()`
    - Split: `str_object.split(string_to_split_on)`
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

Type Aliasing:

```
Vector = list[float]
```

## String Formatting
https://docs.python.org/3/library/string.html#format-string-syntax
https://docs.python.org/3/library/string.html#formatspec
https://docs.python.org/3/library/string.html#format-specification-mini-language

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
