#!/usr/bin/awk -E

# This function transforms the output from a SQL schema dump from
# SQL Server Management Studio into a sql query that counts the number
# of records for each table in the database.

BEGIN { FS=OFS="." }

/CREATE TABLE/ {
    match($2, /\[.*\]/)
    table_name = substr($2, RSTART + 1, RLENGTH - 2)
    line[++n] = sprintf("SELECT '%s' as [Table Name], COUNT(*) as Count FROM [%s]", table_name, table_name)
}

END {
    for (i = 1; i < n; i++) {
        print line[i] " UNION"
    }
    print line[n]
}
