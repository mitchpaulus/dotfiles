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
