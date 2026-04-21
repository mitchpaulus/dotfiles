# SQLite

## Add a column

```
ALTER TABLE <Table> ADD COLUMN <column name> <Column-def>

<Column-def> := 'Name' 'TypeName'? <Column-constraint>*

<Column-constraint> := NOT NULL
<Column-constraint> := PRIMARY KEY AUTOINCREMENT?
```

## Create Table

```
CREATE TABLE mytable (
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL,
 email TEXT UNIQUE
);
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

## CLI

```
sqlite3 -tabs -header <db> <raw sql>
sqlite3 -tabs <db> < <sql file>
```


## Sqlite for C\#

Microsoft.Data.Sqlite is Microsoft’s lightweight ADO.NET provider.
Microsoft’s docs describe it as a lightweight provider, and EF Core’s SQLite provider is built on top of it.
It uses SQLitePCLRaw to talk to the native SQLite library.

System.Data.SQLite is the older, long-running ADO.NET provider maintained by the SQLite project.
Its site describes it as an ADO.NET provider for SQLite, typically installed with the managed package plus a native SQLite build package.
Microsoft’s comparison page notes the history: it began in 2005, and the SQLite team took over maintenance in 2010.

So I'm going to prefer Microsoft.Data.Sqlite

## REPL

```
.tables
.schema table name
```
