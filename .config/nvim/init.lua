vim.g.mapleader = ' '
vim.g.maplocalleader = ','

silent = { silent = true, noremap = true }

local function nnmap(lhs, rhs)
	vim.api.nvim_set_keymap("n", lhs, rhs, silent)
end

-- https://stackoverflow.com/a/11671820/5932184
local function func_map(f, tbl)
	local t = {}
	for k,v in pairs(tbl) do
		t[k] = f(v)
	end
	return t
end


--[[ "Use jk to escape insert mode. Suggested here:
"http://learnvimscriptthehardway.stevelosh.com/chapters/10.html
"inoremap jk <esc>
" Now switching to jf for a few reasons:
" 1. jk stills causes some RSI problems
" 2. df and fd were annoying since there are many words that end with
"    either of those characters. The biggest offender was f in if statements.
" 3. j is the best leader character, since almost no words end with that.
" 4. So jf splits the duty between both hands using strong pointer finger.  ]]

vim.api.nvim_set_keymap("i", "jf", "<Esc>", silent  )

normalNoRecurseMappings = {
	-- Fast quitting
	{ 'q', ':q<CR>' },

	{ 's', ':<C-u>update<CR>' },

	-- Scrolling
	{ "K", "5k"  },
	{ "J", "5j"  },

	-- Quick mappings for the beginning and ends of lines
	{ "H", "^" },
	{ "L", "$" },

	-- These mappings are for moving around the windows quickly.
	{ '<C-h>', '<c-w>h' },
	{ '<C-j>', '<c-w>j' },
	{ '<C-k>', '<c-w>k' },
	{ '<C-l>', '<c-w>l' },

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

vim.api.nvim_set_option('hlsearch', true)   -- highlight search
vim.api.nvim_set_option('incsearch', true)  -- highlight temporary searches
vim.api.nvim_set_option('lazyredraw', true)  -- don't update screen during macros
vim.api.nvim_set_option('scrolloff', 8)
vim.api.nvim_set_option('sidescrolloff', 10)
vim.api.nvim_set_option('hidden', true)  -- Stop asking me to write file
vim.api.nvim_set_option('mouse', 'a')  -- The mouse can be useful


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
-- set isfname-={
-- set isfname-=}
-- set isfname-==
-- set wildignore+=*.aux*
-- set wildignore+=*.asv
-- set wildignore+=*.log
-- set wildignore+=*.swp
-- set wildignore+=*.nav
-- set wildignore+=*.toc
-- set wildignore+=*.out
-- set wildignore+=*.fdb_latexmk
-- set wildignore+=*.blg
-- set wildignore+=*.fls
-- set wildignore+=*.xdv
-- set wildignore+=*.bbl
-- set wildignore+=*.snm
-- set wildignore+=*.lof
-- set wildignore+=*.lot
-- set wildignore+=*.dvi
-- set wildignore+=*.tmp
-- set wildignore+=*.synctex.gz
-- set wildignore+=*/node_modules/*
-- set wildignore+=*/.git/*
-- set wildignore+=*/venv/*
-- set noshellslash
-- autocmd FileType idf set errorformat=%l:%c\ %m
-- autocmd FileType idf set makeprg=idflint\ %
-- autocmd BufEnter *.cshtml set filetype=html
-- autocmd BufEnter *.do     set filetype=sh
-- autocmd BufEnter *.compass set filetype=compass

}


