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

## Reading CSV, no embedded newlines

```csharp
using System.Text;

namespace CCLLCParsingLibrary;

public class CcllcCsvReader
{
    private readonly StringBuilder _b = new(1000);

    public List<string> ParseCsvLine(string inputLine)
    {
        if (inputLine.Length > _b.Capacity) _b.Capacity = inputLine.Length;
        List<string> fields = new();

        int index = 0;
        int length = inputLine.Length;

        while (index < length)
        {
            if (inputLine[index] == '"')
            {
                index++;
                // Parse escaped
                while (index < length)
                {
                    if (inputLine[index] != '"')
                    {
                        _b.Append(inputLine[index]);
                        index++;
                    }
                    else
                    {
                        if (index >= length) throw new InvalidDataException("Unfinished quoted field");

                        if (index + 1 < length)
                        {
                            // Check whether next item is quote
                            if (inputLine[index + 1] == '"')
                            {
                                _b.Append('"');
                                index += 2;
                            }
                            else if (inputLine[index + 1] == ',')
                            {
                                // Ended escaped field with quote, start next field.
                                fields.Add(_b.ToString());
                                _b.Clear();
                                index += 2;
                                break;
                            }
                            else
                            {
                                throw new Exception($"Invalid CSV format at {index}");
                            }
                        }
                        else // Ended escaped field with quote at end of line.
                        {
                            fields.Add(_b.ToString());
                            _b.Clear();
                            index++;
                        }
                    }
                }
            }
            else if (inputLine[index] == '\r')
            {
                throw new InvalidDataException("This function is not intended to be used with CSV data containing newlines");
            }
            else if (inputLine[index] == '\n')
            {
                throw new InvalidDataException("This function is not intended to be used with CSV data containing newlines");
            }
            else
            {
                // Parse unescaped
                // Read until comma, double quote, or end of line
                while (index < length)
                {
                    char character = inputLine[index];
                    if (character == ',')
                    {
                        fields.Add(_b.ToString());
                        _b.Clear();
                        index++;
                        break;
                    }

                    _b.Append(character);
                    index++;
                }

                if (index >= length)
                {
                    fields.Add(_b.ToString());
                    _b.Clear();
                }
            }
        }

        return fields;
    }
}

```
