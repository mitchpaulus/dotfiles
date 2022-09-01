-- Packages
in_wsl = os.getenv('WSL_DISTRO_NAME') ~= nil

vim.fn["plug#begin"]()

vim.cmd [[ Plug 'altercation/vim-colors-solarized' ]]
vim.cmd [[ Plug 'arcticicestudio/nord-vim' ]]
vim.cmd [[ Plug 'chr4/nginx.vim' ]]
vim.cmd [[ Plug 'ctrlpvim/ctrlp.vim' ]]
vim.cmd [[ Plug 'dag/vim-fish' ]]
vim.cmd [[ Plug 'dylon/vim-antlr' ]]
vim.cmd [[ Plug 'github/copilot.vim' ]]
vim.cmd [[ Plug 'godlygeek/tabular' ]]
vim.cmd [[ Plug 'hrsh7th/vim-vsnip' ]]
vim.cmd [[ Plug 'junegunn/vim-peekaboo' ]]
vim.cmd [[ Plug 'leafgarland/typescript-vim' ]]
vim.cmd [[ Plug 'lervag/vimtex' ]]
vim.cmd [[ Plug 'mboughaba/i3config.vim' ]]
vim.cmd [[ Plug 'mechatroner/rainbow_csv' ]]
vim.cmd [[ Plug 'mileszs/ack.vim' ]]
vim.cmd [[ Plug 'mitchpaulus/autocorrect.vim' ]]
vim.cmd [[ Plug 'mitchpaulus/axon-vim' ]]
vim.cmd [[ Plug 'mitchpaulus/doe2-bdl-vim' ]]
vim.cmd [[ Plug 'mitchpaulus/energyplus-vim' ]]
vim.cmd [[ Plug 'mitchpaulus/mplot.vim' ]]
vim.cmd [[ Plug 'mitchpaulus/neobem-vim' ]]
vim.cmd [[ Plug 'mitchpaulus/vim-andover-plain-english' ]]
vim.cmd [[ Plug 'mitchpaulus/vim-awk-indent-fix' ]]
vim.cmd [[ Plug 'mitchpaulus/vim-siemens-ppcl' ]]
vim.cmd [[ Plug 'mracos/mermaid.vim' ]]
vim.cmd [[ Plug 'nvim-telescope/telescope.nvim' ]]
vim.cmd [[ Plug 'nvim-telescope/telescope-fzf-native.nvim', { 'do': 'make' } ]]
vim.cmd [[ Plug 'nvim-lua/plenary.nvim' ]]
vim.cmd [[ Plug 'PProvost/vim-ps1' ]]
vim.cmd [[ Plug 'rstacruz/vim-closer' ]]
vim.cmd [[ Plug 'scrooloose/nerdcommenter' ]]
vim.cmd [[ Plug 'scrooloose/nerdtree' ]]
vim.cmd [[ Plug 'sickill/vim-monokai' ]]
vim.cmd [[ Plug 'sjl/gundo.vim' ]]
vim.cmd [[ Plug 'subnut/nvim-ghost.nvim', {'do': ':call nvim_ghost#installer#install()'} ]]
vim.cmd [[ Plug 'tpope/vim-fugitive' ]]
vim.cmd [[ Plug 'tpope/vim-surround' ]]
vim.cmd [[ Plug 'unisonweb/unison', { 'branch': 'trunk', 'rtp': 'editor-support/vim' } ]]
vim.cmd [[ Plug 'vmchale/dhall-vim' ]]

vim.cmd [[ Plug 'hrsh7th/cmp-nvim-lsp' ]]
vim.cmd [[ Plug 'hrsh7th/cmp-buffer' ]]
vim.cmd [[ Plug 'hrsh7th/cmp-path' ]]


-- if not in_wsl then load 'hrsh7th/cmp-cmdline'. Seems to break in WSL.
if not in_wsl then vim.cmd [[ Plug 'hrsh7th/cmp-cmdline' ]] end

vim.cmd [[ Plug 'hrsh7th/nvim-cmp' ]]
vim.cmd [[ Plug 'hrsh7th/cmp-vsnip' ]]
vim.cmd [[ Plug 'hrsh7th/vim-vsnip' ]]

vim.cmd [[ Plug 'neovim/nvim-lspconfig' ]]

vim.fn["plug#end"]()

if in_wsl then
    vim.g.clipboard = {
        name = 'wsl clipboard',
        copy =  { ["+"] = { "clip.exe" },   ["*"] = { "clip.exe" } },
        paste = { ["+"] = { "nvim_paste" }, ["*"] = { "nvim_paste" } },
        cache_enabled = true
    }
end

-- Setup nvim-cmp.
local cmp = require'cmp'

cmp.setup({
    completion = { keyword_length = 2 },
    snippet = {
        -- REQUIRED - you must specify a snippet engine
        expand = function(args)
            vim.fn["vsnip#anonymous"](args.body) -- For `vsnip` users.
            -- require('luasnip').lsp_expand(args.body) -- For `luasnip` users.
            -- vim.fn["UltiSnips#Anon"](args.body) -- For `ultisnips` users.
            -- require'snippy'.expand_snippet(args.body) -- For `snippy` users.
        end,
    },
    mapping = {
        -- ['<C-d>'] = cmp.mapping(cmp.mapping.scroll_docs(-4), { 'i', 'c' }),
        -- ['<C-f>'] = cmp.mapping(cmp.mapping.scroll_docs(4), { 'i', 'c' }),
        ['<C-;>'] = cmp.mapping(cmp.mapping.complete(), { 'i', 'c' }),
        ['<C-e>'] = cmp.mapping({
            i = cmp.mapping.abort(),
            c = cmp.mapping.close(),
        }),
        ['<C-y>'] = cmp.mapping.confirm({ select = true }),
        ['<C-p>'] = cmp.mapping.select_prev_item(),
        ['<C-n>'] = cmp.mapping.select_next_item(),
    },
    sources = cmp.config.sources({
        { name = 'nvim_lsp' },
        { name = 'vsnip' }, -- For vsnip users.
    }, {
        { name = 'buffer' },
    })
})

-- Use buffer source for `/` (if you enabled `native_menu`, this won't work anymore).
cmp.setup.cmdline('/', {
    sources = {
        { name = 'buffer' }
    }
})

-- Use cmdline & path source for ':' (if you enabled `native_menu`, this won't work anymore).
if not in_wsl then
    ex_cmdline_sources = cmp.config.sources({{ name = 'path'    }}, {{ name = 'cmdline' }})
    cmp.setup.cmdline(':', { sources = ex_cmdline_sources  })
end

local function setupLsp()
    local nvim_lsp = require('lspconfig')
    local on_attach = function(client, bufnr)
        local function buf_set_keymap(...) vim.api.nvim_buf_set_keymap(bufnr, ...) end
        local function buf_set_option(...) vim.api.nvim_buf_set_option(bufnr, ...) end

        buf_set_option('omnifunc', 'v:lua.vim.lsp.omnifunc')
        -- require'completion'.on_attach()

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
        buf_set_keymap('n', '<space>e', '<cmd>lua vim.diagnostic.get()<CR>', opts)
        buf_set_keymap('n', '[d', '<cmd>lua vim.diagnostic.goto_prev()<CR>', opts)
        buf_set_keymap('n', ']d', '<cmd>lua vim.diagnostic.goto_next()<CR>', opts)
        buf_set_keymap('n', '<space>q', '<cmd>lua vim.diagnostic.setloclist()<CR>', opts)
        buf_set_keymap('n', '<space>la', '<cmd>lua vim.lsp.buf.code_action()<CR>', opts)
        buf_set_keymap('v', '<space>la', '<Esc>:<C-u>lua vim.lsp.buf.range_code_action()<CR>', opts)

        -- Critical to have the noinsert option
        vim.o.completeopt = 'menuone,noinsert'

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
            ]], false)

            vim.api.nvim_create_augroup('LspDocumentHighlight', { clear = true })
            vim.api.nvim_create_autocmd('CursorHold',  { buffer = 0, callback = vim.lsp.buf.document_highlight })
            vim.api.nvim_create_autocmd('CursorMoved', { buffer = 0, callback = vim.lsp.buf.clear_references })
        end
    end

    -- Use a loop to conveniently both setup defined servers
    -- and map buffer local keybindings when the language server attaches
    local servers = { "bashls", "vimls", "texlab", "hls", "pyright", "tsserver", "awk_ls" }
    local capabilities = require('cmp_nvim_lsp').update_capabilities(vim.lsp.protocol.make_client_capabilities())
    for _, lsp in ipairs(servers) do
        -- Setup lspconfig. Update capabilities with nvim-cmp stuff
        nvim_lsp[lsp].setup { on_attach = on_attach, capabilities = capabilities }
    end

    -- OmniSharp stuff
    local omnisharp_bin = "/usr/local/omnisharp/OmniSharp"
    -- check if omnisharp is installed
    if vim.fn.executable(omnisharp_bin) == 1 then
        local pid = vim.fn.getpid()
        nvim_lsp.omnisharp.setup { on_attach = on_attach, capabilities = capabilities, cmd = { omnisharp_bin, "--languageserver", "--hostPID", tostring(pid)  } }
    end
end

-- Wrap this up so we don't fail if we haven't installed the package yet.
local status, err = pcall(setupLsp)
if not status then print(err) end

-- terminal mode mappings
vim.api.nvim_set_keymap("t", "jf", "<C-\\><C-n>" , {noremap = true, silent = true})
-- 'jb' for [j]ump [b]ack
vim.api.nvim_set_keymap("t", "jb", "<C-\\><C-n><C-^>" , {noremap = true, silent = true})

vim.g.mapleader = ' '
vim.g.maplocalleader = ','
vim.g.markdown_fenced_languages = { 'python', 'gnuplot', 'vim', 'sh', 'vim', 'axon', 'lua','haskell', 'neobem', 'awk' }
vim.g.markdown_syntax_conceal = 0

silent = { silent = true, noremap = true }

local function nnmap(lhs, rhs) vim.api.nvim_set_keymap("n", lhs, rhs, silent) end
local function inmap(lhs, rhs) vim.api.nvim_set_keymap("i", lhs, rhs, silent) end
local function cnmap(lhs, rhs) vim.api.nvim_set_keymap("c", lhs, rhs, silent) end
local function vnmap(lhs, rhs) vim.api.nvim_set_keymap("v", lhs, rhs, silent) end

function open_terminal()
    buf_num = vim.fn.bufnr("term:*")
    if buf_num < 0 then vim.cmd("terminal") else vim.cmd("buffer " .. buf_num) end
end

-- These are visual mode mappings to convert Fahrenheit to Celsius and Kelvin
vnmap("<localleader>f2c", "s(<c-r>\" - 32) * 5/9")
vnmap("<localleader>f2k", "s(<c-r>\" + 459.67) * 5/9")

vnmap("<leader>=", ":Tab /=/<CR>")


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

    { 's', '<Cmd>update<CR>' },

    -- Need something to remap to join lines
    { 'gj', 'J' },

    -- Quick mappings for the beginning and ends of lines
    { "H", "^" },
    { "L", "$" },

    -- Telescope mappings
    { '<leader>ff', "<cmd>lua require('telescope.builtin').find_files()<cr>" },
    { '<leader>fg', "<cmd>lua require('telescope.builtin').live_grep()<cr>" },
    { '<leader>fb', "<cmd>lua require('telescope.builtin').buffers()<cr>" },
    { '<leader>fh', "<cmd>lua require('telescope.builtin').help_tags()<cr>" },

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
    { '<F2>', '<Cmd>update<CR>' },
    { '<F4>', 'ZZ' },
    { '<F8>', ':<C-u>set paste!<cr>:set paste?<cr>' },
    { '<F9>',  ':<C-u>set paste<CR>"+p:set nopaste<CR>' },
    { '<F10>', ':<C-u>set paste<CR>"+P:set nopaste<CR>' },

    -- Toggle spell setting
    { '<leader>ss',  ':<C-u>set spell!<CR>:<C-u>echo "Spell is now " . &spell<CR>'  },

    -- Toggle list setting
    { '<leader>ll', ':set list!<cr>' },

    -- I don't use marks, so move q (starting macros) to m (for macros)
    { 'm', 'q' },
    -- Copy entire file to clipboard
    { '<leader>y', '<Cmd>%yank +<CR>' },
    -- Move backwards through spell.
    { 'T', '[s' },
    -- "[B]reak at [c]ommas
    { '<leader>bc', '<Cmd>s/,/\r/g<Cr>' },

    -- Clear the previous search (c[lear] h[ighlight])
    { '<leader>ch', ':nohlsearch<CR>' },

    -- Checktime of the file
    { '<leader>ct', '<Cmd>checktime<cr>' },

    -- Edit [v]imrc, [p]ython utilties
    { '<leader>ev', '<Cmd>edit $MYVIMRC<CR>' },
    { '<leader>ep', '<Cmd>edit $DOTFILES/python/mputils.py<CR>' },
    { '<leader>sv', '<Cmd>source $MYVIMRC | echo "Sourced " . $MYVIMRC<CR>' },

    { '<leader>t', '<Cmd>lua open_terminal()<CR>' },

    -- [j]ump to alternative buffer
    { '<leader>j', '<Cmd>normal <C-^><CR>' },

    -- Remove all stray carriage returns
    { '<leader>cr', '<Cmd>%s/\\r//g<CR>' },

    { '<C-n>', ':bnext<CR>' },

    -- Yank to the end of the line, without the newline
    { 'Y', 'yg_'},

    -- Compile Markdown to PDF using pandoc
    { '<leader>pc',  ':silent !pandoc -V geometry:margin=1in -o "%:p:r.pdf" "%:p"<cr>'  },

    -- Open and close quickfix
    { '<leader>qo', '<Cmd>silent :cw<CR>' },
    { '<leader>qc', '<Cmd>silent :cclose<CR>' },

    -- Re-indent after putting
    { 'p', 'p==' },
    { 'P', 'P==' },

    { '<leader>=', '<Cmd>Tab /=/<CR>' },
}

vim.api.nvim_set_keymap("n", '<leader>g', ':%s/',    { noremap = true, silent = false })
vim.api.nvim_set_keymap("n", '<leader>r', ':read! ', { noremap = true, silent = false })

vim.api.nvim_set_keymap("t", '<C-^>', '<Cmd>execute "norm \\<C-^>"<CR>', { noremap = true, silent = true })

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

    -- Sometimes I also hold the shift key too long.
    { 'jf', '<esc>' },
    { 'Jf', '<esc>' },
    { 'JF', '<esc>' },
    { '<C-BS>', '<C-W>' },
    { '<c-e>', '<c-o>$' },
    { '<c-a>', '<c-o>^' },

    -- HVAC stuff
    { '<localleader>df', '°F' },
    { '<localleader>dp', 'ΔP' },
    { '<localleader>dt', 'ΔT' },

    -- Faster file name completion
    { '<C-F>', '<C-X><C-F>' },

    { '<C-@>', '' },

    -- Function keys, mostly to put in tilde's
    { '<F1>', '`' },
    { '<F2>', '```' },
    { '<F3>', '``<Left>' },
    { '<F4>', '```<CR><CR>```<Esc>kI' },
    { '<F9>', '<C-o>:set paste<CR><C-r>+<C-o>:set nopaste<CR>' },
    -- Often try F10 instead of F9, just do the same pasting in insert mode.
    { '<F10>', '<C-o>:set paste<CR><C-r>+<C-o>:set nopaste<CR>' },


    -- Move to end of line when in insert mode
    { '<C-l>', '<Esc>A' },
    { '<C-j>', '<Esc>/\\V<+\\.\\{-}+><CR>cgn' },

    -- Add undo break points while typing
    { '.', '.<C-g>u'},
    { '=', '=<C-g>u'},
    { '!', '!<C-g>u'},
    { ':', ':<C-g>u'},

    -- I need to use this ALL the time, shell files, etc.
    { '<localleader>ab', 'BEGIN { FS=OFS="\\t" }' },

    -- Company brand standard hex color
    { '<localleader>c', '004987' },

    -- Shebangs
    { '<localleader>sh', '#!/bin/sh' },

    { '<C-Space>', '<Space>' },
}

func_map(function(tbl) inmap(tbl[1], tbl[2]) end, insertModeNoRecurseMappings)

-- https://stackoverflow.com/a/60355468/5932184
-- vim.api.nvim_exec( [[
-- cnoremap <expr> <C-P> wildmenumode() ? "\<C-P>" : "\<Up>"
-- cnoremap <expr> <C-N> wildmenumode() ? "\<C-N>" : "\<Down>"
-- ]], false)

vim.api.nvim_set_keymap("v", '<leader>y', '"+y', silent)
vim.api.nvim_set_keymap("x", 'L', '$', silent)
vim.api.nvim_set_keymap("x", 'H', '^', silent)

vim.api.nvim_exec( [[
" Search for the current visual selection using '*'. See pg. 212 of Practical Vim
function! VSetSearch()
    let temp = @s
    norm! gv"sy
    let @/ = '\V' . substitute(escape(@s, '/\'), '\n', '\\n', 'g')
    let @s = temp
endfunction

xnoremap * :<C-u>call VSetSearch()<CR>/<C-R>=@/<CR><CR>
xnoremap # :<C-u>call VSetSearch()<CR>?<C-R>=@/<CR><CR>
]], false)

-- Use ripgrep instead of grep if available.
if vim.fn.executable('rg') then
    vim.o.grepprg = "rg --vimgrep"
end

vim.api.nvim_exec( [[
" Reload file every second
function! NbemWatch()
    call timer_start(1000, { id -> execute('let l:winview=winsaveview() | checktime | call winrestview(l:winview) ' ) }, { 'repeat': -1 } )
endfunction
]], false)

local statusLineComponents = {
    -- Used to put the mode, but if terminal can change cursor shape, it really isn't required.
    '%f',   -- File name
    '%=',    -- makes following right aligned
    '%y ',   -- file type
    'C:%c ',  -- column number
    '%p%% ',  -- percentage through file
    'HEX:%2B ', -- Hex value for character under cursor
    '%{&ff} ',  -- File format (unix vs. dos)
    '%{&encoding}' -- current encoding
}

vim.o.statusline = table.concat(statusLineComponents)

vim.o.hlsearch = true   -- highlight search
vim.o.incsearch = true  -- highlight temporary searches
vim.o.lazyredraw = true  -- don't update screen during macros
vim.o.scrolloff = 8
vim.o.sidescrolloff = 10
vim.o.hidden = true  -- Stop asking me to write file
vim.o.mouse = 'a'  -- The mouse can be useful
vim.o.isfname = '@,48-57,/,.,-,_,+,,,#,$,%,~,='
vim.o.listchars = 'tab:▸ ,eol:¬,trail:-,nbsp:+'
vim.o.showmode = true
vim.o.shiftround = true
vim.o.spellsuggest = 'best,9'
-- Remove the noinsert option if we aren't in LSP mode.
vim.o.completeopt = 'menu,preview'

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

vim.o.wildignore = wildignorePatterns
vim.o.relativenumber = true        -- Relative line numbering
vim.o.number = true     -- Show the current line number
vim.o.foldmethod = 'marker' -- Never has used manual folds.
vim.o.cursorline = false
vim.o.wrap = false
vim.o.conceallevel = 2 -- Concealed text is completely hidden unless it has a custom replacement character defined
vim.o.scroll = 5
vim.o.spelllang = 'en_us' -- U.S. only spelling
vim.o.expandtab = true -- Yes, I use spaces
vim.o.tabstop = 4      -- Default of 8 is absurd
vim.o.shiftwidth = 0      -- 0 makes this follow tabstop
vim.o.synmaxcol = 300
vim.o.swapfile = false

if os.getenv('DOTFILES') ~= nil then
    vim.o.spellfile = os.getenv('DOTFILES') .. '/vim/spell/hvac.utf-8.add'
end

vim.o.nrformats = 'bin,hex,alpha'

-- Nah, just use desert.  Colorscheme, try monokai
vim.cmd('colorscheme desert')

-- Modern terminals are great am i right?
vim.o.termguicolors = true

-- if not pcall(function() vim.cmd('colorscheme monokai') end) then
-- vim.cmd('colorscheme desert')
-- end

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
vim.g.AutocorrectDisableDefaultMappings = true
vim.api.nvim_set_keymap("n", "<leader>a", "<Plug>(AutocorrectAddToAbbrev)" , {noremap = false, silent = true})

function check(value)    print(vim.inspect(value)) end
function in_lsp_buffer() return next(vim.lsp.buf_get_clients()) ~= nil end
function fix_completeopt()
    if in_lsp_buffer() then
        vim.o.completeopt = 'menuone,noinsert'
    else
        vim.o.completeopt = 'menu,preview'
    end
end

-- NERD Commenter
vim.g.NERDCustomDelimiters = { axon = { left = "//" }, idf = { left = "!" } }
-- I like spaces around my delimiters
vim.g.NERDSpaceDelims = 1

nnmap('<leader>n', ':NERDTree<cr>')
vim.g.NERDTreeIgnore = { '\\.aux.*$','\\.fls$','\\.lof$','\\.toc$','\\.out$','\\.vrb$','\\.nav$','\\.snm$','\\.bbl$','\\.bib','\\.fdb_latexmk$','\\.xdv','\\.gif','\\.pdf','\\~$','\\.blg$','\\.lot$' }

vim.g.copilot_filetypes = {
    fish = false,
}

-- vim-vsnip {{{
-- https://github.com/hrsh7th/vim-vsnip
-- Taken nearly directly out of the README.
vim.api.nvim_exec([[
" NOTE: You can use other key to expand snippet.

" Expand
" imap <expr> <C-j>   vsnip#expandable()  ? '<Plug>(vsnip-expand)'         : '<C-j>'
" smap <expr> <C-j>   vsnip#expandable()  ? '<Plug>(vsnip-expand)'         : '<C-j>'

" Expand or jump
imap <expr> <C-j>   vsnip#available(1)  ? '<Plug>(vsnip-expand-or-jump)' : '<C-j>'
smap <expr> <C-j>   vsnip#available(1)  ? '<Plug>(vsnip-expand-or-jump)' : '<C-j>'

" Jump forward or backward
"imap <expr> <Tab>   vsnip#jumpable(1)   ? '<Plug>(vsnip-jump-next)'      : '<Tab>'
" smap <expr> <Tab>   vsnip#jumpable(1)   ? '<Plug>(vsnip-jump-next)'      : '<Tab>'
imap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'
smap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'

" Select or cut text to use as $TM_SELECTED_TEXT in the next snippet.
" See https://github.com/hrsh7th/vim-vsnip/pull/50
" nmap        s   <Plug>(vsnip-select-text)
" xmap        s   <Plug>(vsnip-select-text)
" nmap        S   <Plug>(vsnip-cut-text)
" xmap        S   <Plug>(vsnip-cut-text)

" If you want to use snippet for multiple filetypes, you can `g:vsnip_filetypes` for it.
let g:vsnip_filetypes = {}
let g:vsnip_filetypes.neobem = ['idf']
let g:vsnip_filetypes.typescriptreact = ['typescript']

]], false)

vim.g.vsnip_snippet_dir = os.getenv('HOME') .. '/.config/vsnip'
vim.g.vsnip_snippet_dirs = { os.getenv('HOME') .. '/.config/vsnip',  os.getenv('HOME') .. '/.vsnip' }
-- }}}
-- ack.vim  {{{2

-- Use ripgrep for searching ⚡️
-- Options include:
-- --vimgrep -> Needed to parse the rg response properly for ack.vim
-- --type-not sql -> Avoid huge sql file dumps as it slows down the search
-- --smart-case -> Search case insensitive if all lowercase pattern, Search case sensitively otherwise
vim.g.ackprg = 'rg --vimgrep --smart-case --type-not sql'

-- Auto close the Quickfix list after pressing '<enter>' on a list item
vim.g.quickfix_auto_close = 1

-- Any empty ack search will search for the work the cursor is on
vim.g.ack_use_cword_for_empty_search = 1

-- Don't jump to first match
vim.cmd [[ cnoreabbrev Ack Ack! ]]

-- Maps <leader>/ so we're ready to type the search keyword
vim.api.nvim_set_keymap("n", '<leader>/', ':<C-u>Ack! ', { noremap = true, silent = false })

-- }}}
-- FileType AutoCmd Mappings {{{1

filetype_autocmds_id = vim.api.nvim_create_augroup('filetype_autocmds', { clear = true })
local function addToFiletypeAugroup(pattern, command)
    vim.api.nvim_create_autocmd('FileType', { pattern = pattern, group = filetype_autocmds_id, command = command })
end

vim.api.nvim_create_autocmd('FileType', { pattern = 'antlr4', group = filetype_autocmds_id, command = 'nnoremap <localleader>c :!antlr4 %<CR>' })

filetypeAutocmds = {
    { 'antlr4', 'nnoremap <localleader>c :!antlr4 %<CR>' },
    { 'antlr4', 'nnoremap <localleader>j :!antlrj<Space>%<CR>', },
    { 'antlr4', 'inoremap <localleader>s STRING : \'\\\' (ESC<bar>.)*? \'\\"\' ;', },

    { 'axon', 'inoremap <localleader>do do<CR>end<Esc>ko' },
    { 'axon', 'inoremap <localleader>ll () =><Esc>3hi' },
    { 'axon', 'inoremap <localleader>ld do<CR><CR>end<Esc>2k$F)i' },
    { 'axon', 'inoremap <localleader>if if () <++> else <++><Esc>F)i' },

    { 'cs', 'inoremap <localleader>l List<><Left>' },
    { 'cs', 'inoremap <localleader>s string' },

    -- make a header 1 line, deleting trailing whitespace first.
    --{ 'markdown', 'nnoremap <silent> <leader>h1 :<c-u>call<Space><SID>MakeHeading("=")<cr>', },
    --{ 'markdown', 'nnoremap <silent> <leader>h2 :<c-u>call<Space><SID>MakeHeading("-")<cr>', },
    -- { 'markdown,tex,text', 'setlocal textwidth=72' },
    { 'markdown,tex,text', 'setlocal spell' },
    { 'markdown', 'setlocal tabstop=2' },
    { 'markdown', 'nnoremap ]] <Cmd>keeppatterns /^#<Cr>' },
    { 'markdown', 'nnoremap <localleader>- <Cmd>keeppatterns s/[^<bar>]/-/g<Cr>' },

    { 'help', 'nnoremap <leader>hh mnA~<esc>`n', },
    { 'help', 'nnoremap <leader>hl mn78i=<esc>`n', },
    { 'help', 'setlocal nospell' },

    { 'json', 'setlocal conceallevel=0' },

    { 'gnuplot', 'nnoremap <localleader>gw :silent !gnuplot.exe % && start "Plot" %:p:r.png<cr>', },
    { 'gnuplot', 'nnoremap <localleader>gu :!gnuplot %; and wsl-opener %:p:r.png<cr>', },
    { 'gnuplot', 'nnoremap <localleader>c :silent !gnuplot.exe % && start "Plot" %:p:r.png<cr>', },
    { 'gnuplot', 'nnoremap <localleader>k :silent !taskkill.exe /IM Microsoft.Photos.exe /F<cr>', },
    { 'gnuplot', 'inoremap ,hist <esc>:0read ~/.vim/snipfiles/hist.gnuplot<cr>', },

    { 'make', 'inoremap ,p .PHONY :<Space>', },

    -- Quickly enter in ² symbol
    { 'markdown,text', 'inoremap ^2 <c-v>178', },
    { 'markdown,text', 'inoremap ,l [](<++>)<esc>6hi', },
    { 'markdown,text', 'inoremap ,c ✓', },
    { 'markdown,text', 'inoremap ,x ✗', },
    -- Quickly enter in °F
    { 'markdown,text', 'inoremap DEGF °F', },
    { 'markdown,text', 'inoremap <localleader>y 2022-', },

    { 'markdown', 'inoremap <localleader>aj (adj.)', },
    { 'markdown', 'inoremap <localleader>b ****<Left><Left>', },
    { 'markdown', 'inoremap <localleader>e $$  $$<Esc>2hi', },
    { 'markdown', 'inoremap <localleader>fi ![]()<Esc>2hi', },
    { 'markdown', 'inoremap <localleader>fr \\frac{}{}<esc>2hi', },
    { 'markdown', 'inoremap <localleader>i **<Left>', },
    { 'markdown', 'inoremap <localleader>m $$<Left>', },
    { 'markdown', 'inoremap <localleader>n \\begin{equation}<CR>\\end{equation}<Esc>0ko', },
    { 'markdown', 'inoremap <localleader>u _{}<Left>', },
    { 'markdown', 'vnoremap <localleader>b s**<c-r>"**' },
    { 'markdown', 'vnoremap <localleader>i s*<c-r>"*' },
    { 'markdown', 'vnoremap <localleader>l s[<c-r>"]()<Left>' },

    { 'gitcommit', 'setlocal spell' },

    { 'html', 'inoremap ,1 <h1></h1><Esc>4hi', },
    { 'html', 'inoremap ,2 <h2></h2><Esc>4hi', },
    { 'html', 'inoremap ,3 <h3></h3><Esc>4hi', },
    { 'html', 'inoremap ,a <a href=""></a><Esc>5hi', },
    { 'html', 'inoremap ,b data-bind=""<Left>', },
    { 'html', 'inoremap ,c class=""<Left>', },
    { 'html', 'inoremap ,d <div></div><Esc>5hi', },
    { 'html', 'inoremap ,i <input  /><Esc>2hi', },
    { 'html', 'inoremap ,l <label></label><Esc>7hi', },
    { 'html', 'inoremap ,p <lt>p></p><Esc>3hi', },
    { 'html', 'inoremap ,sp <span></span><Esc>6hi', },
    { 'html', 'inoremap ,st <style></style><Esc>7hi', },
    { 'html', 'inoremap ,u <ul><cr><li></li><cr></ul><Esc>k^f>a', },
    { 'html', 'vnoremap <localleader>p :! pandoc --to=html -<CR><Esc>' },

    { 'javascript,typescript', 'inoremap ,f function (<++>) {<cr><++><cr>}<Esc>2k^f(i', },
    { 'javascript,typescript', 'inoremap ,> () =><Space>', },

    { 'typescript', 'nnoremap <leader>tc <Cmd>!tsc<cr>', },

    { 'tex', 'setlocal conceallevel=0' },
    { 'tex', 'inoremap %%%', [[\%]] },
    { 'tex', 'inoremap ,ab \\begin{abstract}<Cr><Cr>\\end{abstract}<Esc>k0i', },
    { 'tex', 'inoremap ,au \\author{}<Left>', },
    { 'tex', 'inoremap ,base <esc>:0read $DOTFILES/snipfiles/base.tex<cr>', },
    { 'tex', 'inoremap ,bf \\textbf{} <++><esc>5hi', },
    { 'tex', 'inoremap ,co \\newcommand{\\}{<++>}<esc>6hi', },
    { 'tex', 'inoremap ,dot \\dot{} <++><esc>5hi', },
    { 'tex', 'inoremap ,en \\begin{enumerate}<cr><cr>\\end{enumerate}<esc>ki    <esc>i', },
    { 'tex', 'inoremap ,eq \\begin{equation}<cr><cr>\\end{equation}<esc>ki    <esc>i', },
    { 'tex', 'inoremap ,ei \\(\\)<esc>hi' },
    { 'tex', 'inoremap ,fig \\includegraphics{}<Left>', },
    { 'tex', 'inoremap ,fr \\frac{}{}<esc>2hi', },
    { 'tex', 'inoremap ,h \\title{}<Left>', },
    { 'tex', 'inoremap ,i \\item <esc>a', },
    { 'tex', 'inoremap ,lr \\left(\\right) <++><esc>11hi', },
    { 'tex', 'inoremap ,ms \\section{}<Left>', },
    { 'tex', 'inoremap ,mt \\maketitle{}<Cr>', },
    { 'tex', 'inoremap ,p \\usepackage{}<esc>i', },
    { 'tex', 'inoremap ,rm \\textrm{}<Left>', },
    { 'tex', 'inoremap ,s ^{}<esc>i', },
    { 'tex', 'inoremap ,tab \\begin{tabular}{}<cr><++><cr>\\end{tabular}<esc>2k^2f{a', },
    { 'tex', 'inoremap ,tx \\text{} <++><esc>5hi', },
    { 'tex', 'inoremap ,u _{}<Left>', },
    { 'tex', 'nnoremap ,base :0read $DOTFILES/snipfiles/base.tex<cr>', },
    { 'tex', 'nnoremap [e ?\\begin{equation}<cr>:nohlsearch<cr>', },
    { 'tex', 'nnoremap ]e /\\begin{equation}<cr>:nohlsearch<cr>', },
    { 'tex', 'vnoremap <localleader>b s\\textbf{<c-r>"}' },
    { 'tex', 'vnoremap <localleader>p :! pandoc --to=latex -<CR><Esc>' },
    -- vimtex has a mapping lL for compiling selected, so use two-char mapping here.
    { 'tex', 'vnoremap <localleader>li s\\href{}{<c-r>"}<Esc>2F{a' },
    { 'tex', 'vnoremap <localleader>i s\\textit{<c-r>"}<Esc>' },
    { 'tex', 'vnoremap <localleader>lr s\\left(<c-r>"\\right)<Esc>' },

    { 'awk', 'inoremap ,! #!/usr/bin/awk -E<cr>', },
    { 'awk', 'inoremap ,b BEGIN { FS=OFS="" }<esc>2hi', },
    { 'awk', 'inoremap ,for for (i = ; i <= <++>; i++) {<cr><++><cr>}<esc>2k^f;i', },
    { 'awk', 'inoremap ,fi for (<+var+> in <+array+>) {<cr><++><cr>}<esc>2k^f;i', },
    { 'awk', 'inoremap ,if if () {<cr><++><cr>}<esc>2k^f(a', },
    { 'awk', 'inoremap ,pf printf("")<esc>hi', },
    { 'awk', 'inoremap ,sh #!/usr/bin/awk -E<CR>', },
    { 'awk', 'inoremap <localleader>q \\"', },
    { 'awk', 'inoremap <localleader>sp split(<+string+>, <+array+>, <+FS+>)<Esc>35hi', },
    { 'awk', 'setlocal path+=$DOTFILES/awk_functions' },
    { 'awk', 'nnoremap <localleader>h i<C-r>=system("headers2awk -c", @+)<Cr>' },

    { 'sh', 'inoremap ,sh #!/bin/sh<CR>', },
    { 'sh,bash', 'nnoremap <localleader>h :read $DOTFILES/snipfiles/shell_help.sh<Cr>', },
    { 'sh,bash', 'inoremap <localleader>h <cmd>read $DOTFILES/snipfiles/shell_help.sh<Cr>', },
    { 'sh,bash', 'nnoremap <localleader>s <cmd>!shellcheck "%"<Cr>', },
    { 'sh,fish,bash', 'inoremap ,v "$"<Left>', },

    { 'matlab', 'inoremap ,f function [output] = functionname(inputvariable)<CR><CR>end<Esc>2k', },

    { 'make', 'inoremap ,v $()<Left>', },

    { 'idf', 'inoremap <localleader>i ! INCLUDE<Space>', },
    { 'idf', 'inoremap <localleader>r Replace ECM ::', },
    { 'idf', 'inoremap <localleader>de Delete ECM', },
    { 'idf', 'nnoremap <localleader>s /<C-r>*\\c<CR>', },
    { 'idf', 'set errorformat=%l:%c\\ %m', },
    { 'idf', 'set makeprg=idflint\\ %', },
    { 'idf,neobem', 'inoremap <localleader>l λ', },
    { 'idf,neobem', 'nnoremap <localleader>t :Tabularize /!-\\?/l1l1<CR>', },
    { 'neobem', 'nnoremap <localleader>c :!nbem -o %:t:r.idf %<CR>', },
    { 'neobem', 'nnoremap <localleader>f <cmd>%!nbem -f %<CR>', },
    { 'neobem', 'nnoremap <localleader>d <cmd>%!nbem -f --doe2 %<CR>', },
    { 'neobem', 'inoremap <localleader>f λ  { <++> }<Esc>8hi', },
    { 'neobem', 'inoremap <localleader>r <  ><Esc>hi', },
    { 'neobem', 'inoremap <localleader>c ✓', },

    { 'python', 'iabbrev l lambda' },
    { 'python', 'iabbrev r return' },
    { 'python', 'inoremap <localleader>di def __init__(self) -> None:<Esc>F)i' },
    { 'python', 'inoremap <localleader>im if __name__ == "__main__":<Cr>' },
    { 'python', 'inoremap <localleader>mp import mputils' },
    { 'python', 'inoremap <localleader>sh #!/usr/bin/env python3' },
    { 'python', 'inoremap <localleader>wo with open(\'\') as file:<Esc>F\'i' },
    { 'python', 'nnoremap <localleader>ga vip:!python_class_gen -a<CR>' },
    { 'python', 'nnoremap <localleader>gc vip:!python_class_gen<CR>' },
    { 'python', 'xnoremap <localleader>sl s[str(l) for l in <C-r>"]' },
    { 'python', 'xnoremap <localleader>e senumerate(<C-r>")<Left>' },

    { 'python,nbem', 'iabbrev improt import', },

    { 'compass', 'inoremap <localleader>b <!-- Compass:  --><CR><CR><!-- Compass --><Esc>2k0f:la', },

    { 'ce', 'inoremap <localleader>p \\prop{}<Left>' },
}

for _, autocmd in pairs(filetypeAutocmds) do
    addToFiletypeAugroup(autocmd[1], autocmd[2])
end

-- Event Type Autocmds {{{1
bufEnterAutocmds = {
    { '*.cshtml' , 'set filetype=html' },
    { '*.do'     , 'set filetype=sh' },
    { '*.do'     , 'inoremap ,ex exec >&2<Cr>' },
    { '*.do'     , 'inoremap ,r redo-ifchange<Space>' },
    { '*.compass', 'set filetype=compass' },
    { '*.gnuplot', 'set filetype=gnuplot'},
    { '*.har'    , 'set filetype=json' },
    { '*.ce'     , 'set filetype=ce' },
    { '.gitignore', 'set filetype=conf' }, -- close enough
    { '.gitignore', 'inoremap ,dt :read !do-targets' },

    -- The Windows Terminal settings file ('settings.json') is JSON5 with comments.
    -- jsonc filetype seems to handle it alright.
    { 'settings.json', 'set ft=jsonc' },

    -- doit build system file
    { 'dodo.py', 'inoremap ,dep "file_dep": [  ]<Left><Left>' },
    { 'dodo.py', 'inoremap ,a "actions": [  ]<Left><Left>' },
    { 'dodo.py', 'inoremap ,tar "targets": [  ]<Left><Left>' },
    { 'dodo.py', 'inoremap ,doc "doc": ""<Left>' },
    { 'dodo.py', 'inoremap ,task <esc>:read $DOTFILES/snipfiles/doit_task.py<cr>' },

    -- This is a function defined here, to make sure the completeopt option is
    -- updated properly for whether we're in a LSP setting or not.
    { '*', 'lua fix_completeopt()' },
}

bufenter_augroup_id = vim.api.nvim_create_augroup('bufenter_augroup', { clear = true })
for _, autocmd in ipairs(bufEnterAutocmds) do
    vim.api.nvim_create_autocmd('BufEnter', { pattern = autocmd[1], group = bufenter_augroup_id, command = autocmd[2] })
end


vim.api.nvim_create_augroup('MPEvents', { clear = true })
vim.api.nvim_create_autocmd('TermOpen', { pattern = '*',        group = 'MPEvents', command = 'setlocal nonumber norelativenumber | startinsert | echom "Term Open.."' })
vim.api.nvim_create_autocmd('BufEnter', { pattern = "term://*", group = 'MPEvents', command = 'startinsert' })
vim.api.nvim_create_autocmd('TextYankPost', { pattern = '*', group = 'MPEvents', command = 'silent! lua vim.highlight.on_yank { timeout = 500 }' })

-- Remove trailing whitespace. Use keeppatterns so that
-- the search history isn't ruined with the \v\s+$ junk.
-- Setting the marks is required so that the cursor doesn't jump
-- around.
-- vim.cmd([[autocmd BufWrite * execute "normal! mz" |  keeppatterns %s/\v\s+$//e | normal `z]])
vim.api.nvim_create_autocmd('BufWrite', { pattern = '*', group = 'MPEvents', command = 'execute "normal! mz" |  keeppatterns %s/\\v\\s+$//e | normal `z' })

function remove_trailing_blank_lines()
    -- Get number of lines in buffer. 0 is only for unloaded buffer.
    local line_count = vim.api.nvim_buf_line_count(0)
    if line_count < 2 then return end

    -- Get contents of final line
    local last_line = vim.api.nvim_buf_get_lines(0, -2, -1, false)[1]
    -- If it's blank or whitespace, delete it
    if last_line:match('^%s*$') then
        vim.api.nvim_buf_set_lines(0, -2, -1, false, {})
        -- recurse until no more blank lines
        remove_trailing_blank_lines()
    end
end

-- Remove trailing blank lines of save
vim.api.nvim_create_autocmd('BufWrite', { pattern = '*', group = 'MPEvents', callback = remove_trailing_blank_lines })

-- Determine the syntax group and resulting highlight gruop under the cursor
function syngroup()
    syn_id = vim.fn.synID(vim.fn.line('.'), vim.fn.col('.'), true)
    print(vim.fn.synIDattr(syn_id, 'name') .. ' -> ' .. vim.fn.synIDattr(vim.fn.synIDtrans(syn_id), 'name'))
end
vim.api.nvim_create_user_command('Syngroup', syngroup, { nargs = 0 })

-- Make sure we are aware of when we are in insert mode.
--vim.cmd([[autocmd InsertEnter * setlocal statusline=%#ErrorMsg#\ INSERT\ %.50F%=%y,C:%c,%p%%,HEX:%B,%{&ff},%{&encoding}]])
--vim.cmd([[autocmd InsertLeave * setlocal statusline=%!g:basestatusline]])

-- vim:foldmethod=marker
