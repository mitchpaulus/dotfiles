# VS Code

Settings location:

-  Windows %APPDATA%\Code\User\settings.json
-  macOS $HOME/Library/Application Support/Code/User/settings.json
-  Linux $HOME/.config/Code/User/settings.json

Extension locations:

- Windows %USERPROFILE%\.vscode\extensions
- macOS ~/.vscode/extensions
- Linux ~/.vscode/extensions

# Extensions

## Syntax Highlighting

Use Textmate grammars

For syntax highlighting, typically stick with the default scopes.
For the built in theme defaults, can view the scopes used in the VS Code GitHub at:
`vscode/extensions/theme-defaults/themes/dark_plus.json`

Dark Plus uses `keyword.other.operator`, not `keyword.operator`


## Debugger

`"debuggers"` contribution point.

## Variable Reference

[Source](https://code.visualstudio.com/docs/editor/variables-reference)


${userHome} - the path of the user's home folder
${workspaceFolder} - the path of the folder opened in VS Code
${workspaceFolderBasename} - the name of the folder opened in VS Code without any slashes (/)
${file} - the current opened file
${fileWorkspaceFolder} - the current opened file's workspace folder
${relativeFile} - the current opened file relative to workspaceFolder
${relativeFileDirname} - the current opened file's dirname relative to workspaceFolder
${fileBasename} - the current opened file's basename
${fileBasenameNoExtension} - the current opened file's basename with no file extension
${fileDirname} - the current opened file's dirname
${fileExtname} - the current opened file's extension
${cwd} - the task runner's current working directory upon the startup of VS Code
${lineNumber} - the current selected line number in the active file
${selectedText} - the current selected text in the active file
${execPath} - the path to the running VS Code executable
${defaultBuildTask} - the name of the default build task
${pathSeparator} - the character used by the operating system to separate components in file paths

## `launch.json` attributes

[Source](https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes)

## References

[In depth debugger](https://www.codemag.com/article/1809051/Writing-Your-Own-Debugger-and-Language-Extensions-with-Visual-Studio-Code)
[Task Provider Example](https://github.com/microsoft/vscode-extension-samples/tree/main/task-provider-sample)
