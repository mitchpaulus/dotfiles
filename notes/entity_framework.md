# Entity Framework

- `Where blank in` query:

```csharp
var typeList = new int[] { 2, 4, 5 };

var customerList =
    Customers
        .Where(c => typeList.Contains(c.Type))
        .ToList();
```

## Getting Started

1. Install package for a particular 'database provider'. For SQLServer,
   it is: `Microsoft.EntityFrameworkCore.SqlServer`. Note that you have
   to match the major version to the version of .NET that you are using.
   Last time I did this, I only had .NET 5 available, and the entity
   framework version 6.x.x did not work.

As of 2021-11-09, Entity Framework Core does not have a wizard/EDMX file
for helping generate the models.


## DbContext lifetime

[From docs:](https://docs.microsoft.com/en-us/ef/core/dbcontext-configuration/)

> The lifetime of a DbContext begins when the instance is created and ends
> when the instance is disposed. A DbContext instance is designed to be
> used for a single unit-of-work. This means that the lifetime of a
> DbContext instance is usually very short.

## Available string functions

<https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/ef/language-reference/string-canonical-functions>

- Concat
- Contains
- EndsWith
- IndexOf
- Left
- Length
- LTrim
- Replace
- Reverse
- Right
- RTrim
- Substring
- StartsWith
- ToLower
- ToUpper
- Trim
