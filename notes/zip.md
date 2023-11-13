## Zip Files

```sh
zip zipfilename files...
fd | zip -@ zipfilename  # Using files from standard input, one per line.
unzip zipfilename -d extractDir  # Only one file can be processed at a time. extractDir doesn't have to exist.
for z in *.zip; unzip $z -d (string sub -e -4 $z); end  # Extract to subdirs.
unzip zilefile.zip fileinzip  # Extract a single file.
unzip -p zipfile.zip fileinzip > new_file_name  # Extract a single file to stdout, can then redirect.
```

## C\#

```
System.IO.Compression
ZipArchive
```
