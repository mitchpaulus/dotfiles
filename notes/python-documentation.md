# Python Documentation

The Python interpreter actually parses comments in particular locations
in a particular form. See [PEP](https://www.python.org/dev/peps/pep-0257/)

Within the comments, there are several competing standards:

1. Google docstrings
2. reStructured Text
3. NumPy/SciPy docstring

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
