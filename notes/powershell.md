# Powershell

# Symbolic Links

```powershell
New-Item -ItemType SymbolicLink -Path path\to\new\file.txt -Target path\to\already\existing\file.txt
```

# Common default aliases

Can view these aliases using 'Get-Alias'

```
cat -> Get-Content
cd -> Set-Location
cp -> Copy-Item
dir -> Get-ChildItem
% -> ForEach-Object
? -> Where-Object
```

# Other

- Installation Path: `C:\Windows\System32\WindowsPowershell\v1.0\`

# Selecting Properties in Pipeline

```powershell
Get-Process | Select-Object -Property Name, Id, Path
Get-ChildItem | Select-Object -ExpandProperty Name  # Needed to get the actual value of the property, not a new object with the property
```

# Locations

<https://www.powershelladmin.com/wiki/PowerShell_Executables_File_System_Locations.php>

32-bit (x86) PowerShell executable	%SystemRoot%\SysWOW64\WindowsPowerShell\v1.0\powershell.exe
64-bit (x64) Powershell executable	%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe
32-bit (x86) Powershell ISE executable	%SystemRoot%\SysWOW64\WindowsPowerShell\v1.0\powershell_ise.exe
64-bit (x64) Powershell ISE executable	%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell_ise.exe

PowerShell core:

Get-Command pwsh.exe

PS C:\> (Get-Command -Name pwsh).Path
C:\Program Files\PowerShell\6\pwsh.exe

```
# GREP, alias sls
Select-String -Path .\file.txt -Pattern "pattern"
# Returns MatchInfo class
# -SimpleMatch, -List, -Raw
# -AllMatches (gets all the matches on a given line)

# FIND, Get-ChildItem, alias dir
Get-ChildItem -Path .\ -Recurse -Filter "*.txt" | Select-String -Pattern "pattern"
```
