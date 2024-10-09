# Vim

## Mapping Ctrl-Space or Ctrl-@/Finding what key sequence Vim receives

I found this great tip from [here](https://www.reddit.com/r/vim/comments/dn7dtb/how_to_rebind_ctrlspace_in_vim_running_inside/).
To find what sequence Vim is receiving, can use CTRL-V, then sequence,
and see what Vim prints. This helped me find that Vim received Ctrl-Space as `<C-Space>`, not `<C-@>` as I had expected.


## Syntax Highlighting

See `:h group-name` for standard group names like 'Comment' and 'Constant'

See `:h syn-match` for syntax matching. It's in `syntax.txt`

General process is:

1. Match things using `syntax keyword`, `syntax match`, or `syntax
   region`.

2. Link to highlight groups `highlight link CustomGroup Known Group`

3. `let b:current_syntax="newtype"` at the end of the file.


Other considerations:

- Should use default option in `highlight default`, so that other peoples configuration isn't overwritten.

- Can use `@Spell` and `@NoSpell` flags to mark where spell checking
  should and shouldn't occur. [link](https://unix.stackexchange.com/a/31155/296724).

- Have run into issue using the `\zs` and `\ze` patterns. The lookahead/lookbehind assertions seems to work fine.

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

## LSP Support

[neovim/lsp-config](https://github.com/neovim/nvim-lspconfig)
[blog on setting up LSP](https://www.chrisatmachine.com/Neovim/27-native-lsp/)

Along with 'neovim/lsp-config', need 'nvim-lua/completion-nvim' for auto
completion like behavior.

Other plugins [from Hacker News](https://news.ycombinator.com/item?id=27713358):

* `nvim-compe` (autocompletion)
* `vim-vsnip` (snippets)
* `lsp_signature.nvim` (automatically pop up signature window, note signature_help is built-into core, just manually triggered)

Another completion engine instead of 'nvim-lua/completion-nvim' is
[ncm2](https://github.com/ncm2/ncm2)

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


## Debugging

`echom` is your friend.

## Printing all mappings to file

<https://stackoverflow.com/a/15756785/5932184>

```
:redir! > vim_keys.txt
:silent verbose map
:redir END
```


## Two character sequences that don't occur in English

This is important for text editing mappings.

From Joseph Lin: <https://www.quora.com/What-are-all-of-the-two-letter-combinations-that-never-occur-in-an-English-dictionary>

Used SIL International English dictionary wordlist

```
bq bz
cf cj cv cx
fq fv fx fz
gq gv gx
hx hz
jb jd jf jg jh jl jm jp jq jr js jt jv jw jx jy jz
kq kx kz
mx mz
pq pv px
qb qc qd qf qg qh qj qk ql qm qn qp qq qv qw qx qy qz
sx
tq
vb vf vh vj vk vm vp vq vw vx
wq wv wx
xd xj xk xr xz
yq yy
zf zr zx
```

## Terminal Mode

Order of events:

1. TermOpen - happens once on creation
2. BufEnter - happens only on *second* load for terminal mode

## Debugging

`echom` in vimscript, `print` in lua.

## Default CTRL keys for Vim.

A: Increment
B: Scroll window pages backwards
C: Interrupt
D: Scroll window downwards
E: Scroll window downwards line
F: Scroll window pages forwards
G: Prints current file name, cursor position, and status
H: Move Left
I: Move forward in jump list
J: Move down line
K: Enter digraph
L: Clears and redraws
M: Like Enter
N: Same as, j, CTRL-J
O: Move backwards in jump list
P: Same as k, move line up.
Q: Same as CTRL-V
R: Redo
S: Nothing??
T: Jump to older entry in tag stack
U: Scroll upwards in the buffer
V: Start visual mode blockwise
W: Starts a prefix for window commands
X: Decrement
Y: Scroll window upwards line
Z: Suspend vim (quit)

## Filetype setting sequence

- Triggers FileType autommand
- Filetype Plugin Loading
    - ftplugin/{filetype}.vim
- Indentation
    - indent/{filetype}.vim
- Syntax
    - syntax/{filetype}.vim
