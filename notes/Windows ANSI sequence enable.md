Source: <https://stackoverflow.com/a/56150498/5932184>

ANSI escape sequences in CMD.exe

```powershell
REG ADD HKCU\CONSOLE /f /v VirtualTerminalLevel /t REG_DWORD /d 1
```
