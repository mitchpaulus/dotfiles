# OneOf library C#

```C#
[GenerateOneOf]
public partial class StringOrNumber : OneOfBase<string, int> { }

public partial class StringOrNumber
{
	public StringOrNumber(OneOf.OneOf<System.String, System.Int32> _) : base(_) { }

	public static implicit operator StringOrNumber(System.String _) => new StringOrNumber(_);
	public static explicit operator System.String(StringOrNumber _) => _.AsT0;

	public static implicit operator StringOrNumber(System.Int32 _) => new StringOrNumber(_);
	public static explicit operator System.Int32(StringOrNumber _) => _.AsT1;
}
```
