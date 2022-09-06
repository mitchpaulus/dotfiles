# MySQL

Package on Ubuntu is `sudo apt install mysql-server`. <https://ubuntu.com/server/docs/databases-mysql>

Utility to read the binary log files (this is what was sent from HPC): `mysqlbinlog`.

## Delimiters

If you have multiple statements, especially with function definitions or similar, you will probably need to set a "delimiter" to something other than ';'
See <https://stackoverflow.com/questions/10259504/delimiters-in-mysql>

```sql
DELIMITER $$
```
