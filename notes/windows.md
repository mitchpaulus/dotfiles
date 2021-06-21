# Windows

Still can't update my HP tower since the issue with Conexant audio
drivers still hasn't been resolved.

[Windows 2004 Status](https://docs.microsoft.com/en-us/windows/release-information/status-windows-10-2004)


## `%USERPROFILE%` vs `%HOMEDRIVE%%HOMEPATH%`

Pretty much am seeing `%USERPROFILE%` as the better option.

## C:\Program Files vs C:\Program Files (x86)

x86 = 32 bit programs
Program Files\ = 64 bit programs

# Symbolic Links

```powershell
New-Item -ItemType SymbolicLink -Path path\to\new\file.txt -Target path\to\already\existing\file.txt
```
