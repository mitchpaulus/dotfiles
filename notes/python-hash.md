Typically best to use built in hash function on tuple of equality
properties

```python
class BACnetPoint:
    def __hash__(self) -> int:
        return hash((self.name, self.address))

    def __eq__(self, other):
        if not isinstance(other, BACnetPoint):
            return NotImplemented
        return self.name == other.name and self.address == other.address

    def __init__(self, name: str, address: int):
        self.name: str = name
        self.address: int = address
```
