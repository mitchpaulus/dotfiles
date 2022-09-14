# Python CSV module

```python
# https://docs.python.org/3/library/csv.html
import csv
reader = csv.reader(csvfile,dialect='excel',**fmtparams)

# Can loop over reader
for row in reader:
  # row :: List[str]

filelike_from_string = io.StringIO('test string')
```
