# Windows

Still can't update my HP tower since the issue with Conexant audio
drivers still hasn't been resolved.

[Windows 2004 Status](https://docs.microsoft.com/en-us/windows/release-information/status-windows-10-2004)


## `%USERPROFILE%` vs `%HOMEDRIVE%%HOMEPATH%`

Pretty much am seeing `%USERPROFILE%` as the better option.

Based on documentation [here](https://docs.microsoft.com/en-us/windows/win32/shell/knownfolderid?redirectedfrom=MSDN),
these are the following environment strings, table near the bottom:

Post-Vista:
String | Example Path
-------|-----------
%ALLUSERSPROFILE%   | C:\ProgramData
%APPDATA%           | C:\Users\username\AppData\Roaming
%LOCALAPPDATA%      | C:\Users\username\AppData\Local
%ProgramData%       | C:\ProgramData
%ProgramFiles%      | C:\Program Files
%ProgramFiles(x86)% | C:\Program Files (x86)
%PUBLIC%            | C:\Users\Public
%SystemDrive%       | C:
%USERPROFILE%       | C:\Users\username
%windir%            | C:\Windows


HomeDrive and HomePath not found.

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

## Useful One Drive Environment Variables

Didn't know these existed:

OneDrive=C:\Users\mpaulus\OneDrive - Command Commissioning
OneDriveCommercial=C:\Users\mpaulus\OneDrive - Command Commissioning
