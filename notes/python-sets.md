## Sets

https://docs.python.org/3/tutorial/datastructures.html#sets
https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

`set` is mutable and does not have hash value
`frozenset` is immutable and does have hash value. Can be used a
dictionary key

```python
myset = { 1, 2, 3 }
myset = { x for x in iterable }
3 in myset

len(s)
x in s
x not in s
isdisjoint(other_set)
issubset(other_set) or set <= other_set
set < other # Proper subset set <= other_set and set != other_set
issuperset(other_set) or set >= other_set
set > other # Proper superset set >= other_set and set != other_set
s.union(*other_sets) or set | other_set | ...
s.intersection(*other_sets) or set & other_set & ...
s.difference(*other_sets) or set - other_set - ...
s.symmetric_difference(other_sets) or set ^ other_set
s.copy()

## Mutability
s.update(*other_sets) or |= operator
s.intersection_update(*other_sets) or &= operator
s.difference_update(*other_sets) or -= operator
s.symmetric_difference_update(other_set) or ^- operator

s.add(element)
s.remove(element) # exception if not in set
s.discard(element)
s.pop() # Error if nothing in set
s.clear()
```
