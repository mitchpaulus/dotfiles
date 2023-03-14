# Python Documentation

The Python interpreter actually parses comments in particular locations
in a particular form. See [PEP](https://www.python.org/dev/peps/pep-0257/)

Within the comments, there are several competing standards:

1. Google docstrings
2. reStructured Text
3. NumPy/SciPy docstring


Google
```python
def myfunc(param1, param2):
   """
   myfunc does something cool.

   Args:
    param1: Something
    param2: Something Else

   Returns:
    another_thing:

   Raises:
    SomeCrazyException
   """
```

reStructured Text
```python
"""
This is a reST style.

:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""
```

NumPy/SciPy docstring
```python
"""
My numpydoc description of a kind
of very exhautive numpydoc format docstring.

Parameters
----------
first : array_like
    the 1st param name `first`
second :
    the 2nd param
third : {'value', 'other'}, optional
    the 3rd param, by default 'value'

Returns
-------
string
    a value in a string

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""
```
