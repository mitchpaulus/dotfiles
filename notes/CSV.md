# Escaping CSV cell

[Source](https://stackoverflow.com/a/6377656/5932184)

```c#
/// <summary>
/// Turn a string into a CSV cell output. https://stackoverflow.com/a/6377656/5932184
/// </summary>
/// <param name="str">String to output</param>
/// <returns>The CSV cell formatted string</returns>
public static string ToCsvCell(this string str)
{
    bool mustQuote = str.Contains(',') || str.Contains('\"') || str.Contains('\r') || str.Contains('\n');
    if (!mustQuote) return str;

    StringBuilder sb = new();
    sb.Append('\"');
    foreach (char nextChar in str)
    {
        sb.Append(nextChar);
        if (nextChar == '"') sb.Append('\"');
    }
    sb.Append('\"');
    return sb.ToString();
}
```

- [This article](https://www.codeproject.com/Articles/1175263/Why-to-build-your-own-CSV-parser-or-maybe-not) has a nice state machine diagram.

- [Storing state in control flow](https://research.swtch.com/pcdata)
