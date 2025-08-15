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

INSERT INTO mydatabasename.mytable (MyColumnName1, MyColumnName2) VALUES ('Value1', 'Value2');
```
