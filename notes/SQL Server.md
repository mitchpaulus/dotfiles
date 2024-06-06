# SQL Server

Different versions have different size limits

- 10 Gb for Express
- Unlimited for Developer?

Installation steps:

- Run through wizard - 'New SQL Server stand-alone installation or add features to an existing installation'

- Run through install rules:

 - Got one warning on the Windows Firewall:

 States: Rule "Windows Firewall" generated a warning.
 The Windows Firewall is enabled.
 Make sure the appropriate ports are open to enable remote access.
 See the rules documentation at: https://go.microsoft.com/fwlink/?linkid=2094702 for information about ports to open for each feature.

- Feature Selection
  - Only feature that looks like it is required is the "Database Engine Services".
  - The 'Instance Root Directory' was: 'C:\Program Files\Microsoft SQL Server\'

- Instance Configuration
  - Going to use the Default instance: `MSSQLSERVER`
  - Directory: `C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER`

- Server Configuration
  - Here we are setting the service accounts and collation.
  - Using the default Service Accounts:

    | Service                    | Account Name               | Password   | Startup Type   |
    | ---------                  | --------------             | ---------- | -------------- |
    | SQL Server Agent           | NT Service\SQLSERVERAGENT  |            | Manual         |
    | SQL Server Database Engine | NT Service\MSSQLSERVER     |            | Automatic      |
    | SQL Server Browser         | NT AUTHORITY\LOCAL SERVICE |            | Disabled       |

- Database Engine Configuration
  - Authentication, data directories, etc.
  - Set up with the current user, me: `cc\mpaulus`. Also added `sa` account with generated password in password manager.

  - Data Directories
    - Data root directory:         `C:\Program Files\Microsoft SQL Server\`
    - System database directory:   `C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\Data`
    - User database directory:     `C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\Data`
    - User database log directory: `C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\Data`
    - Backup directory:            `C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\Backup`

- Wizard then jumped over the 'Feature Configuration Rules', probably because I didn't choose any features.

- Configuration file path: `C:\Program Files\Microsoft SQL Server\150\Setup Bootstrap\Log\20220517_093623\ConfigurationFile.ini`

- Summary log written to:
  - `C:\Program Files\Microsoft SQL Server\150\Setup Bootstrap\Log\20220517_093623\Summary_MPAULUS_20220517_093623.txt`

- Installation Media Root Directory
  - `C:\SQL2019\Developer_ENU`



## Attaching existing Database MDF

- Using SQL Server Management Studio
- Right click on databases, Attach.
- When adding, looks like the default directory to put the MDF file is:
  - `C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA`
  - Probably want to put things there since that's guaranteed to be a location the service account has access to.

Error: Couldn't find file.
- Check that the file name it's looking for matches the actual file name. I've found them to be different.
  So there is probably something within the MDF file definition itself, in which the real file name on the system must match.
- If there was no LDF or log file, probably will have to remove that from the list as well.


## Disk Size

Can run standard reports out of SQL Server Management Studio.
Right-click on table, 'Reports' -> 'Standard Reports' -> 'Disk Usage' / 'Disk Usage by Table'

## Connections

- 3 different types of connections:
  - Shared Memory
  - Named Pipes
  - TCP/IP

- By default, only Shared Memory is enabled. Can use 'SQL Server Configuration Manager' to enable TCP/IP.

```go
connString := "server=localhost;database=DATABASE_NAME;trusted_connection=yes;"
```

```go
package main

import (
    "database/sql"
    "fmt"
    "log"

    _ "github.com/denisenkom/go-mssqldb"
)

func main() {
    // Update the connection string with your SQL Server details
    // connString := "sqlserver://localhost?user id=cc\\mpaulus&database=CLIMATEC__HOBBYHOU"
    connString := "server=localhost;database=CLIMATEC__HOBBYHOU;trusted_connection=yes;"

    // Open the database connection
    db, err := sql.Open("sqlserver", connString)
    if err != nil {
        log.Fatal("Error creating connection pool: ", err)
    }
    defer db.Close()

    // Example query
    query := "SELECT objname, logdescription FROM tblTrendlogList"

    // Execute the query
    rows, err := db.Query(query)
    if err != nil {
        log.Fatal("Error executing query: ", err)
    }
    defer rows.Close()

    // Iterate through the results
    for rows.Next() {
        var column1, column2 string
        if err := rows.Scan(&column1, &column2); err != nil {
            log.Fatal("Error scanning row: ", err)
        }
        fmt.Printf("Column1: %s, Column2: %s\n", column1, column2)
    }

    // Check for errors from iterating over rows
    if err = rows.Err(); err != nil {
        log.Fatal("Error reading rows: ", err)
    }
}
```

## SSL Connection Troubleshooting

<https://stackoverflow.com/questions/70399243/how-to-fix-sql-server-2019-connection-error-due-to-certificate-issue> Explicitly trust the certificate.
