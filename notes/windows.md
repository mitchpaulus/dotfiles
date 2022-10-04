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

The `Roaming` folder can follow the user on different computers within
the same domain. The `Local` folder is local to the machine.


HomeDrive and HomePath not found.

## C:\Program Files vs C:\Program Files (x86)

x86 = 32 bit programs
Program Files\ = 64 bit programs

# Symbolic Links

```powershell
New-Item -ItemType SymbolicLink -Path path\to\new\file.txt -Target path\to\already\existing\file.txt
```

```cmd
MKLINK [/D | /H | /J] Link Target
```

By default, symbolic links are relative, unless a drive letter is
specified in the path.

Based on blog
[here](https://blogs.windows.com/windowsdeveloper/2016/12/02/symlinks-windows-10/),
if you use `mklink` from cmd.exe, you don't need the admin privileges.
Going through the PowerShell route still requires admin privileges.

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

## What is using USB drive?

https://superuser.com/questions/87364/can-windows-tell-me-what-is-using-my-usb-drive#1102080


## Performance Debugging

Links to 'Windows Performance Recorder':
 - <https://answers.microsoft.com/en-us/windows/forum/all/extremely-high-100-disk-usage-windows-10/fa7099e9-2c56-49e7-ad6d-7a278d08e711>
 - <https://answers.microsoft.com/en-us/windows/forum/all/windows-performance-recorder/a1648e8c-50c7-4243-9f1d-4216385c7ff3>

## Issues with Second Monitor not showing

Tuesday 2022-01-11: Keeps resetting to "Only display 1" or "Only display 2" after restart.
From this post [on AMD 12-11-2021 11:27 AM](https://community.amd.com/t5/drivers-software/quot-extend-these-displays-quot-options-resetting-automatically/td-p/500478),
a workaround is to 'Duplicate', and then 'Extend'.
It's only an issue with the AMD drivers.


## Issues with Taskbar

I was finding that sometimes I couldn't click on Icon in the taskbar.
Turns out its a crazy windows bug when Visual Studio 2022 is open.
See <https://techcommunity.microsoft.com/t5/report-an-issue/windows-11-clicking-taskbar-icon-doesn-t-always-switch-to-that/m-p/3015066>
and <https://developercommunity.visualstudio.com/t/Window-switching-in-Window-11-taskbar-st/1597282>.

Used workaround:

[Workaround]
Unchecking the Option “Enable Diagnostic Tools while Debugging” in Visual Studio options resolves the problem for me as well. Looking forward to a fix…

## Special Directories/Folders Locations

Right click on 'Documents' -> Properties -> Location
Typically, it is in the `%USERPROFILE%\Documents` location.
If OneDrive is present, that will usually update the `%USERPROFILE%` environment variable.

[Registry Locations](https://www.repairwin.com/change-personal-folders-location-using-registry-windows-8-7-vista/)

- `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders`

Directories defined:

- {374DE290-123F-4565-9164-39C4925E467B}  –>   %USERPROFILE%\Downloads
- Desktop  –>   %USERPROFILE%\Desktop
- Favorites  –>   %USERPROFILE%\Favorites
- My Music   –>   %USERPROFILE%\Music
- My Pictures  –>   %USERPROFILE%\Pictures
- My Video  –>   %USERPROFILE%\Videos
- Personal  –>   %USERPROFILE%\Documents
- Programs  –>   %USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
- Start Menu  –>   %USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu
- Startup  –>   %USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

## Windows Path variables

There are two PATH related registry keys [Source](https://stackoverflow.com/questions/573817/where-are-environment-variables-stored-in-the-windows-registry):

System: `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment`
User: `Computer\HKEY_CURRENT_USER\Environment`
