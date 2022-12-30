# Windows Terminal

Default settings location:
`%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`

`LOCALAPPDATA` is usually:
`C:\Users\mpaulus\AppData\Local`

# Regenerating profiles

To regenerate the profiles, you need to remove the profiles from the main `settings.json` file,
along with removing the `state.json` file that automatically created.

# Background Image for entire Window

"experimental.useBackgroundImageForWindow": true

See <https://devblogs.microsoft.com/commandline/windows-terminal-preview-1-14-release/>

But currently doesn't work correctly. <https://github.com/microsoft/terminal/issues/14260>
