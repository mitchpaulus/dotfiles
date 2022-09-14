## Building Neovim

Good resources:

- [https://dev.to/creativenull/installing-neovim-nightly-alongside-stable-10d0](https://dev.to/creativenull/installing-neovim-nightly-alongside-stable-10d0)
- [https://github.com/neovim/neovim/wiki/Building-Neovim](https://github.com/neovim/neovim/wiki/Building-Neovim)

1. Clone repository
2. `make CMAKE_BUILD_TYPE=Release` to build
3. Either:
    - `make CMAKE_INSTALL_PREFIX=$HOME/local/nvim install`
    - Run directly from the build using: `env VIMRUNTIME=/path/to/neovim/runtime /path/to/build/bin/nvim`
4. Build docs using the EX command while running the new Neovim:
    - `:helptags $VIMRUNTIME/doc` or
    - `:helptags ALL`
