<https://docs.python.org/3/library/sqlite3.html>

```python
import sqlite3
con = sqlite3.connect('example.db')

cur = con.cursor()

cur.execute('CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)')
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

con.commit()

# This allow you to access columns by name. Critical.
cur.row_factory = sqlite3.Row

for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
  print(row)

# or .fetchone() or .fetchall()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
```
