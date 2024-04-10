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

## General Code Completion

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

## `DocumentSymbols` and `WorkspaceSymbols`

See <https://github.com/neovim/neovim/issues/11664> for potential uses of that.

## LSP

Position 0-based

## OmniSharp C\# LSP

- [Handling errors](https://github.com/OmniSharp/csharp-language-server-protocol/issues/144)

## References

- <https://stefan-marr.de/papers/dls-marr-et-al-execution-vs-parse-based-language-servers/>
- <https://stefan-marr.de/2022/10/effortless-language-servers/>
- <https://stefan-marr.de/downloads/dls22-marr-et-al-execution-vs-parse-based-language-servers.pdf>
- <https://www.hpi.uni-potsdam.de/hirschfeld/publications/media/StolpeFelgentreffHumerNiephausHirschfeld_2019_LanguageIndependentDevelopmentEnvironmentSupportForDynamicRuntimes_AcmDL_Preprint.pdf>
- <https://tamerlan.dev/how-to-build-a-language-server-with-go/>
