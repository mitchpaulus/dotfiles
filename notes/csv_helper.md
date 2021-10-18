# CsvHelper C\#

```C#
TextReader reader = new StreamReader(filePath, Encoding.UTF8);

using CsvReader csvReader = new CsvReader(reader, CultureInfo.InvariantCulture);

while (csvReader.Read())
{
    var firstRecord = csvReader[0];
}
```
