-- Packages
-- From paq-nvim documentation
vim.cmd 'packadd paq-nvim'         -- Load package
local paq = require'paq-nvim'.paq  -- Import module and bind `paq` function
paq { 'savq/paq-nvim', opt=true }  -- Let Paq manage itself

paq 'altercation/vim-colors-solarized'
paq 'arcticicestudio/nord-vim'
paq 'ctrlpvim/ctrlp.vim'
paq 'dag/vim-fish'
paq 'dylon/vim-antlr'
paq 'godlygeek/tabular'
paq 'leafgarland/typescript-vim'
paq 'lervag/vimtex'
paq 'mboughaba/i3config.vim'
paq 'mileszs/ack.vim'
paq 'mitchpaulus/autocorrect.vim'
paq 'mitchpaulus/energyplus-vim'
paq 'mitchpaulus/neobem-vim'
paq 'mitchpaulus/vim-andover-plain-english'
paq 'mitchpaulus/vim-siemens-ppcl'
paq 'nvim-lua/completion-nvim'
paq 'PProvost/vim-ps1'
paq 'qpkorr/vim-bufkill'
paq 'scrooloose/nerdcommenter'
paq 'scrooloose/nerdtree'
paq 'sickill/vim-monokai'
paq 'sjl/gundo.vim'
paq 'tpope/vim-fugitive'
paq 'tpope/vim-surround'

if vim.fn.has('nvim-0.5.0') == 1 then
    paq 'neovim/nvim-lspconfig'

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
    pcall(setupLsp)
end

vim.g.mapleader = ' '
vim.g.maplocalleader = ','

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

vim.api.nvim_set_keymap("i", "jf", "<Esc>", silent  )

normalNoRecurseMappings = {
	-- Fast quitting
	{ 'q', ':q<CR>' },
	{ 'Q', ':q!<CR>' },

	{ 's', ':<C-u>update<CR>' },

	-- Scrolling
	{ "K", "5k"  },
	{ "J", "5j"  },
	-- Need something to remap to join lines
	{ 'gJ', 'J' },

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


vim.api.nvim_set_option('hlsearch', true)   -- highlight search
vim.api.nvim_set_option('incsearch', true)  -- highlight temporary searches
vim.api.nvim_set_option('lazyredraw', true)  -- don't update screen during macros
vim.api.nvim_set_option('scrolloff', 8)
vim.api.nvim_set_option('sidescrolloff', 10)
vim.api.nvim_set_option('hidden', true)  -- Stop asking me to write file
vim.api.nvim_set_option('mouse', 'a')  -- The mouse can be useful
vim.api.nvim_set_option('isfname', '@,48-57,/,\\,.,-,_,+,(,),[,],@-@')  -- Sane filename characters.

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

vim.api.nvim_buf_set_option(0, 'spelllang', 'en_us') -- U.S. only spelling






settings = {


-- nnoremap <leader>sp :<c-u>set paste!<cr>:set paste?<cr>
-- nnoremap <leader>ss :set spell!<cr>:echo "Spell is now " . &spell<cr>
        -- set shellslash
        -- set noshellslash
-- inoremap <F9> <C-o>:set paste<CR><C-r>+<C-o>:set nopaste<CR>
-- nnoremap <F8> :<c-u>set paste!<cr>:set paste?<cr>
-- nnoremap <F9> :<C-u>set paste<CR>"+p:set nopaste<CR>
-- nnoremap <F10> :<C-u>set paste<CR>"+P:set nopaste<CR>
-- nnoremap <leader>ll :set list!<cr>
-- set statusline=%!g:basestatusline
-- set backspace=indent,eol,start " Want backspaces to always work as normal.
-- set smartcase                  " Use smartcase
-- set laststatus=2               " Always show the statusbar
-- set tabstop=4                  " show existing tab with 4 spaces width
-- set shiftwidth=4               " when indenting with '>', use 4 spaces width
-- set expandtab                  " On pressing tab, insert 4 spaces
-- set cmdheight=2                " Make the command window height 2 to avoid the hit-enter prompts
-- set spellsuggest=10
-- set noshowmode                 " My status line already takes of this for me.
-- set sessionoptions=buffers,curdir,winpos,winsize
-- set nolist                     " No special characters by default
-- set listchars=tab:▸\ ,eol:¬    " But provide better characters when requried
-- set guioptions-=e
-- set guioptions-=L
-- set guioptions-=R
-- set completeopt=menuone,noinsert,longest
-- set shortmess+=c
    -- set directory^=$HOME/vimfiles/tmp//
    -- set directory^=$HOME/.vim/tmp//
-- set noswapfile
-- set synmaxcol=200
	-- set grepprg=rg\ --vimgrep
    -- set spellfile=~\vimfiles\spell\hvac.utf-8.add
    -- set spellfile=~/.config/nvim/spell/hvac.utf-8.add
    -- set guifont=Inconsolata\ 12
    -- set guifont=Inconsolata\ 12
    -- set guifont=Menlo\ Regular:h14
    -- set guifont=Fira_Code_Retina:h10:cANSI:qDRAFT,Consolas:h11:cANSI
    -- set renderoptions=type:directx
-- set noshellslash
-- autocmd FileType idf set errorformat=%l:%c\ %m
-- autocmd FileType idf set makeprg=idflint\ %
-- autocmd BufEnter *.cshtml set filetype=html
-- autocmd BufEnter *.do     set filetype=sh
-- autocmd BufEnter *.compass set filetype=compass

}

-- Colorscheme, try monokai
if not pcall(function() vim.cmd('colorscheme monokai') end) then
vim.cmd('colorscheme desert')
end

