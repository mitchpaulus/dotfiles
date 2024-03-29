" Plugins {{{1
set nocompatible  " be iMproved, required for Vundle

" Programming would be craziness without.
filetype plugin indent on

" Automatically pull vim-plug if required. From
" https://github.com/junegunn/vim-plug/wiki/tips#automatic-installation
if has('unix')
    if empty(glob('~/.local/share/nvim/site/autoload/plug.vim'))
      silent !curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
      autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
    endif
elseif has('win32')
    if empty(glob('~\AppData\Local\nvim\autoload\plug.vim'))
        execute "!md " . glob('~') . '\AppData\Local\nvim\autoload'
        execute "!powershell -Command \"Invoke-WebRequest -Uri https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim\" -OutFile " . glob('~') . '\AppData\Local\nvim\autoload\plug.vim"'
        autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
    endif
endif

call plug#begin()

Plug 'altercation/vim-colors-solarized'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'godlygeek/tabular'
Plug 'lervag/vimtex'
Plug 'scrooloose/nerdcommenter'
Plug 'scrooloose/nerdtree'
Plug 'sickill/vim-monokai'
" Plug 'SirVer/ultisnips'
Plug 'sjl/gundo.vim'
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-surround'
Plug 'mboughaba/i3config.vim'
Plug 'leafgarland/typescript-vim'
Plug 'arcticicestudio/nord-vim'
Plug 'mitchpaulus/autocorrect.vim'
Plug 'mitchpaulus/axon-vim'
Plug 'mitchpaulus/energyplus-vim'
Plug 'mitchpaulus/vim-andover-plain-english'
Plug 'mitchpaulus/vim-awk-indent-fix'
Plug 'mitchpaulus/vim-siemens-ppcl'
Plug 'mitchpaulus/neobem-vim'
Plug 'nvim-lua/completion-nvim'
Plug 'PProvost/vim-ps1'
Plug 'dag/vim-fish'
Plug 'dylon/vim-antlr'
Plug 'mileszs/ack.vim'

if has("nvim-0.5.0")
    " Trying out some language servers with the built in LSP
    Plug 'neovim/nvim-lspconfig'
endif

call plug#end()

" Using the marker line below to separate out nvim specific stuff, to better
" keep the pure vimrc in sync.
" NVIM START
if has("nvim-0.5.0")

lua << EOF
local nvim_lsp = require('lspconfig')
local on_attach = function(client, bufnr)
  local function buf_set_keymap(...) vim.api.nvim_buf_set_keymap(bufnr, ...) end
  local function buf_set_option(...) vim.api.nvim_buf_set_option(bufnr, ...) end

  buf_set_option('omnifunc', 'v:lua.vim.lsp.omnifunc')
  require'completion'.on_attach()

  -- Mappings.
  local opts = { noremap=true, silent=true }
  buf_set_keymap('n', 'gD', '<Cmd>lua vim.lsp.buf.declaration()<CR>', opts)
  buf_set_keymap('n', 'gd', '<Cmd>lua vim.lsp.buf.definition()<CR>', opts)
  buf_set_keymap('n', '<C-k>', '<Cmd>lua vim.lsp.buf.hover()<CR>', opts)
  buf_set_keymap('n', 'gi', '<cmd>lua vim.lsp.buf.implementation()<CR>', opts)
  -- buf_set_keymap('n', '<C-k>', '<cmd>lua vim.lsp.buf.signature_help()<CR>', opts)
  buf_set_keymap('n', '<space>wa', '<cmd>lua vim.lsp.buf.add_workspace_folder()<CR>', opts)
  buf_set_keymap('n', '<space>wr', '<cmd>lua vim.lsp.buf.remove_workspace_folder()<CR>', opts)
  buf_set_keymap('n', '<space>wl', '<cmd>lua print(vim.inspect(vim.lsp.buf.list_workspace_folders()))<CR>', opts)
  buf_set_keymap('n', '<space>D', '<cmd>lua vim.lsp.buf.type_definition()<CR>', opts)
  buf_set_keymap('n', '<space>rn', '<cmd>lua vim.lsp.buf.rename()<CR>', opts)
  buf_set_keymap('n', 'gr', '<cmd>lua vim.lsp.buf.references()<CR>', opts)
  buf_set_keymap('n', '<space>e', '<cmd>lua vim.lsp.diagnostic.show_line_diagnostics()<CR>', opts)
  buf_set_keymap('n', '[d', '<cmd>lua vim.lsp.diagnostic.goto_prev()<CR>', opts)
  buf_set_keymap('n', ']d', '<cmd>lua vim.lsp.diagnostic.goto_next()<CR>', opts)
  buf_set_keymap('n', '<space>q', '<cmd>lua vim.lsp.diagnostic.set_loclist()<CR>', opts)

  -- Critical to have the noinsert option
  vim.api.nvim_set_option('completeopt', 'menuone,noinsert')

  -- Set some keybinds conditional on server capabilities
  if client.resolved_capabilities.document_formatting then
    buf_set_keymap("n", "<space>f", "<cmd>lua vim.lsp.buf.formatting()<CR>", opts)
  elseif client.resolved_capabilities.document_range_formatting then
    buf_set_keymap("n", "<space>f", "<cmd>lua vim.lsp.buf.range_formatting()<CR>", opts)
  end

  -- Set autocommands conditional on server_capabilities
  if client.resolved_capabilities.document_highlight then
    vim.api.nvim_exec([[
      hi LspReferenceRead cterm=bold ctermbg=red guibg=LightYellow
      hi LspReferenceText cterm=bold ctermbg=red guibg=LightYellow
      hi LspReferenceWrite cterm=bold ctermbg=red guibg=LightYellow
      augroup lsp_document_highlight
        autocmd! * <buffer>
        autocmd CursorHold <buffer> lua vim.lsp.buf.document_highlight()
        autocmd CursorMoved <buffer> lua vim.lsp.buf.clear_references()
      augroup END
    ]], false)
  end
end

-- Use a loop to conveniently both setup defined servers
-- and map buffer local keybindings when the language server attaches
local servers = { "bashls", "vimls", "texlab", "hls", "pyright" }
for _, lsp in ipairs(servers) do
  nvim_lsp[lsp].setup { on_attach = on_attach }
end
EOF

endif
" NVIM END


" General Mappings {{{1
let mapleader=" "
let maplocalleader=","

" Fast saving, but use update not write.
"nnoremap <Leader>w :update<CR>
nnoremap s :<C-u>update<CR>

imap <tab> <Plug>(completion_smart_tab)
imap <s-tab> <Plug>(completion_smart_s_tab)

" For when I hold the shift key too long
command! W w

" Faster scrolling? K is pretty much useless by deafult, losing 'J' a little
" more painful.
nnoremap K 5k
nnoremap J 5j

" Join lines on gj - since I don't wrap lines, default gj is redundant.
nnoremap gj J

" Fast quitting
nnoremap q :q<CR>
" Really quit
nnoremap Q :q!<CR>

" Start macro
nnoremap m q
" [Y]ank entire file to clipboard.
nnoremap <leader>y :<c-u>%yank +<cr>
" Insert [t]oday's [d]ate
nnoremap <leader>td i<c-r>=strftime("%Y-%m-%d")<cr>
" Insert today's c-[d]ate
inoremap <c-d> <c-r>=strftime("%Y-%m-%d")<cr>
" Insert today's date, never used ctrl-t in command mode.
cnoremap <c-t> <c-r>=strftime("%Y-%m-%d")<cr>
" Insert today's date with the day of the week
inoremap <localleader>t <c-r>=strftime("%A %Y-%m-%d")<cr>
" stay on current search
nnoremap * *N

" Copy to clipboard in visual mode
xnoremap <leader>y "+y

" Checktime of the file
nnoremap <leader>ct :<C-u>checktime<cr>

" Compile Pandoc
nnoremap <leader>pc :silent !pandoc -V geometry:margin=1in -o "%:p:r.pdf" "%:p"<cr>

" Terminal mode, see pg. 73 Modern Vim
if has('nvim')
    tnoremap jf <C-\><C-n>
    tnoremap <C-v>jk jk
    tnoremap <Esc> <C-\><C-n>
    tnoremap <C-v><Esc> <Esc>
endif


" From Vimscript the Hard Way chap 15
onoremap p i(
onoremap in( :<c-u>execute "normal! /(\r:nohlsearch\rvi("<cr>
onoremap il( :<c-u>execute "normal! ?(\r:nohlsearch\rvi("<cr>
vnoremap p i(

" Add in quotes
onoremap q i"
vnoremap q i"

onoremap ' i'
vnoremap ' i'

onoremap b i{
vnoremap b i{
onoremap in{ :<c-u>execute "normal! /{\r:nohlsearch\rvi{"<cr>
onoremap inb :<c-u>execute "normal! /{\r:nohlsearch\rvi{"<cr>
onoremap il{ :<c-u>execute "normal! ?{\r:nohlsearch\rvi{"<cr>
onoremap ilb :<c-u>execute "normal! ?{\r:nohlsearch\rvi{"<cr>


" From https://vi.stackexchange.com/a/15233/10847
" 'if' for 'inside fold'
onoremap if :<C-u>normal! [zV]z<CR>
xnoremap if [zo]z

" Copy file to clipboard (d for duplicate)
nnoremap <leader>d ggVG"+y

" Visually select inside latex table cell, first go back to last
" & or beginning of line, mark to s, then go to next & or end of line \\
" then go to the end of the previous word, visually select back to
" original mark.
vnoremap tc v?^\<bar>&<cr>wms/&\<bar>\\\\<cr>:nohlsearch<cr>gEv`s
onoremap tc :<c-u>execute 'normal! ?^\<bar>&' . "\r" . 'wms/&\<bar>\\\\' . "\r:nohlsearch\rgEv`s"<cr>

" Change paste settings
nnoremap <leader>sp :<c-u>set paste!<cr>:set paste?<cr>

" Quickly change present working directory to
" the current files directory.
nnoremap <leader>pw :<c-u>call <SID>ChangePWD()<cr>

function! s:ChangePWD()
    cd %:p:h
    pwd
endfunction

"Make it easy to edit the vimrc file. From
"http://learnvimscriptthehardway.stevelosh.com/chapters/07.html.
nnoremap <leader>ev :edit $MYVIMRC<cr>
nnoremap <leader>sv :source $MYVIMRC<cr>

" [e]dit [t]ikz plugin.
nnoremap <leader>et :vsplit ~/vimfiles/bundle/latex-plus/ftplugin/tex.vim<cr>
"
"[C]lear [W]hitespace at End of Line
nnoremap <leader>cw :%s/\v\s+$//<cr>
"Default searches to be very magic and case-insensitive
"nnoremap / /\v

" These mappings are for VisualStudio Vim in order to get correct indentation.
nnoremap S ddO
nnoremap cc S

nnoremap [q :cprevious<CR>
nnoremap ]q :cnext<CR>
nnoremap [Q :cfirst<CR>
nnoremap ]Q :clast<CR>

nnoremap <silent> [b :bprevious<CR>
nnoremap <silent> ]b :bnext<CR>
nnoremap <silent> [B :bfirst<CR>
nnoremap <silent> ]B :blast<CR>

"Mapping to make current word in insert/normal mode capitalized. See Modal Mapping Vimscript the Hard Way.
"inoremap <leader><c-u> <esc>hviwUea
nnoremap <leader><c-u> viwU

" https://stackoverflow.com/a/60355468/5932184
cnoremap <C-p> <Up>
cnoremap <C-n> <Down>
cnoremap <C-b> <Left>
cnoremap <C-f> <Right>
cnoremap <C-a> <C-b>

"Use jk to escape insert mode. Suggested here:
"http://learnvimscriptthehardway.stevelosh.com/chapters/10.html
"inoremap jk <esc>
" Now switching to jf for a few reasons:
" 1. jk stills causes some RSI problems
" 2. df and fd were annoying since there are many words that end with
"    either of those characters. The biggest offender was f in if statements.
" 3. j is the best leader character, since almost no words end with that.
" 4. So jf splits the duty between both hands using strong pointer finger.
inoremap jf <esc>

noremap <TAB> <PageDown>zz
noremap <S-TAB> <PageUp>zz

" Quick mappings for the beginning and ends of lines
noremap H ^
noremap L $

" Want ctrl-backspace to delete whole word in insert mode
inoremap <C-BS> <C-W>

xnoremap * :<C-u>call <SID>VSetSearch()<CR>/<C-R>=@/<CR><CR>
xnoremap # :<C-u>call <SID>VSetSearch()<CR>?<C-R>=@/<CR><CR>

"Clear the previous search (c[lear] h[ighlight])
nnoremap <leader>ch :nohlsearch<cr>

nnoremap <leader>ss :set spell!<cr>:echo "Spell is now " . &spell<cr>
" Flip background color setting, from http://tilvim.com/2013/07/31/swapping-bg.html.
nnoremap <leader>bg :let &background = ( &background == "dark"? "light" : "dark" )<CR>

" Switch the setting of the [sh]ell slash setting.
nnoremap <leader>sh :<c-u>call <SID>SwitchShellSlash()<CR>

function! s:SwitchShellSlash()
    if &shellslash == 0
        set shellslash
    else
        set noshellslash
    endif
    echo "shellslash setting is now " . &shellslash
endfunction


" Switch setting for [t]ext [w]idth.
nnoremap <leader>tw :<c-u>call <SID>ChangeTextWidth()<CR>

function! s:ChangeTextWidth()
    let &textwidth = ( &textwidth == 0 ? 72 : 0 )
    echo "textwidth is now " . &textwidth
endfunction


"These mappings are for moving around the windows quickly.
nnoremap <C-h> <c-w>h
nnoremap <C-j> <c-w>j
nnoremap <C-k> <c-w>k
nnoremap <C-l> <c-w>l

" From pg. 81 Modern Vim
if has('nvim')
    tnoremap <M-h> <C-\><c-n><c-w>h
    tnoremap <M-j> <C-\><c-n><c-w>j
    tnoremap <M-k> <C-\><c-n><c-w>k
    tnoremap <M-l> <C-\><c-n><c-w>l
endif

nnoremap <c-c> <c-w>c
 " Move backwards in spell check. T is 'backwards til' and I never use it.
nnoremap T [s
nnoremap <kPlus> <c-w>+
nnoremap <kMinus> <c-w>-

nnoremap <c-n> :bn<cr>

" Screen gets messed up in WSL when maximizing.
nnoremap <leader>r :redraw!<cr>
nnoremap <localleader>q :copen<CR>

" Emulate bash in insert mode.
inoremap <c-e> <c-o>$
inoremap <c-a> <c-o>^
" nnoremap <leader>j <c-w>j
" nnoremap <leader>k <c-w>k

inoremap <localleader>df °F
inoremap <localleader>dt ΔT

" Filename completion
inoremap <C-F> <C-X><C-F>

" CTRL-Space is often translated by terminals to CTRL-@. When typing fast,
" CTRL-N followed by space, often catches the CTRL key too long and then
" you get whole 'nother copy of the last insert. I rarely find myself using
" the CTRL-@ mapping, so I don't think this should be a big deal to NOP.
" See:
" https://en.wikipedia.org/wiki/Control_character#How_control_characters_map_to_keyboards
" https://stackoverflow.com/a/7725796/5932184
" https://github.com/microsoft/terminal/issues/2865
inoremap <C-@> <Nop>
inoremap <C-Space> <Space>

" Since ` is used as prefix in tmux, this lets me put in ` without having to
" double the keystrokes. Critical for Markdown.
inoremap <F1> `
inoremap <F2> ```
inoremap <F3> ``<Left>
inoremap <F4> ```<CR><CR>```<Esc>kI

" Sane pasting
inoremap <F9> <C-o>:set paste<CR><C-r>+<C-o>:set nopaste<CR>

" This allows you to escape out of quotes, braces, etc. and then append
" at the end of the current line.
execute "inoremap <C-L> <Esc>A"

" Take first spelling suggestion
nnoremap <F1> 1z=
nnoremap <F2> :<C-u>update<CR>
nnoremap <F4> ZZ
nnoremap <F8> :<c-u>set paste!<cr>:set paste?<cr>
nnoremap <F9> :<C-u>set paste<CR>"+p:set nopaste<CR>
nnoremap <F10> :<C-u>set paste<CR>"+P:set nopaste<CR>

" Open and close parenthesis. Idea from:
" http://xahlee.info/kbd/best_way_to_insert_brackets.html
inoremap <C-j> <Esc>/<++><CR>cgn

" [S]ession [w]rite
nnoremap <leader>sw :mksession! ~/defaultsession.vim<cr>
" [S]ession [l]oad
nnoremap <leader>sl :so ~/defaultsession.vim<cr>
" Toggle list setting
nnoremap <leader>ll :set list!<cr>
"
" Search for the current visual selection using '*'. See pg. 212 of Practical Vim
function! s:VSetSearch()
    let temp = @s
    norm! gv"sy
    let @/ = '\V' . substitute(escape(@s, '/\'), '\n', '\\n', 'g')
    let @s = temp
endfunction

syntax enable

try
    colorscheme monokai
catch
    colorscheme desert
endtry

" Make the QuickFixLine readable
highlight QuickFixLine cterm=bold ctermfg=7

" It's wild that this is even possible, but man it's a headache to work
" through the interop issues with the WSL (not to mention the vimscript layer
" as well). 'wslpath' is required here to translate WSL to windows paths, and
" you have to start cmd.exe in a valid Windows directory or it'll also
" complain.
command! WinExploreHere silent !cd /mnt/c && cmd.exe /C start "vim explore" /D $(wslpath -w '%:p:h')" explorer.exe "$(wslpath -w '%:p:h')"

function! s:MakeHeading(replaceCharacter)
    let previousSearch=@/
    "echom ":s/\\s\\+$//e\rVypVr".a:replaceCharacter.":noh\r"
    silent execute "normal! :s/\\s\\+$//e\rVypVr".a:replaceCharacter
    let @/=previousSearch
endfunction

function! s:CleanBibFile()
    %g/month\s*=/d
    %g/file\s*=/d
    %g/doi\s*=/d
    %g/issn\s*=/d
    %g/keywords\s*=/d
    %g/url\s*=/d
    %g/mendeley-groups\s*=/d
    %s/title\s*=\s*{\s*{\(.*\)}\s*}/title = {\1}/
endfunction

nnoremap <leader>j /<++><cr>cgn
"inoremap <c-j> <esc>/<++><cr>:nohlsearch<cr>cgn

" Figure out what syntax group item under cursor is
function! SynGroup()
    let l:s = synID(line('.'), col('.'), 1)
    echo synIDattr(l:s, 'name') . ' -> ' . synIDattr(synIDtrans(l:s), 'name')
endfunction

" General Settings/Options {{{1
"Custom Status Line
"
let g:markdown_fenced_languages = ['python', 'gnuplot', 'vim', 'sh', 'vim', 'axon', 'lua']
let g:markdown_syntax_conceal = 0

let g:basestatusline='%F%=%y,C:%c,%p%%,HEX:%B,%{&ff},%{&encoding}'

set statusline=%!g:basestatusline
set hlsearch   " highlight search
set incsearch  " highlight temporary searches
set rnu        " Relative line numbering
set number     " Show the current line number
set nocursorline
set encoding=utf-8
set backspace=indent,eol,start " Want backspaces to always work as normal.
set scrolloff=8                " Want two lines above and below cursor when scrolling.
set sidescrolloff=10           " Have some buffer when scrolling side to side.
set smartcase                  " Use smartcase
set laststatus=2               " Always show the statusbar
set nowrap                     " No word wrap.
set lbr                        " Want line breaks at whitespace
set tabstop=4                  " show existing tab with 4 spaces width
set shiftwidth=0               " When 0, follows whatever the tabstop option is.
set expandtab                  " On pressing tab, insert 4 spaces
set cmdheight=2                " Make the command window height 2 to avoid the hit-enter prompts
set history=1000               " Remember up to 1000 ex commands.
set lazyredraw
set ttyfast                    " Not even used in nvim.
set spelllang=en_us
set spellsuggest=10
set hidden
set mouse=a
set noshowmode                 " My status line already takes of this for me.
set sessionoptions=buffers,curdir,winpos,winsize
set nolist                     " No special characters by default
set listchars=tab:▸\ ,eol:¬    " But provide better characters when requried
set guioptions-=e
set guioptions-=L
set guioptions-=R
set nrformats+=alpha

set completeopt=menuone,preview
set shortmess+=c

" Concealed text is completely hidden unless it has a custom replacement character defined
set conceallevel=2

"This is to make sure that when you first enter a file
"you don't get a whole bunch of highlighting.
nohlsearch

if has('win32')
    set directory^=$HOME/vimfiles/tmp//
elseif has('unix')
    set directory^=$HOME/.vim/tmp//
endif
set noswapfile

" Don't try to highlight lines longer than 200 chars (from sjl)
set synmaxcol=200

if executable('rg')
	set grepprg=rg\ --vimgrep
endif

" Set spellfile for custom words. Originally just started as
" HVAC related words, but turned into everything.
if has('win32')
    set spellfile=~\vimfiles\spell\hvac.utf-8.add
elseif has('unix')
    set spellfile=~/.config/nvim/spell/hvac.utf-8.add
endif

if has("gui_running")
  if has("gui_gtk2")
    set guifont=Inconsolata\ 12
  elseif has("gui_gtk3")
    set guifont=Inconsolata\ 12
  elseif has("gui_macvim")
    set guifont=Menlo\ Regular:h14
  elseif has("gui_win32")
    set guifont=Fira_Code_Retina:h10:cANSI:qDRAFT,Consolas:h11:cANSI
    set renderoptions=type:directx
    set encoding=utf-8
  endif
endif


" A sane user does not use these characters in filenames
set isfname-={
set isfname-=}
set isfname-==

set wildignore+=*.aux*
set wildignore+=*.asv
set wildignore+=*.log
set wildignore+=*.swp
set wildignore+=*.nav
set wildignore+=*.toc
set wildignore+=*.out
set wildignore+=*.fdb_latexmk
set wildignore+=*.blg
set wildignore+=*.fls
set wildignore+=*.xdv
set wildignore+=*.bbl
set wildignore+=*.snm
set wildignore+=*.lof
set wildignore+=*.lot
set wildignore+=*.dvi
set wildignore+=*.tmp
set wildignore+=*.synctex.gz
set wildignore+=*/node_modules/*
set wildignore+=*/.git/*
set wildignore+=*/venv/*

set noshellslash

" Plugin Specific Options {{{1

" NERDTree {{{2
" NERDTree Settings
" Open up nerd tree quickly.
nnoremap <leader>n :NERDTree<cr>
let NERDTreeIgnore=['\.aux.*$','\.fls$','\.lof$','\.toc$','\.out$','\.vrb$','\.nav$','\.snm$','\.bbl$','\.bib','\.fdb_latexmk$','\.xdv','\.gif','\.pdf','\~$','\.blg$','\.lot$']



" Gundo {{{2
" Gundo Options. New versions of GVIM don't have
" original python support.
if has('python3')
    let g:gundo_prefer_python3 = 1
endif
" Open up the undo tree.
nnoremap <F5> :<c-u>GundoToggle<cr>

"Tabular {{{2
"Tabular mapping to format table
" aligning on & and \\ at the end of the line.
" See http://stackoverflow.com/questions/19414193/regex-extract-string-not-between-two-brackets
vnoremap <leader>tf :<c-u>'<,'>Tab /[^\\]\zs&\<Bar>\({[^}{]*\)\@<!\(\\\\\)\([^{}]*}\)\@!/<cr>
nnoremap <leader>tf :<c-u>Tab /[^\\]\zs&\<Bar>\({[^}{]*\)\@<!\(\\\\\)\([^{}]*}\)\@!/<cr>
nnoremap <leader>t<Bar> :Tab /<Bar>/<cr>
nnoremap <leader>t= :Tab /=/<CR>
nnoremap <localleader>= :Tab /=/<CR>

" Fugitive {{{2
" Fugitive mappings for status, add, and commit.
nnoremap <leader>gs :Gstatus<cr>
nnoremap <leader>ga :Gwrite<cr>
nnoremap <leader>gc :Gcommit<cr>
nnoremap <leader>gph :Gpush<cr>
nnoremap <leader>gpl :Gpull<cr>

" See Vimcast http://vimcasts.org/episodes/fugitive-vim-resolving-merge-conflicts-with-vimdiff/
" and Prime   https://www.youtube.com/watch?v=PO6DxfGPQvw
nnoremap <leader>gh :diffget //2<cr>
nnoremap <leader>gl :diffget //3<cr>


" Vimtex {{{2
"For vimtex
let g:vimtex_view_enabled = 0
let g:tex_flavor="latex"
let g:vimtex_quickfix_latexlog = {'overfull': 0, 'underfull':0}
let g:vimtex_compiler_latexmk = {
            \ 'backend' : 'jobs',
            \ 'background' : 1,
            \ 'build_dir' : '',
            \ 'callback' : 1,
            \ 'continuous' : 1,
            \ 'executable' : 'latexmk',
            \ 'options' : [
            \   '-pdf',
            \   '-verbose',
            \   '-file-line-error',
            \   '-synctex=0',
            \   '-interaction=nonstopmode',
            \ ],
            \}
"
" Ctrl-P {{{2
" For CTRL-P
let g:ctrlp_mruf_exclude = '.*log\|.*aux\|.*tmp\|.*\\.git\\.*' " Windows
let g:ctrlp_mruf_max = 250

let g:ctrlp_custom_ignore = { 'file': '\.\(pdf\|png\|PNG\)$' }
let g:ctrlp_by_filename = 1
" Chose <c-y> because it is analogous to ctrl-p but with the pointer
" finger
nnoremap <c-y> :CtrlPBuffer<cr>
" Chose <c-u> for most recently [u]sed
nnoremap <c-u> :CtrlPMRU<cr>

" autoignore extensions allows for a .ctrlpignore file, acts like .gitignore
let g:ctrlp_extensions = ['autoignore']

" NERDCommenter {{{2

let g:NERDCustomDelimiters = { "idf": { 'left': '!' } }


" ack.vim --- {{{2

" Use ripgrep for searching ⚡️
" Options include:
" --vimgrep -> Needed to parse the rg response properly for ack.vim
" --type-not sql -> Avoid huge sql file dumps as it slows down the search
" --smart-case -> Search case insensitive if all lowercase pattern, Search case sensitively otherwise
let g:ackprg = 'rg --vimgrep --type-not sql --smart-case'

" Auto close the Quickfix list after pressing '<enter>' on a list item
let g:ack_autoclose = 1

" Any empty ack search will search for the work the cursor is on
let g:ack_use_cword_for_empty_search = 1

" Don't jump to first match
cnoreabbrev Ack Ack!

" Maps <leader>/ so we're ready to type the search keyword
nnoremap <Leader>/ :Ack!<Space>
" }}}
" UltiSnips {{{2
if has('unix')
    let g:UltiSnipsSnippetDir = "~/.vim/UltiSnips"
endif

if has('win32')
    let g:UltiSnipsSnippetDir = "~/vimfiles/UltiSnips"
    let g:UltiSnipsSnippetDirectories = [$HOME.'/vimfiles/UltiSnips', 'UltiSnips']
endif
let g:UltiSnipsUsePythonVersion = 3

nnoremap <leader>ue :UltiSnipsEdit<cr>



let g:AutocorrectFiletypes = ["markdown", "tex", "text","gitcommit"]

" FileType AutoCmd Mappings {{{1
"
augroup filetypemappings
autocmd!

autocmd FileType antlr4 nnoremap <localleader>c :!antlr4 %<CR>
autocmd FileType antlr4 nnoremap <localleader>j :!antlrj %<CR>

autocmd FileType axon inoremap <localleader>do do<CR>end<Esc>ko
autocmd FileType axon inoremap <localleader>ll () =><Esc>3hi
autocmd FileType axon inoremap <localleader>ld () => do<CR><CR>end<Esc>2k$F)i
autocmd FileType axon inoremap <localleader>if if () <++> else <++><Esc>F)i

" make a header 1 line, deleting trailing whitespace first.
autocmd FileType markdown nnoremap <silent> <leader>h1 :<c-u>call <SID>MakeHeading("=")<cr>
autocmd FileType markdown nnoremap <silent> <leader>h2 :<c-u>call <SID>MakeHeading("-")<cr>
autocmd FileType markdown,tex,text setlocal textwidth=72
autocmd FileType markdown,tex,text setlocal spell
autocmd FileType markdown setlocal tabstop=2
autocmd FileType help nnoremap <leader>hh mnA~<esc>`n
autocmd FileType help nnoremap <leader>hl mn78i=<esc>`n
autocmd FileType help setlocal nospell
autocmd FileType bib command! CleanBib call <SID>CleanBibFile()
autocmd FileType gnuplot nnoremap <localleader>g :silent !gnuplot.exe % && start "Plot" %:p:r.png<cr>
autocmd FileType gnuplot nnoremap <localleader>k :silent !taskkill.exe /IM Microsoft.Photos.exe /F<cr>
autocmd FileType gnuplot inoremap ,hist <esc>:0read ~/.vim/snipfiles/hist.gnuplot<cr>

autocmd FileType make inoremap ,p .PHONY :<Space>

" Quickly enter in ² symbol
autocmd FileType markdown,text inoremap ^2 <c-v>178
autocmd FileType markdown,text inoremap ,l [](<++>)<esc>6hi
autocmd FileType markdown,text inoremap ,c ✓
autocmd FileType markdown,text inoremap ,x ✗
" Quickly enter in °F
autocmd FileType markdown,text inoremap DEGF °F

autocmd FileType markdown inoremap <localleader>f ![]()<Esc>2hi
autocmd FileType markdown inoremap <localleader>i **<Left>
autocmd FileType markdown inoremap <localleader>b ****<Left><Left>
autocmd FileType markdown inoremap <localleader>e $$  $$<Esc>2hi
autocmd FileType markdown inoremap <localleader>n \begin{equation}<CR>\end{equation}<Esc>0ko
autocmd FileType markdown inoremap <localleader>m $$<Left>

autocmd FileType gitcommit setlocal spell

autocmd FileType html inoremap ,1 <h1></h1><Esc>4hi
autocmd FileType html inoremap ,2 <h2></h2><Esc>4hi
autocmd FileType html inoremap ,3 <h3></h3><Esc>4hi
autocmd FileType html inoremap ,a <a href=""></a><Esc>5hi
autocmd FileType html inoremap ,b data-bind=""<Left>
autocmd FileType html inoremap ,c class=""<Left>
autocmd FileType html inoremap ,d <div></div><Esc>5hi
autocmd FileType html inoremap ,i <input  /><Esc>2hi
autocmd FileType html inoremap ,l <label></label><Esc>7hi
autocmd FileType html inoremap ,p <lt>p></p><Esc>3hi
autocmd FileType html inoremap ,sp <span></span><Esc>6hi
autocmd FileType html inoremap ,st <style></style><Esc>7hi
autocmd FileType html inoremap ,u <ul><cr><li></li><cr></ul><Esc>k^f>a

autocmd FileType javascript,typescript inoremap ,f function (<++>) {<cr><++><cr>}<Esc>2k^f(i
" )
autocmd FileType javascript,typescript inoremap ,> () =><Space>

autocmd FileType typescript nnoremap <leader>tc :<c-u>!tsc<cr>

autocmd FileType tex inoremap %%% \%
autocmd FileType tex inoremap ,ab \begin{abstract}<Cr><Cr>\end{abstract}<Esc>k0i
autocmd FileType tex inoremap ,au \author{}<Left>
autocmd FileType tex inoremap ,base <esc>:0read $DOTFILES/snipfiles/base.tex<cr>
autocmd FileType tex inoremap ,bf \textbf{} <++><esc>5hi
autocmd FileType tex inoremap ,co \newcommand{\}{<++>}<esc>6hi
autocmd FileType tex inoremap ,dot \dot{} <++><esc>5hi
autocmd FileType tex inoremap ,en \begin{enumerate}<cr><cr>\end{enumerate}<esc>ki    <esc>i
autocmd FileType tex inoremap ,eq \begin{equation}<cr><cr>\end{equation}<esc>ki    <esc>i
autocmd FileType tex inoremap ,fig \includegraphics{}<Left>
autocmd FileType tex inoremap ,fr \frac{}{}<esc>2hi
autocmd FileType tex inoremap ,h \title{}<Left>
autocmd FileType tex inoremap ,i \item <esc>a
autocmd FileType tex inoremap ,lr \left(\right) <++><esc>11hi
autocmd FileType tex inoremap ,ms \section{}<Left>
autocmd FileType tex inoremap ,mt \maketitle{}<Cr>
autocmd FileType tex inoremap ,p \usepackage{}<esc>i
autocmd FileType tex inoremap ,rm \textrm{}<Left>
autocmd FileType tex inoremap ,s ^{} <++><esc>5hi
autocmd FileType tex inoremap ,tab \begin{tabular}{}<cr><++><cr>\end{tabular}<esc>2k^2f{a
autocmd FileType tex inoremap ,tx \text{} <++><esc>5hi
autocmd FileType tex inoremap ,u _{}<Left>
autocmd FileType tex nnoremap ,base :0read $DOTFILES/snipfiles/base.tex<cr>
autocmd FileType tex nnoremap [e ?\\begin{equation}<cr>:nohlsearch<cr>
autocmd FileType tex nnoremap ]e /\\begin{equation}<cr>:nohlsearch<cr>

autocmd FileType awk inoremap ,! #!/usr/bin/awk -E<cr>
autocmd FileType awk inoremap ,b BEGIN { FS=OFS="" }<esc>2hi
autocmd FileType awk inoremap ,for for (i = ; i <= <++>; i++) {<cr><++><cr>}<esc>2k^f;i
autocmd FileType awk inoremap ,if if () {<cr><++><cr>}<esc>2k^f(a
autocmd FileType awk inoremap ,pf printf("")<esc>hi
autocmd FileType awk inoremap ,sh #!/usr/bin/awk -E<CR>
autocmd FileType awk inoremap <localleader>q \042
autocmd FileType awk inoremap <localleader>sp split(string, array, FS)

autocmd FileType sh inoremap ,sh #!/bin/sh<CR>
autocmd FileType sh,bash nnoremap <localleader>h :read $DOTFILES/snipfiles/shell_help.sh<Cr>
autocmd FileType sh,fish,bash inoremap ,v "$"<Left>

autocmd FileType matlab inoremap ,f function [output] = functionname(inputvariable)<CR><CR>end<Esc>2k

autocmd FileType make inoremap ,v $()<Left>

autocmd FileType idf inoremap <localleader>i ! INCLUDE<Space>
autocmd FileType idf inoremap <localleader>r Replace ECM ::
autocmd FileType idf inoremap <localleader>de Delete ECM
autocmd FileType idf nnoremap <localleader>s /<C-r>*\c<CR>
autocmd FileType idf set errorformat=%l:%c\ %m
autocmd FileType idf set makeprg=idflint\ %
autocmd FileType idf,neobem inoremap <localleader>l λ
autocmd FileType idf,neobem nnoremap <localleader>t :Tabularize /!-\?/l1l1<CR>
autocmd FileType neobem nnoremap <localleader>c :!nbem -o out.idf %<CR>
autocmd FileType neobem inoremap <localleader>f λ  { <++> }<Esc>8hi
autocmd FileType neobem inoremap <localleader>r <  ><Esc>hi
autocmd FileType neobem inoremap <localleader>c ✓

autocmd FileType python inoremap <localleader>wo with open('') as file:<Esc>F'i
" Check if we are main
autocmd FileType python inoremap <localleader>im if __name__ == "__main__":<Cr>

autocmd FileType python,nbem iabbrev improt import


autocmd FileType compass inoremap <localleader>b <!-- Compass:  --><CR><CR><!-- Compass --><Esc>2k0f:la

augroup END



" Event Type Autocmd mappings {{{1
augroup eventtypemappings
autocmd!
" cshtml - html - close enough
autocmd BufEnter *.cshtml set filetype=html
autocmd BufEnter *.do     set filetype=sh
autocmd BufEnter *.do     inoremap ,ex exec >&2<Cr>
autocmd BufEnter *.do     inoremap ,r redo-ifchange<Space>
autocmd BufEnter *.compass set filetype=compass

autocmd BufEnter *.har set filetype=json

autocmd BufEnter dodo.py inoremap ,dep "file_dep": [  ]<Left><Left>
autocmd BufEnter dodo.py inoremap ,a "actions": [  ]<Left><Left>
autocmd BufEnter dodo.py inoremap ,tar "targets": [  ]<Left><Left>
autocmd BufEnter dodo.py inoremap ,doc "doc": ""<Left>
autocmd BufEnter dodo.py inoremap ,task <esc>:read $DOTFILES/snipfiles/doit_task.py<cr>

" Remove trailing whitespace. Use keeppatterns so that
" the search history isn't ruined with the \v\s+$ junk.
" Setting the marks is required so that the cursor doesn't jump
" around.
autocmd BufWrite * execute "normal! mz" |  keeppatterns %s/\v\s+$//e | normal `z
" Make sure we are aware of when we are in insert mode.
autocmd InsertEnter * setlocal statusline=%#ErrorMsg#\ INSERT\ %.50F%=%y,C:%c,%p%%,HEX:%B,%{&ff},%{&encoding}
autocmd InsertLeave * setlocal statusline=%!g:basestatusline
augroup END



" vim:ft=vim:foldmethod=marker
