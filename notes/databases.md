# Default Ports

MS SQL Server: 1433
MySql: 3306, X Protocol Port 33060


## SQLite format

<https://www.sqlite.org/fileformat2.html>

### Checkpoint algorithm

> On a checkpoint, the WAL is first flushed to persistent storage using the xSync method of the VFS.
> Then valid content of the WAL is transferred into the database file.
> Finally, the database is flushed to persistent storage using another xSync method call.
> The xSync operations serve as write barriers - all writes launched before the xSync must complete before any write that launches after the xSync begins.
>
> A checkpoint need not run to completion.
> It might be that some readers are still using older transactions with data that is contained in the database file.
> In that case, transferring content for newer transactions from the WAL file into the database would delete the content out from under readers still using the older transactions.
> To avoid that, checkpoints only run to completion if all reader are using the last transaction in the WAL.

May have to look into what constitutes `xSync` method of the VFS.


# References

[Database in C#](https://youtu.be/4TqR8yVVjV4)
