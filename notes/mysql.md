# MySQL

Package on Ubuntu is `sudo apt install mysql-server`. <https://ubuntu.com/server/docs/databases-mysql>

Utility to read the binary log files (this is what was sent from HPC): `mysqlbinlog`.

## Delimiters

If you have multiple statements, especially with function definitions or similar, you will probably need to set a "delimiter" to something other than ';'
See <https://stackoverflow.com/questions/10259504/delimiters-in-mysql>

```sql
DELIMITER $$
```

- Port 3306


```c#
using MySql.Data.MySqlClient; # From MySql.Data Nuget
string connString = $"Server={mySqlHost};Database=ccllc;User Id=ccllc;Password={mySqlPass};Pooling=true;";
await using var conn = new MySqlConnection(connString);
await conn.OpenAsync();
await using var transaction = await conn.BeginTransactionAsync();
await using var deleteCmd = new MySqlCommand("DELETE FROM PR", conn, transaction);
await deleteCmd.ExecuteNonQueryAsync();

await using var cmd = new MySqlCommand(insertQuery, conn, (MySqlTransaction)transaction);
cmd.Parameters.AddWithValue("@WBS1", MySqlDbType.VarChar, 'hello world');

```

## Root

```sh
sudo -i
mysql

sudo mysql # Does not work.
```

```
SHOW GRANTS FOR CURRENT_USER;

CREATE database mydatabasename;
SHOW DATABASES;

GRANT ALL PRIVILEGES ON mydatabasename.* TO 'myuser'@'%'
ALTER TABLE dbname.mytablename ADD MyColumnName VARCHAR(255) NOT NULL;

INSERT INTO mydatabasename.mytable (MyColumnName1, MyColumnName2) VALUES ('Value1', 'Value2'), ('Value 3', 'Value 4');
```

```
column_definition: {
    data_type [NOT NULL | NULL] [DEFAULT {literal | (expr)} ]
      [VISIBLE | INVISIBLE]
      [AUTO_INCREMENT] [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [COLLATE collation_name]
      [COLUMN_FORMAT {FIXED | DYNAMIC | DEFAULT}]
      [ENGINE_ATTRIBUTE [=] 'string']
      [SECONDARY_ENGINE_ATTRIBUTE [=] 'string']
      [STORAGE {DISK | MEMORY}]
      [reference_definition]
      [check_constraint_definition]
  | data_type
      [COLLATE collation_name]
      [GENERATED ALWAYS] AS (expr)
      [VIRTUAL | STORED] [NOT NULL | NULL]
      [VISIBLE | INVISIBLE]
      [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [reference_definition]
      [check_constraint_definition]
}

```

Data Types:
```
strings: CHAR, VARCHAR, BINARY, VARBINARY, BLOB, TEXT, ENUM, and SET.
INTEGER
TINYINT(1)
DATE TIME DATETIME TIMESTAMP YEAR
```

```
mysql < file.sql # Output as TSV
mysql -N # no header
```

<https://dev.mysql.com/doc/refman/8.4/en/data-types.html>
<https://dev.mysql.com/doc/refman/8.4/en/string-literals.html>

# Install

```
sudo apt install mysql-server
sudo mysql_secure_installation # On Ubuntu, it used auth_socket

sudo mysql

CREATE DATABASE mydb;
CREATE USER myuser@'localhost' IDENTIFIED BY 'password'
GRANT ALL PRIVILEGES ON mydb.* TO myuser@'%';
```

# cnf locations on Windows

```
C:\WINDOWS\my.ini
C:\WINDOWS\my.cnf
C:\my.ini
C:\my.cnf
C:\Program Files\MySQL\my.ini
C:\Program Files\MySQL\my.cnf
```
