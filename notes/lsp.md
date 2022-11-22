# LSP - Language Server Protocol

An important part of getting the LSP client to start in Neovim is that
a "root" directory has to be found. Normally this is simple regex on
certain file names or directories, for example `.git`.


## Building a Language Server

References:
- [Useful GitHub comment](https://github.com/microsoft/language-server-protocol/issues/964#issuecomment-618867090)

## Completion

[lsp-config wiki](https://github.com/neovim/nvim-lspconfig/wiki/Autocompletion)
[Reddit post](https://www.reddit.com/r/neovim/comments/q58l17/autocompletion_plugin_alternatives/)

<https://github.com/ms-jpq/coq_nvim>

## GEneral Code Completion

Good talk [here](https://www.youtube.com/watch?v=aRO7DkJrA_c). Recommends using a special `CURSOR` token.

## Example Servers in languages I know

LSP servers implemented in C#.

Language              | Repo                                                                              | Notes
----------------------|-----------------------------------------------------------------------------------|------
ANTLR                 | <https://github.com/kaby76/AntlrVSIX>
Bicep                 | <https://github.com/azure/bicep>
C#                    | <https://github.com/OmniSharp/omnisharp-roslyn>
HLSL                  | <https://github.com/tgjones/HlslTools/tree/master/src/ShaderTools.LanguageServer> | Looks to be a good one for example
Language Server Robot | <https://github.com/TypeCobolTeam/LanguageServerRobot/wiki>                       | Not sure what this is
Papyrus               | <https://github.com/joelday/papyrus-lang>
PowerShell            | <https://github.com/PowerShell/PowerShellEditorServices>
Python                | <https://github.com/Microsoft/python-language-server>                             | Read only public archive
Q#                    | <https://github.com/microsoft/qsharp-compiler>
TypeCobol             | <https://github.com/TypeCobolTeam/TypeCobol/tree/master/TypeCobol.LanguageServer>
MiniYAML              | <https://github.com/penev92/Oraide.LanguageServer>


## Gotchas

- Properties `activationEvents` and `main` must both be specified or must both be omitted
- Pretty much need a `tsconfig` - this will set the directory used for main.

- Debug in console - Help -> Toggle Developer Tools in VS Code

## DocumentSymbols and WorkspaceSymbols

See https://github.com/neovim/neovim/issues/11664 for potential uses of that.
