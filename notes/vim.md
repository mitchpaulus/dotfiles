# Vim

## Mapping Ctrl-Space or Ctrl-@/Finding what key sequence Vim receives

I found this great tip from [here](https://www.reddit.com/r/vim/comments/dn7dtb/how_to_rebind_ctrlspace_in_vim_running_inside/).
To find what sequence Vim is receiving, can use CTRL-V, then sequence,
and see what Vim prints. This helped me find that Vim received Ctrl -
Space as `<C-Space>`, not `<C-@>` as I had expected.



## Syntax Highlighting

See `:h group-name` for standard group names like 'Comment' and
'Constant'

See `:h syn-match` for syntax matching. It's in `syntax.txt`

General process is:

1. Match things using `syntax keyword`, `syntax match`, or `syntax
   region`.

2. Link to highlight groups `highlight link CustomGroup Known Group`

3. `let b:current_syntax="newtype"` at the end of the file.


## Constantly Reload File for Demo

From [link](https://www.reddit.com/r/vim/comments/ktd2kw/run_a_vim_command_in_loop_each_n_seconds/):

```vim
:call timer_start( 2000, { id -> execute( 'e!' ) }, { 'repeat': -1 } )
```

However, combining it with this function for restoring the cursor
position is even better ([link](https://stackoverflow.com/a/50476532/5932184)):

```vim
:call timer_start( 2000, { id -> execute('let l:winview=winsaveview() | checktime | call winrestview(l:winview) ' ) }, { 'repeat': -1 } )
```

## Inserting text from external command

Few options:

1. Use read. `:read !shell text`
2. Use System, Use expression register `<C-R>` followed by `=`.
    `<C-R>=system('shell text')<CR>`
3. Use filter. `:range!shell text`. `:help filter`

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
    - `:helptags $VIMRUNTIME/doc`



## LSP Support

[neovim/lsp-config](https://github.com/neovim/nvim-lspconfig)
[blog on setting up LSP](https://www.chrisatmachine.com/Neovim/27-native-lsp/)

Along with 'neovim/lsp-config', need 'nvim-lua/completion-nvim' for auto
completion like behavior.

## General Improvements

- Must remap Caps Lock to Alt
- Shorten the repeat rate from the keyboard settings

## Neovim lua

For Help:
- api.txt

```vim
nvim.api.nvim_set_keymap({mode}, {lhs}, {rhs}, {opts})
```

## Syntax Highlighting within Markdown

[See Stack Overflow answer here](https://vi.stackexchange.com/questions/23215/how-to-use-code-highlighting-and-checking-in-markdown)
Add `let g:markdown_fenced_languages`{.vim} to vimrc.

## Vim's normal mode grammar

[Cool post](https://gist.github.com/countvajhula/0721a5fc40f2124097652071bb9f97fb)


## Using `<cmd>` in mappings: See `:h :map-cmd` or `:h <Cmd>`
Alternative to using `:<C-u>` in mappings.

