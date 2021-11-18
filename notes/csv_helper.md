# CsvHelper C\#

```C#
TextReader reader = new StreamReader(filePath, Encoding.UTF8);

using CsvReader csvReader = new CsvReader(reader, CultureInfo.InvariantCulture);

while (csvReader.Read())
{
    var firstRecord = csvReader[0];
}
```

```C#
// For CsvReader, depends on IParser interface.

		/// <inheritdoc/>
		public virtual bool Read()
		{
			// Don't forget about the async method below!

			bool hasMoreRecords;
			do
			{
				hasMoreRecords = parser.Read();
			}
			while (hasMoreRecords && shouldSkipRecord(new ShouldSkipRecordArgs(parser.Record)));

			currentIndex = -1;
			hasBeenRead = true;

			if (detectColumnCountChanges && hasMoreRecords)
			{
				if (columnCount > 0 && columnCount != parser.Count)
				{
					var csvException = new BadDataException(context, "An inconsistent number of columns has been detected.");

					var args = new ReadingExceptionOccurredArgs(csvException);
					if (readingExceptionOccurred?.Invoke(args) ?? true)
					{
						throw csvException;
					}
				}

				columnCount = parser.Count;
			}

			return hasMoreRecords;
		}

```

All `ReadHeader` does is set the `headerRecord` field to the current
state of the parsers Record. Source code:

```C#
		/// <inheritdoc/>
		public virtual bool ReadHeader()
		{
			if (!hasHeaderRecord)
			{
				throw new ReaderException(context, "Configuration.HasHeaderRecord is false.");
			}

			headerRecord = parser.Record;
			ParseNamedIndexes();

			return headerRecord != null;
		}

```


