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

By default, symbolic links are relative, unless a drive letter is
specified in the path.

In order to get OneDrive to resync, create and delete an empty file in
the directory. Have script file `odsync` to do this file
creation/deletion.

## Issue with Windows Explorer and Toolbar

Many times, I can't open a Windows Explorer instance from the toolbar.
Following the answer
[here](https://community.spiceworks.com/topic/2258254-frustrating-file-explorer-missing-top-portion-or-top-bar-unresponsive),
I was able to magically get things working by removing some network
drive that wasn't often connected.

## Restarting Graphics Driver

CTRL+SHIFT+WIN+B, be careful with that one.

## Print all environment variables

`set` in cmd.exe
