-- Packages
vim.fn["plug#begin"]()

vim.cmd [[ Plug 'altercation/vim-colors-solarized' ]]
vim.cmd [[ Plug 'ctrlpvim/ctrlp.vim' ]]
vim.cmd [[ Plug 'godlygeek/tabular' ]]
vim.cmd [[ Plug 'lervag/vimtex' ]]
vim.cmd [[ Plug 'qpkorr/vim-bufkill' ]]
vim.cmd [[ Plug 'scrooloose/nerdcommenter' ]]
vim.cmd [[ Plug 'scrooloose/nerdtree' ]]
vim.cmd [[ Plug 'sickill/vim-monokai' ]]
-- vim.cmd [[ Plug 'SirVer/ultisnips' ]]
vim.cmd [[ Plug 'sjl/gundo.vim' ]]
vim.cmd [[ Plug 'tpope/vim-fugitive' ]]
vim.cmd [[ Plug 'tpope/vim-surround' ]]
vim.cmd [[ Plug 'mboughaba/i3config.vim' ]]
vim.cmd [[ Plug 'leafgarland/typescript-vim' ]]
vim.cmd [[ Plug 'arcticicestudio/nord-vim' ]]
vim.cmd [[ Plug 'mitchpaulus/autocorrect.vim' ]]
vim.cmd [[ Plug 'mitchpaulus/energyplus-vim' ]]
vim.cmd [[ Plug 'mitchpaulus/vim-andover-plain-english' ]]
vim.cmd [[ Plug 'mitchpaulus/vim-siemens-ppcl' ]]
vim.cmd [[ Plug 'mitchpaulus/neobem-vim' ]]
vim.cmd [[ Plug 'nvim-lua/completion-nvim' ]]
vim.cmd [[ Plug 'PProvost/vim-ps1' ]]
vim.cmd [[ Plug 'dag/vim-fish' ]]
vim.cmd [[ Plug 'dylon/vim-antlr' ]]
vim.cmd [[ Plug 'mileszs/ack.vim' ]]

if vim.fn.has('nvim-0.5.0') == 1 then
	vim.cmd [[ Plug 'neovim/nvim-lspconfig' ]]
end

vim.fn["plug#end"]()

if vim.fn.has('nvim-0.5.0') == 1 then
    local function setupLsp()
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

          -- Critical to have the noinsert and noselect option
          vim.api.nvim_set_option('completeopt', 'menuone,noinsert,noselect')

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
    end

    -- Wrap this up so we don't fail if we haven't installed the package yet.
    local status, err = pcall(setupLsp)
    if not status then print(err) end
end


vim.g.mapleader = ' '
vim.g.maplocalleader = ','
vim.g.markdown_fenced_languages = { 'python', 'gnuplot', 'vim', 'sh', 'vim' }
vim.g.markdown_syntax_conceal = 1

silent = { silent = true, noremap = true }

local function nnmap(lhs, rhs)
	vim.api.nvim_set_keymap("n", lhs, rhs, silent)
end

local function inmap(lhs, rhs)
    vim.api.nvim_set_keymap("i", lhs, rhs, silent)
end

-- https://stackoverflow.com/a/11671820/5932184
local function func_map(f, tbl)
	local t = {}
	for k,v in pairs(tbl) do
		t[k] = f(v)
	end
	return t
end

normalNoRecurseMappings = {
	-- Fast quitting
	{ 'q', ':q<CR>' },
	{ 'Q', ':q!<CR>' },

	{ 's', ':<C-u>update<CR>' },

	-- Scrolling
	{ "K", "5k"  },
	{ "J", "5j"  },
	-- Need something to remap to join lines
	{ 'gj', 'J' },

	-- Quick mappings for the beginning and ends of lines
	{ "H", "^" },
	{ "L", "$" },

	-- These mappings are for moving around the windows quickly.
	{ '<C-h>', '<c-w>h' },
	{ '<C-j>', '<c-w>j' },
	{ '<C-k>', '<c-w>k' },
	{ '<C-l>', '<c-w>l' },

	-- Move around buffers and quickfix list
        { '[q', ':cprevious<CR>' },
        { ']q', ':cnext<CR>' },
	{ '[Q', ':cfirst<CR>' },
	{ ']Q', ':clast<CR>' },
	{ '[b', ':bprevious<CR>' },
	{ ']b', ':bnext<CR>' },
	{ '[B', ':bfirst<CR>' },
	{ ']B', ':blast<CR>' },

	-- Take first spelling suggestion
	{ '<F1>', '1z=' },
	{ '<F2>', ':<C-u>update<CR>' },
	{ '<F4>', 'ZZ' },
	{ '<F8>', ':<c-u>set paste!<cr>:set paste?<cr>' },
	{ '<F9>',  ':<C-u>set paste<CR>"+p:set nopaste<CR>' },
	{ '<F10>', ':<C-u>set paste<CR>"+P:set nopaste<CR>' },

	-- Toggle list setting
	{ '<leader>ll', ':set list!<cr>' },

	-- I don't use marks, so move q (starting macros) to m (for macros)
	{ 'm', 'q' },
	-- Copy entire file to clipboard
	{ '<leader>y', ':<C-u>%yank +<CR>' },
	-- Move backwards through spell.
	{ 'T', '[s' },

	-- Clear the previous search (c[lear] h[ighlight])
	{ '<leader>ch', ':nohlsearch<CR>' },

	{ 'ev', ':<C-u>edit $MYVIMRC<CR>' },
	{ 'sv', ':<C-u>luafile $MYVIMRC<CR>' },

	{ '<C-n>', ':bnext<CR>' },
}

func_map(function(tbl) nnmap(tbl[1], tbl[2]) end, normalNoRecurseMappings)

insertModeNoRecurseMappings = {
    { '<c-d>', '<c-r>=strftime("%Y-%m-%d")<cr>' },
    { '<localleader>t', '<c-r>=strftime("%A %Y-%m-%d")<cr>' },

    --inoremap <leader><c-u> <esc>hviwUea
    --[[
    http://learnvimscriptthehardway.stevelosh.com/chapters/10.html suggests jk.
    Now switching to jf for a few reasons:
    1. jk stills causes some RSI problems
    2. df and fd were annoying since there are many words that end with
       either of those characters. The biggest offender was f in if statements.
    3. j is the best leader character, since almost no words end with that.
    4. So jf splits the duty between both hands using strong pointer finger.  ]]
    { 'jf', '<esc>' },
    { '<C-BS>', '<C-W>' },
    { '<c-e>', '<c-o>$' },
    { '<c-a>', '<c-o>^' },

    -- HVAC stuff
    { '<localleader>df', '°F' },
    { '<localleader>dt', 'ΔT' },

    -- Faster file name completion
    { '<C-F>', '<C-X><C-F>' },

    { '<C-@>', '' },
    { '<C-Space>', '<Space>' },

    -- Function keys, mostly to put in tilde's
    { '<F1>', '`' },
    { '<F2>', '```' },
    { '<F3>', '``<Left>' },
    { '<F4>', '```<CR><CR>```<Esc>kI' },
    { '<F9>', '<C-o>:set paste<CR><C-r>+<C-o>:set nopaste<CR>' },


    -- Move to end of line when in insert mode
    { '<C-l>', '<Esc>A' },
    { '<C-j>', '()<Left>' },
}

func_map(function(tbl) inmap(tbl[1], tbl[2]) end, insertModeNoRecurseMappings)

vim.api.nvim_set_keymap("v", '<leader>y', '"+y', silent)
vim.api.nvim_set_keymap("v", 'L', '$', silent)
vim.api.nvim_set_keymap("v", 'H', '^', silent)

local statusLineComponents = {
	-- Used to put the mode, but if terminal can change cursor shape, it really isn't required.
	'%f',   -- File name
	'%=',    -- makes following right aligned
	'%y ',   -- file type
	'C:%c ',  -- column number
	'%p%% ',  -- percentage through file
	'HEX:%B ', -- Hex value for character under cursor
	'%{&ff} ',  -- File format (unix vs. dos)
	'%{&encoding}' -- current encoding
}

vim.api.nvim_set_option('statusline', table.concat(statusLineComponents))

vim.api.nvim_set_option('hlsearch', true)   -- highlight search
vim.api.nvim_set_option('incsearch', true)  -- highlight temporary searches
vim.api.nvim_set_option('lazyredraw', true)  -- don't update screen during macros
vim.api.nvim_set_option('scrolloff', 8)
vim.api.nvim_set_option('sidescrolloff', 10)
vim.api.nvim_set_option('hidden', true)  -- Stop asking me to write file
vim.api.nvim_set_option('mouse', 'a')  -- The mouse can be useful
vim.api.nvim_set_option('isfname', '@,48-57,/,\\,.,-,_,+,(,),[,],@-@')  -- Sane filename characters.
vim.api.nvim_set_option('listchars', 'tab:▸ ,eol:¬,trail:-,nbsp:+')
vim.api.nvim_set_option('showmode', false)
vim.api.nvim_set_option('shiftround', true)
vim.api.nvim_set_option('spellsuggest', 'best,9')
vim.api.nvim_set_option('completeopt', 'menuone,preview')

local wildignorePatterns = table.concat({
    '*.aux',
    '*.asv',
    '*.log',
    '*.swp',
    '*.nav',
    '*.toc',
    '*.out',
    '*.fdb_latexmk',
    '*.blg',
    '*.fls',
    '*.xdv',
    '*.bbl',
    '*.snm',
    '*.lof',
    '*.lot',
    '*.dvi',
    '*.tmp',
    '*.synctex.gz',
    'node_modules/*',
    '.git/*',
    'venv/*',
}, ',')
vim.api.nvim_set_option('wildignore', wildignorePatterns)  -- Sane filename characters.

vim.api.nvim_win_set_option(0, 'relativenumber', true)        -- Relative line numbering
vim.api.nvim_win_set_option(0, 'number', true)     -- Show the current line number

vim.api.nvim_win_set_option(0, 'cursorline', false)
vim.api.nvim_win_set_option(0, 'wrap', false)
vim.api.nvim_win_set_option(0, 'conceallevel', 2) -- Concealed text is completely hidden unless it has a custom replacement character defined

vim.api.nvim_buf_set_option(0, 'spelllang', 'en_us') -- U.S. only spelling

vim.api.nvim_buf_set_option(0, 'expandtab', true) -- Yes, I use spaces
vim.api.nvim_buf_set_option(0, 'tabstop', 4)      -- Default of 8 is absurd
vim.api.nvim_buf_set_option(0, 'shiftwidth', 4)      -- Default of 8 is absurd
vim.api.nvim_buf_set_option(0, 'synmaxcol', 300)
vim.api.nvim_buf_set_option(0, 'swapfile', false)
vim.api.nvim_buf_set_option(0, 'spellfile', os.getenv('DOTFILES') .. '/vim/spell/hvac.utf-8.add')

settings = {


-- nnoremap <leader>sp :<c-u>set paste!<cr>:set paste?<cr>
-- nnoremap <leader>ss :set spell!<cr>:echo "Spell is now " . &spell<cr>
-- inoremap <F9> <C-o>:set paste<CR><C-r>+<C-o>:set nopaste<CR>
-- nnoremap <F8> :<c-u>set paste!<cr>:set paste?<cr>
-- nnoremap <F9> :<C-u>set paste<CR>"+p:set nopaste<CR>
-- nnoremap <F10> :<C-u>set paste<CR>"+P:set nopaste<CR>
-- set laststatus=2               " Always show the statusbar
-- set cmdheight=2                " Make the command window height 2 to avoid the hit-enter prompts
-- set sessionoptions=buffers,curdir,winpos,winsize
-- set guioptions-=e
-- set guioptions-=L
-- set guioptions-=R
-- set completeopt=menuone,noinsert,longest
-- set shortmess+=c
	-- set grepprg=rg\ --vimgrep
    -- set renderoptions=type:directx

}

-- Colorscheme, try monokai
if not pcall(function() vim.cmd('colorscheme monokai') end) then
vim.cmd('colorscheme desert')
end

-- Search for the current visual selection using '*'. See pg. 212 of Practical Vim
function vsetsearch()
	local temp = vim.fn.getreg('s')
	--let temp = @s
	vim.cmd 'normal! gv"sy'
	vim.fn.setreg('/',  '\\V' .. vim.fn.substitute(vim.fn.escape(temp, '/\\'), '\n', '\\n', 'g'))
	vim.fn.setreg('s', temp)
end

--vim.api.nvim_set_keymap("v", '*', ':<C-u>lua vsetsearch()', silent)

vim.g.AutocorrectFiletypes = { "markdown", "tex", "text", "gitcommit" }

-- FileType AutoCmd Mappings {{{1

local function createAugroup(autocmds, name, event)
    vim.cmd('augroup ' .. name)
    vim.cmd('autocmd!')
    for _, autocmd in ipairs(autocmds) do
        vim.cmd('autocmd ' .. event .. ' ' .. table.concat(autocmd, ' '))
    end
    vim.cmd('augroup END')
end

filetypeAutocmds = {

	{ 'antlr4', 'nnoremap', '<localleader>c', ':!antlr4 %<CR>' },
	{ 'antlr4', 'nnoremap', '<localleader>j', ':!antlrj<Space>%<CR>', },

	-- make a header 1 line, deleting trailing whitespace first.
	--{ 'markdown', 'nnoremap', '<silent>', '<leader>h1 :<c-u>call<Space><SID>MakeHeading("=")<cr>', },
	--{ 'markdown', 'nnoremap', '<silent>', '<leader>h2 :<c-u>call<Space><SID>MakeHeading("-")<cr>', },
	{ 'markdown,tex,text', 'setlocal', 'textwidth=72' },
	{ 'markdown,tex,text', 'setlocal spell' },
	{ 'help', 'nnoremap', '<leader>hh', 'mnA~<esc>`n', },
	{ 'help', 'nnoremap', '<leader>hl', 'mn78i=<esc>`n', },
	{ 'help', 'setlocal nospell' },

	{ 'gnuplot', 'nnoremap', '<localleader>g', ':silent !gnuplot.exe % && start "Plot" %:p:r.png<cr>', },
	{ 'gnuplot', 'nnoremap', '<localleader>k', ':silent !taskkill.exe /IM Microsoft.Photos.exe /F<cr>', },
	{ 'gnuplot', 'inoremap', ',hist', '<esc>:0read ~/.vim/snipfiles/hist.gnuplot<cr>', },

	{ 'make', 'inoremap', ',p', '.PHONY :<Space>', },

	-- Quickly enter in ² symbol
	{ 'markdown,text', 'inoremap', '^2', '<c-v>178', },
	{ 'markdown,text', 'inoremap', ',l', '[](<++>)<esc>6hi', },
	{ 'markdown,text', 'inoremap', ',c', '✓', },
	{ 'markdown,text', 'inoremap', ',x', '✗', },
	-- Quickly enter in °F
	{ 'markdown,text', 'inoremap', 'DEGF', '°F', },

	{ 'markdown', 'inoremap', '<localleader>f', '![]()<Esc>2hi', },
	{ 'markdown', 'inoremap', '<localleader>i', '**<Left>', },
	{ 'markdown', 'inoremap', '<localleader>b', '****<Left><Left>', },
	{ 'markdown', 'inoremap', '<localleader>e', '$$  $$<Esc>2hi', },
	{ 'markdown', 'inoremap', '<localleader>n', '\\begin{equation}<CR>\\end{equation}<Esc>0ko', },
	{ 'markdown', 'inoremap', '<localleader>m', '$$<Left>', },

	{ 'gitcommit', 'setlocal spell' },

	{ 'html', 'inoremap', ',1', '<h1></h1><Esc>4hi', },
	{ 'html', 'inoremap', ',2', '<h2></h2><Esc>4hi', },
	{ 'html', 'inoremap', ',3', '<h3></h3><Esc>4hi', },
	{ 'html', 'inoremap', ',a', '<a href=""></a><Esc>5hi', },
	{ 'html', 'inoremap', ',b', 'data-bind=""<Left>', },
	{ 'html', 'inoremap', ',c', 'class=""<Left>', },
	{ 'html', 'inoremap', ',d', '<div></div><Esc>5hi', },
	{ 'html', 'inoremap', ',i', '<input  /><Esc>2hi', },
	{ 'html', 'inoremap', ',l', '<label></label><Esc>7hi', },
	{ 'html', 'inoremap', ',p', '<lt>p></p><Esc>3hi', },
	{ 'html', 'inoremap', ',sp', '<span></span><Esc>6hi', },
	{ 'html', 'inoremap', ',st', '<style></style><Esc>7hi', },
	{ 'html', 'inoremap', ',u', '<ul><cr><li></li><cr></ul><Esc>k^f>a', },

	{ 'javascript,typescript', 'inoremap', ',f', 'function (<++>) {<cr><++><cr>}<Esc>2k^f(i', },
	{ 'javascript,typescript', 'inoremap', ',>', '() =><Space>', },

	{ 'typescript', 'nnoremap', '<leader>tc', ':<c-u>!tsc<cr>', },

	{ 'tex', 'inoremap', '%%%', [[\%]] },
	{ 'tex', 'inoremap', ',ab', '\\begin{abstract}<Cr><Cr>\\end{abstract}<Esc>k0i', },
	{ 'tex', 'inoremap', ',au', '\\author{}<Left>', },
	{ 'tex', 'inoremap', ',base', '<esc>:0read $DOTFILES/snipfiles/base.tex<cr>', },
	{ 'tex', 'inoremap', ',bf', '\\textbf{} <++><esc>5hi', },
	{ 'tex', 'inoremap', ',co', '\\newcommand{\\}{<++>}<esc>6hi', },
	{ 'tex', 'inoremap', ',dot', '\\dot{} <++><esc>5hi', },
	{ 'tex', 'inoremap', ',en', '\\begin{enumerate}<cr><cr>\\end{enumerate}<esc>ki    <esc>i', },
	{ 'tex', 'inoremap', ',eq', '\\begin{equation}<cr><cr>\\end{equation}<esc>ki    <esc>i', },
	{ 'tex', 'inoremap', ',fig', '\\includegraphics{}<Left>', },
	{ 'tex', 'inoremap', ',fr', '\\frac{}{}<esc>2hi', },
	{ 'tex', 'inoremap', ',h', '\\title{}<Left>', },
	{ 'tex', 'inoremap', ',i', '\\item <esc>a', },
	{ 'tex', 'inoremap', ',lr', '\\left(\\right) <++><esc>11hi', },
	{ 'tex', 'inoremap', ',ms', '\\section{}<Left>', },
	{ 'tex', 'inoremap', ',mt', '\\maketitle{}<Cr>', },
	{ 'tex', 'inoremap', ',p', '\\usepackage{}<esc>i', },
	{ 'tex', 'inoremap', ',rm', '\\textrm{}<Left>', },
	{ 'tex', 'inoremap', ',s', '^{} <++><esc>5hi', },
	{ 'tex', 'inoremap', ',tab', '\\begin{tabular}{}<cr><++><cr>\\end{tabular}<esc>2k^2f{a', },
	{ 'tex', 'inoremap', ',tx', '\\text{} <++><esc>5hi', },
	{ 'tex', 'inoremap', ',u', '_{}<Left>', },
	{ 'tex', 'nnoremap', ',base', ':0read $DOTFILES/snipfiles/base.tex<cr>', },
	{ 'tex', 'nnoremap', '[e', '?\\begin{equation}<cr>:nohlsearch<cr>', },
	{ 'tex', 'nnoremap', ']e', '/\\begin{equation}<cr>:nohlsearch<cr>', },

	{ 'awk', 'inoremap', ',!', '#!/usr/bin/awk -E<cr>', },
	{ 'awk', 'inoremap', ',b', 'BEGIN { FS=OFS="" }<esc>2hi', },
	{ 'awk', 'inoremap', ',for', 'for (i = ; i < <++>; i++) {<cr>    <++><cr>}<esc>2k^f;i', },
	{ 'awk', 'inoremap', ',if', 'if () {<cr>    <++><cr>}<esc>2k^f(a', },
	{ 'awk', 'inoremap', ',pf', 'printf("")<esc>hi', },
	{ 'awk', 'inoremap', ',sh', '#!/usr/bin/awk -E<CR>', },
	{ 'awk', 'inoremap', '<localleader>q', '\\042', },
	{ 'awk', 'inoremap', '<localleader>sp', 'split(string, array, FS)', },

	{ 'sh', 'inoremap', ',sh', '#!/bin/sh<CR>', },
	{ 'sh,bash', 'nnoremap', '<localleader>h', ':read $DOTFILES/snipfiles/shell_help.sh<Cr>', },
	{ 'sh,fish,bash', 'inoremap', ',v', '"$"<Left>', },


	{ 'matlab', 'inoremap', ',f', 'function [output] = functionname(inputvariable)<CR><CR>end<Esc>2k', },

	{ 'make', 'inoremap', ',v', '$()<Left>', },

	{ 'idf', 'inoremap', '<localleader>i', '! INCLUDE<Space>', },
	{ 'idf', 'inoremap', '<localleader>r', 'Replace ECM ::', },
	{ 'idf', 'inoremap', '<localleader>de', 'Delete ECM', },
	{ 'idf', 'nnoremap', '<localleader>s', '/<C-r>*\\c<CR>', },
	{ 'idf', 'set', 'errorformat=%l:%c\\', '%m', },
	{ 'idf', 'set', 'makeprg=idflint\\ %', },
	{ 'idf,neobem', 'inoremap', '<localleader>l', 'λ', },
	{ 'idf,neobem', 'nnoremap', '<localleader>t', ':Tabularize /!-\\?/l1l1<CR>', },
	{ 'neobem', 'nnoremap', '<localleader>c', ':!nbem -o out.idf %<CR>', },
	{ 'neobem', 'inoremap', '<localleader>f', 'λ  { <++> }<Esc>8hi', },
	{ 'neobem', 'inoremap', '<localleader>r', '<  ><Esc>hi', },
	{ 'neobem', 'inoremap', '<localleader>c', '✓', },

	{ 'python,nbem', 'iabbrev', 'improt', 'import', },

	{ 'compass', 'inoremap', '<localleader>b', '<!-- Compass:  --><CR><CR><!-- Compass --><Esc>2k0f:la', },
}

createAugroup(filetypeAutocmds, 'filetypemappings', 'FileType')

-- Event Type Autocmds {{{1
bufEnterAutocmds = {
	{ '*.cshtml', 'set filetype=html' },
	{ '*.do',    'set filetype=sh' },
	{ '*.do',     'inoremap ,ex exec >&2<Cr>' },
	{ '*.do',     'inoremap ,r redo-ifchange<Space>' },
	{ '*.compass', 'set filetype=compass' },

    { '*.har', 'set filetype=json' },

	-- doit build system file
	{ 'dodo.py', 'inoremap ,dep "file_dep": [  ]<Left><Left>' },
	{ 'dodo.py', 'inoremap ,a "actions": [  ]<Left><Left>' },
	{ 'dodo.py', 'inoremap ,tar "targets": [  ]<Left><Left>' },
	{ 'dodo.py', 'inoremap ,doc "doc": ""<Left>' },
	{ 'dodo.py', 'inoremap ,task <esc>:read $DOTFILES/snipfiles/doit_task.py<cr>' },
}

createAugroup(bufEnterAutocmds, 'bufenter', 'BufEnter')

-- Remove trailing whitespace. Use keeppatterns so that
-- the search history isn't ruined with the \v\s+$ junk.
-- Setting the marks is required so that the cursor doesn't jump
-- around.
vim.cmd([[autocmd BufWrite * execute "normal! mz" |  keeppatterns %s/\v\s+$//e | normal `z]])

-- Make sure we are aware of when we are in insert mode.
--vim.cmd([[autocmd InsertEnter * setlocal statusline=%#ErrorMsg#\ INSERT\ %.50F%=%y,C:%c,%p%%,HEX:%B,%{&ff},%{&encoding}]])
--vim.cmd([[autocmd InsertLeave * setlocal statusline=%!g:basestatusline]])

-- vim:foldmethod=marker
