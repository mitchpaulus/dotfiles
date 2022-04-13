```python
T = TypeVar('T')  # Can be anything
A = TypeVar('A', str, bytes)  # Must be str or bytes
var: List[T]

y = cast(Type, x) # Type Casting
```
