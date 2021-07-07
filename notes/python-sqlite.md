```python
import sqlite3
connection = sqlite3.connection('path/to/db.db')
cursor = connection.cursor
results = cursor.execute('Select * FROM Table Where Id = ? and Field = ?', (id, field))

for row in cursor
  print(row)
```
