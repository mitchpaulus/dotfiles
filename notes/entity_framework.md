# Entity Framework

- `Where blank in` query:

```csharp
var typeList = new int[] { 2, 4, 5 };

var customerList =
    Customers
        .Where(c => typeList.Contains(c.Type))
        .ToList();
```
