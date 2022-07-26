## Dictionaries

[Data Structures Documentation](https://docs.python.org/3.8/tutorial/datastructures.html)
[Dict Reference](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

To be a key, needs to be hashable - have a __hash__() and __eq__() method.

```python
list(d)                      # return list of keys
len(d)                       # return number of keys
d[key]                       # get value for key, exception if doesn't exist
d[key] = value               # set key pair
del d[key]                   # delete key, exception if doesn't exist
key in d
key not in d or not key in d
iter(d) == iter(d.keys())
d.clear()                      # remove all items
d.copy()                       # make shallow copy
d.get(key, [default])          # Get value without exception, None if no xplicit default given.
d.keys()
d.pop(key, [default])          # Can have exception.
d.items()                    # returns iterable of key, value tuples
d.update(other)              # Update dictionary, other overrides

d | other                    # New dictionary, other overrides d (3.9+)
d |= other                   # modify d in place. (3.9+)


for key in dict:
   ...

dict_comprehension = { t.key: t.value for t in iterable }
```


