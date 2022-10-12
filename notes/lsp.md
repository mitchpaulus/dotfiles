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
