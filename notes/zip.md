## Zip Files

```sh
zip zipfilename files...
fd | zip -@ zipfilename  # Using files from standard input, one per line.
unzip zipfilename -d extractDir  # Only one file can be processed at a time.
```

## C\#

```
System.IO.Compression
ZipArchive
```
