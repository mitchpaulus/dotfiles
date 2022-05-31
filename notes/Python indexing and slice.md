# Understanding the Python Indexing

Python indexing with square brackets is exactly equivalent to called the objects `__getitem__(self, param):` method.

The syntax of [1:2:3] is automatically transformed into a `slice` object to the `__getitem__` method.
All the slice object contains is read only attributes `start`, `stop`, and `step`.
And these don't have to be integers, they can be anything.
If a single object passed (including a single "slice"), it is passed as is.
Otherwise, it is passed as a tuple.

```python
# is valid
my_class[NewClass():"hello"]
# equivalent to:
slice_obj = slice(NewClass(), "hello", None)
my_class.__getitem__(slice_obj)
```

References:
- <https://docs.python.org/3/library/functions.html#slice>


```python
class MyTest:
    def __getitem__(self, param):
        print(str(type(param)) + ": " + param.__repr__())

    def __str__(self):
        return "MyTest Class"

    def __repr__(self):
        return "MyTest Class"

test = MyTest()

test[1::MyTest(), MyTest(), :]
```
