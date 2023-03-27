# SQLite

## Add a column

```
ALTER TABLE <Table> ADD COLUMN <column name> <Column-def>

<Column-def> := 'Name' 'TypeName'? <Column-constraint>*

<Column-constraint> := NOT NULL
<Column-constraint> := PRIMARY KEY AUTOINCREMENT?
```

## Storage Classes

NULL
INTEGER
REAL
TEXT
BLOB

## Type Affinities

TEXT
NUMERIC
INTEGER
REAL
BLOB
