<https://stackoverflow.com/questions/263400/what-is-the-best-algorithm-for-overriding-gethashcode>

```C#
public override int GetHashCode()
{
    unchecked // Overflow is fine, just wrap
    {
        int hash = 17;
        // Suitable nullity checks etc, of course :)
        hash = hash * 23 + field1.GetHashCode();
        hash = hash * 23 + field2.GetHashCode();
        hash = hash * 23 + field3.GetHashCode();
        return hash;
    }
}
// OR
public override int GetHashCode() => HashCode.Combine(this.object1, this.object2);
// OR
(PropA, PropB, PropC, PropD).GetHashCode();
```

```python
def __hash__(self):
   return hash((self.prop1, self.prop2))

# https://stackoverflow.com/a/2909119/5932184
class A:
    def __key(self):
        return (self.attr_a, self.attr_b, self.attr_c)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, A):
            return self.__key() == other.__key()
        return NotImplemented
```

