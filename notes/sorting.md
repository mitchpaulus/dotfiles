# Sorting

## Python

Python sorting in recent versions is stable meaning you can do:

```
list.sort(key=secondary_key)
list.sort(key=primary_key)
```

### Natural Sorting

[Jeff Atwood Post](https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/).

[Source](https://stackoverflow.com/a/2669120/5932184)

```python
import re

def sorted_nicely(l):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)
```


## `sort`

```
-f: Ignore "fold" case
-V: Version sort
```
