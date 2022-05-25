<https://stackoverflow.com/a/14799490/5932184>
```python
def decorator(func):
   return func

@decorator
def some_func():
    pass

# Same as:
def decorator(func):
    return func

def some_func():
    pass

some_func = decorator(some_func)

# Also:
@decomaker(argA, argB, ...)
def func(arg1, arg2, ...):
    pass

func = decomaker(argA, argB, ...)(func)
```

## Properties

Built-in: <https://docs.python.org/3/library/functions.html#property>

```python
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```
