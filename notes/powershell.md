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
