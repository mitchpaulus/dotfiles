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

## Sorting Networks

<https://bertdobbelaere.github.io/sorting_networks.html>

[(0,2)]
[(0,1)]
[(1,2)]

[(0,2),(1,3)]
[(0,1),(2,3)]
[(1,2)]

[(0,3),(1,4)]
[(0,2),(1,3)]
[(0,1),(2,4)]
[(1,2),(3,4)]
[(2,3)]

[(0,5),(1,3),(2,4)]
[(1,2),(3,4)]
[(0,3),(2,5)]
[(0,1),(2,3),(4,5)]
[(1,2),(3,4)]
