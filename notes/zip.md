## Zip Files

```sh
zip zipfilename files...
fd | zip -@ zipfilename  # Using files from standard input, one per line.
unzip zipfilename -d extractDir  # Only one file can be processed at a time. extractDir doesn't have to exist.
for z in *.zip; unzip $z -d (string sub -e -4 $z); end  # Extract to subdirs.
unzip zilefile.zip fileinzip  # Extract a single file.
unzip -p zipfile.zip fileinzip > new_file_name  # Extract a single file to stdout, can then redirect.
zipsplit -n SIZE zipfile.zip
zip -r zipfile.zip dir  # Recursively zip a directory.
zip -m zipfile.zip file  # Move files into zip file.
```

## C\#

```
System.IO.Compression
ZipArchive
class Program
{
    static void Main()
    {
        // Path to the zip file
        string zipPath = "example.zip";

        // The text content to write into the zip entry
        string textContent = "Hello, this is a UTF-8 encoded string.";

        // Create the zip file and write the text content to an entry
        using (FileStream zipToOpen = new FileStream(zipPath, FileMode.Create))
        {
            using (ZipArchive archive = new ZipArchive(zipToOpen, ZipArchiveMode.Create))
            {
                // Create a new entry in the zip archive
                ZipArchiveEntry readmeEntry = archive.CreateEntry("readme.txt");

                // Write the UTF-8 encoded text content to the entry
                using (StreamWriter writer = new StreamWriter(readmeEntry.Open(), Encoding.UTF8))
                {
                    writer.Write(textContent);
                }
            }
        }

        Console.WriteLine("Zip file created and text written successfully.");
    }
}

```

```sh
gunzip FILE # Uncompress in place
gunzip -c FILE > OUT # Uncompress to stdout
```
