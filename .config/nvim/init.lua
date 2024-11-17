-- Packages
in_wsl = os.getenv('WSL_DISTRO_NAME') ~= nil

in_windows = vim.fn.has('win32') == 1

-- Moved all my plugins to $HOME/.vim/pack/mp/start.
-- This way, I can clone them down directly with SSH, and can work on them live.
-- vim.cmd [[ Plug 'mitchpaulus/autocorrect.vim' ]]
-- vim.cmd [[ Plug 'mitchpaulus/axon-vim' ]]
-- vim.cmd [[ Plug 'mitchpaulus/doe2-bdl-vim' ]]
-- vim.cmd [[ Plug 'mitchpaulus/energyplus-vim' ]]
-- vim.cmd [[ Plug 'mitchpaulus/genopt.vim' ]]
-- vim.cmd [[ Plug 'mitchpaulus/mplot.vim' ]]
-- vim.cmd [[ Plug 'mitchpaulus/neobem-vim' ]]
-- vim.cmd [[ Plug 'mitchpaulus/OpenStudio.vim' ]]
-- vim.cmd [[ Plug 'mitchpaulus/vim-andover-plain-english' ]]
-- vim.cmd [[ Plug 'mitchpaulus/vim-awk-indent-fix' ]]
-- vim.cmd [[ Plug 'mitchpaulus/vim-siemens-ppcl' ]]
-- vim.cmd [[ Plug 'mitchpaulus/xlim-vim' ]]

if in_wsl then
    vim.g.clipboard = {
        name = 'wsl clipboard',
        copy =  { ["+"] = { "wsl_clip" },   ["*"] = { "wsl_clip" } },
        paste = { ["+"] = { "nvim_paste" }, ["*"] = { "nvim_paste" } },
        cache_enabled = true
    }
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
        buf_set_keymap('n', 'gh', '<Cmd>lua vim.lsp.buf.hover()<CR>', opts)
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
        buf_set_keymap('n', '<localleader>d', '<cmd>lua vim.diagnostic.setqflist()<CR>', opts)
        buf_set_keymap('n', '<space>la', '<cmd>lua vim.lsp.buf.code_action()<CR>', opts)
        buf_set_keymap('v', '<space>la', ':lua vim.lsp.buf.code_action()<CR>', opts)

        -- Critical to have the noinsert option
        -- vim.o.completeopt = 'menuone,noinsert'

        -- Set some keybinds conditional on server capabilities
        if client.server_capabilities.documentFormattingProvider then
            buf_set_keymap("n", "<space>i", "<cmd>lua vim.lsp.buf.formatting()<CR>", opts)
        elseif client.server_capabilities.documentRangeFormattingProvider then
            buf_set_keymap("v", "<space>i", "<cmd>lua vim.lsp.buf.range_formatting()<CR>", opts)
        end

        -- Set autocommands conditional on server_capabilities
        -- To see all capabilities of your language server run
        -- :lua =vim.lsp.get_active_clients()[1].server_capabilities
        if client.server_capabilities.documentHighlightProvider then
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
    local servers = { "bashls", "vimls", "hls", "pyright", "ts_ls", "awk_ls", "gopls" }
    -- local servers = { "bashls", "vimls", "texlab", "hls", "tsserver", "awk_ls" }
    -- local capabilities = require('cmp_nvim_lsp').default_capabilities(vim.lsp.protocol.make_client_capabilities())
    -- local capabilities =
    for _, lsp in ipairs(servers) do
        -- Setup lspconfig. Update capabilities with nvim-cmp stuff
        -- nvim_lsp[lsp].setup { on_attach = on_attach, capabilities = capabilities }
        nvim_lsp[lsp].setup { on_attach = on_attach }
    end

    -- OmniSharp stuff
    local omnisharp_bin = "/usr/local/omnisharp/OmniSharp"
    -- check if omnisharp is installed
    if vim.fn.executable(omnisharp_bin) == 1 then
        local pid = vim.fn.getpid()
        nvim_lsp.omnisharp.setup { on_attach = on_attach, capabilities = capabilities, cmd = { omnisharp_bin, "--languageserver", "--hostPID", tostring(pid)  } }
    end
end

-- Setup lsp for xlim, custom language.
-- executable is 'xlimlsp'
function setup_xlimlsp()
    name = 'xlim-lsp'
    cmd = {'xlimlsp'}
    -- set root dir to current directory
    root_dir = vim.fn.getcwd()
    vim.lsp.start({
        cmd = cmd,
        name = name,
        root_dir = root_dir,
    })

    -- Set buf keymap gh to hover
    vim.api.nvim_buf_set_keymap(0, 'n', 'gh', '<Cmd>lua vim.lsp.buf.hover()<CR>', { noremap=true, silent=true })
    -- buf_set_keymap('n', 'gd', '<Cmd>lua vim.lsp.buf.definition()<CR>', opts)
    -- set keymap gd to definition
    vim.api.nvim_buf_set_keymap(0, 'n', 'gd', '<Cmd>lua vim.lsp.buf.definition()<CR>', { noremap=true, silent=true })
    vim.api.nvim_buf_set_keymap(0, 'n', '[d', '<Cmd>lua vim.diagnostic.goto_prev()<CR>', { noremap=true, silent=true })
    vim.api.nvim_buf_set_keymap(0, 'n', ']d', '<Cmd>lua vim.diagnostic.goto_next()<CR>', { noremap=true, silent=true })
    vim.api.nvim_buf_set_keymap(0, 'n', '<localleader>d', '<Cmd>lua vim.diagnostic.setqflist()<CR>', { noremap=true, silent=true })
    vim.api.nvim_buf_set_keymap(0, 'n', 'gr', '<Cmd>lua vim.lsp.buf.references()<CR>', { noremap=true, silent=true })
end


function extmark_test()
    ns = vim.api.nvim_create_namespace("xlim")
    vim.api.nvim_buf_set_extmark(0, ns, 0, 0, {
        virt_text = {{"  test hello", "Comment"}},
        virt_text_pos = "eol",
    })
end

function clear_xlim_marks()
    ns = vim.api.nvim_create_namespace("xlim")
    vim.api.nvim_buf_clear_namespace(0, ns, 0, -1)
end

function get_xlim_marks()
    -- Run external command 'xlim $file' and parse output
    local file = vim.fn.expand("%:p")
    -- Use cmd as list to run directly without shell
    local cmd = { "xlim", "--line-nums", file }

    -- Do asyncrounous call to xlim using Neovim jobs. Use buffered output, waiting for entire job to finish
    local job_id = vim.fn.jobstart(cmd, {
        stdout_buffered = true,
        stderr_buffered = true,
        on_stdout = function(_, data, _)
            -- Clear existing marks
            clear_xlim_marks()

            -- Parse output of xlim
            for _, line in ipairs(data) do
                -- Split line into line number and text. Tab separated
                local line_num, text = string.match(line, "(%d+)\t(.*)")

                if line_num ~= nil and text ~= nil then
                    -- parse line_num to number
                    line_num = tonumber(line_num)

                    -- Create extmark
                    ns = vim.api.nvim_create_namespace("xlim")
                    vim.api.nvim_buf_set_extmark(0, ns, line_num - 1, 0, {
                        virt_text = {{text, "Comment"}},
                        virt_text_pos = "eol",
                    })
                end
            end
        end,
        on_stderr = function(_, data, _)
            -- Print error message
            print(table.concat(data, "\n"))
        end,
    })
end

-- Make extmark_test() as command
vim.api.nvim_create_user_command("ExtmarkTest", extmark_test, { nargs = 0 })


-- Wrap this up so we don't fail if we haven't installed the package yet.
local status, err = pcall(setupLsp)
if not status then print(err) end

-- terminal mode mappings
vim.api.nvim_set_keymap("t", "jf", "<C-\\><C-n>" , {noremap = true, silent = true})
-- 'jb' for [j]ump [b]ack
vim.api.nvim_set_keymap("t", "jb", "<C-\\><C-n><C-^>" , {noremap = true, silent = true})

vim.g.mapleader = ' '
vim.g.maplocalleader = ','
vim.g.markdown_fenced_languages = { 'python', 'gnuplot', 'vim', 'sh', 'vim', 'axon', 'lua','haskell', 'neobem', 'awk', 'xlim' }
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
    { '<leader>fg', "<cmd>lua require('telescope.builtin').git_files()<cr>" },
    { '<leader>fc', "<cmd>lua require('telescope.builtin').lsp_document_symbols()<cr>" },

    -- { '<leader>fg', "<cmd>lua require('telescope.builtin').live_grep()<cr>" },
    -- { '<leader>fb', "<cmd>lua require('telescope.builtin').buffers()<cr>" },
    -- { '<leader>fh', "<cmd>lua require('telescope.builtin').help_tags()<cr>" },

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

    -- This matches default kakoune mappings
    { '<M-i>', 'vi' },
    { '<M-a>', 'va' },

    { '<M-f>', 'E' }, -- Match emacs
    { '<M-b>', 'B' }, -- Match emacs

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

    -- Reformat my special date codes
    { '<leader>d', '<Cmd>%!datecode<cr>' },

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
    { '<C-p>', ':bprev<CR>' },

    -- Yank to the end of the line, without the newline
    { 'Y', 'yg_'},

    -- Compile Markdown to PDF using pandoc
    { '<leader>pc',  ':silent !pandoc -V geometry:margin=1in -o "%:p:r.pdf" "%:p"<cr>'  },

    -- Open and close quickfix
    { '<localleader>o', '<Cmd>silent :cw<CR>' },
    { '<localleader>c', '<Cmd>silent :cclose<CR>' },

    -- Re-indent after putting
    { 'p', 'p==' },
    { 'P', 'P==' },

    { '<leader>=', '<Cmd>Tab /=/<CR>' },

    -- Show full file name when requested
    { '<C-G>', '1<C-G>' },

    -- For emacs like movement
    { '<C-a>', '0' },
    { '<C-e>', '$' },
    { '<C-b>', 'h' },
    { '<C-f>', 'l' },
    { '<C-v>', '<C-f>' },
    { '<M-v>', '<C-b>' },
}

local insertLikeCmds = { 'i', 'a', 'I', 'A', 'o', 'O' }

-- Check for file changes before insertion
-- Use count for i if required
for _, cmd in ipairs(insertLikeCmds) do
    vim.api.nvim_set_keymap("n", cmd, "':<C-u>checktime<CR>' . (v:count > 0 ? v:count : '') . '" .. cmd .. "'", { noremap = true, silent = true, expr = true })
end

vim.api.nvim_set_keymap("n", '<leader>gs', ':%s/',    { noremap = true, silent = false })
vim.api.nvim_set_keymap("n", '<leader>ge', ':Copilot enable<CR>',    { noremap = true, silent = false })
vim.api.nvim_set_keymap("n", '<leader>gd', ':Copilot disable<CR>',    { noremap = true, silent = false })
vim.api.nvim_set_keymap("n", '<leader>r', ':read! ', { noremap = true, silent = false })

vim.api.nvim_set_keymap("t", '<C-^>', '<Cmd>execute "norm \\<C-^>"<CR>', { noremap = true, silent = true })

-- Need visual mode mapping to insert '- ' at the beginning of each line to make into markdown list
vim.api.nvim_set_keymap("v", "<localleader>-", ":s/^/- /<CR>", { noremap = true, silent = true })

func_map(function(tbl) nnmap(tbl[1], tbl[2]) end, normalNoRecurseMappings)

-- Insert Mode mappings
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
    { 'j;', '<Plug>(copilot-suggest)' },
    { 'jl', '<Plug>(copilot-accept-line)' },
    { 'jk', '<Plug>(copilot-accept-word)' },
    { 'jn', '<Plug>(copilot-next)' },
    { 'jc', '<Plug>(copilot-dismiss)' },
    { '<C-BS>', '<C-W>' },
    { '<c-e>', '<c-o>$' },
    { '<c-a>', '<c-o>^' },

    -- HVAC stuff
    { '<localleader>df', '°F' },
    { '<localleader>dp', 'ΔP' },
    { '<localleader>dt', 'ΔT' },

    -- Some greek
    { '<localleader>e', 'η' },
    { '<localleader>mu', 'μ' },
    { '<localleader>pi', 'π' },
    { '<localleader>sigma', 'σ' },

    -- Faster file name completion
    -- { '<C-F>', '<C-X><C-F>' },

    { '<C-@>', '' },

    -- Function keys, mostly to put in tilde's.
    -- <C-g>u makes sure I can undo the command if I accidentally press wrong F key.
    { '<F1>', '`' },
    { '<F2>', '```' },
    { '<F3>', '<C-g>u``<Left>' },
    { '<F4>', '<C-g>u```<CR><CR>```<Esc>kI' },
    { '<F9>', '<C-g>u<C-o>:set paste<CR><C-r>+<C-o>:set nopaste<CR>' },
    -- Often try F10 instead of F9, just do the same pasting in insert mode.
    { '<F10>', '<C-g>u<C-o>:set paste<CR><C-r>+<C-o>:set nopaste<CR>' },


    -- Move to end of line when in insert mode
    { '<C-l>', '<Esc>A' },

    -- Add undo break points while typing
    { '.', '.<C-g>u'},
    { '=', '=<C-g>u'},
    { '!', '!<C-g>u'},
    { ':', ':<C-g>u'},
    { '-', '-<C-g>u'},

    -- I need to use this ALL the time, shell files, etc.
    { '<localleader>ab', 'BEGIN { FS=OFS="\\t" }' },

    -- Company brand standard hex color
    { '<localleader>c', '004987' },

    -- Shebangs
    { '<localleader>sh', '#!/bin/sh<Esc>:set ft=sh<CR>' },
    { '<localleader>sp', '#!/usr/bin/env python3<Esc>:set ft=python<Cr>A<Cr><Cr>' },

    -- { '<C-Space>', '<C-x><C-o>' },
    --
    -- Emacs
    { '<C-b>', '<Left>' },
    { '<M-b>', '<Esc>Bi' },
    -- { '<C-f>', '<Right>' }, used for <C-x><C-f> filename completion.
}

-- Command line mappings, mostly to match emacs/shell like defaults.
-- https://stackoverflow.com/a/60355468/5932184
vim.api.nvim_set_keymap("c", "<C-p>", [[ wildmenumode() ? "\<C-p>" : "\<Up>" ]], { noremap = true, expr = true  })
vim.api.nvim_set_keymap("c", "<C-n>", [[ wildmenumode() ? "\<C-n>" : "\<Down>"]], { noremap = true, expr = true })
vim.api.nvim_set_keymap("c", "<C-b>", "<Left>", { noremap = true })
vim.api.nvim_set_keymap("c", "<C-f>", "<Right>", { noremap = true })
vim.api.nvim_set_keymap("c", "<C-a>", "<C-b>", { noremap = true })
vim.api.nvim_set_keymap("c", "<M-f>", "<S-Right>", { noremap = true })
vim.api.nvim_set_keymap("c", "<M-b>", "<S-Left>", { noremap = true })

func_map(function(tbl) inmap(tbl[1], tbl[2]) end, insertModeNoRecurseMappings)

vim.api.nvim_set_keymap("i", "<C-n>", [[pumvisible() ? "\<C-n>" : "\<C-o>:set completeopt=menu\<Cr>\<C-n>"]], { noremap = true, silent = true, expr = true })
vim.api.nvim_set_keymap("i", "<C-f>", [[pumvisible() ? "\<C-f>" : "\<C-o>:set completeopt=menu\<Cr>\<C-x>\<C-f>"]], { noremap = true, silent = true, expr = true })
vim.api.nvim_set_keymap("i", "<C-Space>", [[pumvisible() ? "\<Space>" : "\<Esc>:set completeopt=menuone,noinsert\<Cr>a\<C-x>\<C-o>"]], { noremap = true, silent = true, expr = true })

vim.api.nvim_set_keymap("v", '<leader>y', '"+y', silent)
-- Quit out of visual mode
vim.api.nvim_set_keymap("v", 'q', '<Esc>:q<Cr>', silent)
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

vim.api.nvim_exec([[
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
}


-- Turn off loaded_matchparen plugin. See :h pi_paren.txt
vim.g.loaded_matchparen = 1

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
-- vim.o.completeopt = 'menuone,preview'
vim.o.completeopt = 'menu,preview'

local wildignorePatterns = table.concat({
    '*.aux', '*.asv', '*.log', '*.swp', '*.nav', '*.toc', '*.out', '*.fdb_latexmk', '*.blg', '*.fls', '*.xdv', '*.bbl', '*.snm', '*.lof',
    '*.lot', '*.dvi', '*.tmp', '*.synctex.gz', 'node_modules/*', '.git/*', 'venv/*', }, ',')
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

-- Remove 'r' and 'o' from formatoptions
vim.o.formatoptions = vim.o.formatoptions:gsub('[ro]', '')

-- Modern terminals are great am i right?
vim.o.termguicolors = true

-- Nah, just use desert.  Colorscheme, try monokai
vim.cmd('colorscheme desert')
-- Highlight XlimRegex group #00cec9
vim.cmd('highlight XlimRegex guifg=#00cec9')

vim.cmd('highlight Normal guibg=NONE')
vim.cmd('highlight NonText guibg=NONE')
vim.cmd('highlight LineNr guifg=#808080')
vim.cmd('highlight XlimUnit guifg=#fc9c9e')

vim.cmd('highlight Title guifg=#5ca1b2')

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

vim.g.AutocorrectFiletypes = { "markdown", "tex", "text", "gitcommit", "html" }
vim.g.AutocorrectDisableDefaultMappings = true
vim.api.nvim_set_keymap("n", "<leader>a", "<Plug>(AutocorrectAddToAbbrev)" , {noremap = false, silent = true})

function check(value)    print(vim.inspect(value)) end
function in_lsp_buffer() return next(vim.lsp.buf_get_clients()) ~= nil end
function fix_completeopt()
    if in_lsp_buffer() then
        -- vim.o.completeopt = 'menuone,noinsert'
    else
        -- vim.o.completeopt = 'menu,preview'
    end
end

-- NERD Commenter
vim.g.NERDCustomDelimiters = { axon = { left = "//" }, idf = { left = "!" }, xlim = { left = "--" } }
-- I like spaces around my delimiters
vim.g.NERDSpaceDelims = 1

nnmap('<leader>n', ':NERDTree<cr>')
vim.g.NERDTreeIgnore = { '\\.aux.*$','\\.fls$','\\.lof$','\\.toc$','\\.out$','\\.vrb$','\\.nav$','\\.snm$','\\.bbl$','\\.bib','\\.fdb_latexmk$','\\.xdv','\\.gif','\\.pdf','\\~$','\\.blg$','\\.lot$' }

vim.g.copilot_filetypes = {
    yaml = true,
    markdown = true,
}

-- Function to insert a UUID
local function insert_uuid()
  local handle = io.popen('uuidgen')
  local uuid = handle:read("*a")
  handle:close()
  -- Remove any trailing newline
  uuid = uuid:gsub("%s+", "")
  -- Get the current cursor position
  local row, col = unpack(vim.api.nvim_win_get_cursor(0))
  vim.api.nvim_buf_set_text(0, row - 1, col, row - 1, col, { uuid })
  vim.api.nvim_win_set_cursor(0, { row, col + #uuid })
end
vim.api.nvim_create_user_command('InsertUUID', insert_uuid, {})
vim.api.nvim_set_keymap('i', '<localleader>g', '<Cmd>InsertUUID<CR>', { noremap = true, silent = true })


function shell_command_output_to_telescope(args)
  -- Validate the input
  if type(args) ~= "table" then
    error("The argument must be a table of string arguments.")
  end

  -- Concatenate the arguments into a shell command
  local command = table.concat(args, " ")

  -- Execute the command and capture the output
  local handle = io.popen(command, "r")
  if not handle then
    error("Failed to execute command: " .. command)
  end
  local output = handle:read("*a")
  handle:close()

  -- Split the output into lines
  local lines = {}
  for line in output:gmatch("[^\r\n]+") do
    table.insert(lines, line)
  end

  -- Use Telescope to prompt
  local pickers = require('telescope.pickers')
  local finders = require('telescope.finders')
  local conf = require('telescope.config').values

  pickers.new({}, {
    prompt_title = 'Shell Command Output',
    finder = finders.new_table {
      results = lines,
      entry_maker = function(entry)
        return {
          value = entry,
          display = entry,
          ordinal = entry,
        }
      end,
    },
    sorter = conf.generic_sorter({}),
  }):find()
end

select_plot_header = function()
    possible_items = vim.fn.systemlist({'mplot', '--headers', vim.fn.expand('%')})

    if #possible_items == 0 then
        print("No headers found")
        return
    end

    -- Use vim.ui.select to prompt the user to select an item
    vim.ui.select(
        possible_items,
        { prompt = "Select a column" },
        function(selected_item)
            -- Insert the selected item, surrounded by '"' at the cursor position
            vim.api.nvim_put({ '"' .. selected_item .. '"' }, "c", true, true)
        end
    )
end

-- Trying out custom telescope picker
local pickers      = require('telescope.pickers')
local finders      = require('telescope.finders')
local conf         = require('telescope.config').values
local actions      = require('telescope.actions')
local action_state = require('telescope.actions.state')

-- our picker function: colors
tele_colors = function(opts)
  opts = opts or {}
  pickers.new(opts, {
    prompt_title = "colors",
    finder = finders.new_table {
      results = { "red", "green", "blue" }
    },
    sorter = conf.generic_sorter(opts),
    attach_mappings = function(prompt_bufnr, map)
      actions.select_default:replace(function()
        actions.close(prompt_bufnr)
        local selection = action_state.get_selected_entry()
        -- print(vim.inspect(selection))
        vim.api.nvim_put({ selection[1] }, "", false, true)
      end)
      return true
    end,
  }):find()
end

-- Function to move to the next line with a blank cell in a TSV file
function goto_next_blank_cell_line()
  -- Get the current buffer
  local buf = vim.api.nvim_get_current_buf()

  -- Get the current cursor position
  local row, col = unpack(vim.api.nvim_win_get_cursor(0))

  -- Get the total number of lines in the buffer
  local line_count = vim.api.nvim_buf_line_count(buf)

  -- Loop through the lines starting from the next line
  for i = row + 1, line_count do
    -- Get the line content
    local line = vim.api.nvim_buf_get_lines(buf, i - 1, i, false)[1]

    -- Split the line into cells using tab as delimiter
    local cells = vim.split(line, '\t')

    local start_pos = 0

    -- Check for blank cells
    for _, cell in ipairs(cells) do
      if cell == "" then
        -- Move the cursor to the line with a blank cell
        vim.api.nvim_win_set_cursor(0, {i, start_pos})
        return
      end
      start_pos = start_pos + #cell + 1
    end
  end

  -- Print a message if no blank cell is found
  print("No more lines with blank cells found")
end


-- -- to execute the function
-- colors()

-- vim-vsnip {{{
-- https://github.com/hrsh7th/vim-vsnip
-- Taken nearly directly out of the README.

-- Add insert mode mapping for '<Plug>(vsnip-expand-or-jump)' using C-j
vim.api.nvim_set_keymap('i', '<C-j>', '<Plug>(vsnip-expand-or-jump)', { silent = true, noremap = true })

vim.api.nvim_exec([[
imap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'
smap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'

" If you want to use snippet for multiple filetypes, you can `g:vsnip_filetypes` for it.
let g:vsnip_filetypes = {}
let g:vsnip_filetypes.neobem = ['idf']
let g:vsnip_filetypes.typescriptreact = ['typescript']

]], false)

local home_dir = os.getenv('HOME')

if home_dir ~= nil then
    vim.g.vsnip_snippet_dir = os.getenv('HOME') .. '/.config/vsnip'
    vim.g.vsnip_snippet_dirs = { os.getenv('HOME') .. '/.config/vsnip',  os.getenv('HOME') .. '/.vsnip' }
end
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

local function markdownMathBlocks()
    vim.cmd [[ syn region markdownMath start="^\$\$" end="\$\$" ]]
    vim.cmd [[ syn match inlineMarkdownMath "\$[^$]\+\$" ]]

    vim.cmd [[ hi link markdownMath Statement ]]
    vim.cmd [[ hi link inlineMarkdownMath Statement ]]
end

filetype_autocmds_id = vim.api.nvim_create_augroup('filetype_autocmds', { clear = true })
local function addToFiletypeAugroup(pattern, command)
    vim.api.nvim_create_autocmd('FileType', { pattern = pattern, group = filetype_autocmds_id, command = command })
end

vim.api.nvim_create_autocmd('FileType', { pattern = 'tsv', group=filetype_autocmds_id, callback = function() vim.api.nvim_set_keymap('n', ']n', ':lua goto_next_blank_cell_line()<CR>', { noremap = true, silent = true }) end })
vim.api.nvim_create_autocmd('FileType', { pattern = 'markdown', group = filetype_autocmds_id, callback = markdownMathBlocks })

-- Remove 'r' and 'o' from formatoptions. This is to remove annoying comment wrapping.
vim.api.nvim_create_autocmd('FileType', { pattern = 'sh,cs,gitignore,conf', group = filetype_autocmds_id, command = 'setlocal formatoptions-=r formatoptions-=o' })

local function set_xlim_makeprg()
    vim.api.nvim_buf_set_option(0, 'makeprg', 'xlim "%"')
end

vim.api.nvim_create_autocmd('FileType', { pattern = 'xlim', group = filetype_autocmds_id, callback = setup_xlimlsp })
vim.api.nvim_create_autocmd('FileType', { pattern = 'xlim', group = filetype_autocmds_id, callback = set_xlim_makeprg })

vim.api.nvim_create_autocmd('FileType', { pattern = 'antlr4', group = filetype_autocmds_id, command = 'nnoremap <localleader>c :!antlr4 %<CR>' })

vim.api.nvim_create_autocmd('FileType', {
     pattern = 'python',
     group = filetype_autocmds_id,
     callback = function()
         vim.api.nvim_set_keymap("i", ".", [[&omnifunc == "" ? "." : ".\<C-o>:set completeopt=menuone,noinsert\<Cr>\<C-x>\<C-o>"]], { noremap = true, silent = true, expr = true })
     end })

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

    { 'gitcommit', 'startinsert' },

    -- make a header 1 line, deleting trailing whitespace first.
    --{ 'markdown', 'nnoremap <silent> <leader>h1 :<c-u>call<Space><SID>MakeHeading("=")<cr>', },
    --{ 'markdown', 'nnoremap <silent> <leader>h2 :<c-u>call<Space><SID>MakeHeading("-")<cr>', },
    -- { 'markdown,tex,text', 'setlocal textwidth=72' },
    { 'markdown,tex,text', 'setlocal spell' },
    { 'markdown', 'setlocal tabstop=2' },
    { 'markdown', 'nnoremap ]] <Cmd>keeppatterns /^#<Cr>' },
    { 'markdown', 'nnoremap <localleader>- <Cmd>keeppatterns s/[^<bar>]/-/g<Cr>' },
    { 'markdown', 'nnoremap <leader>m vip:!to_markdown<Cr>' },

    { 'help', 'nnoremap <leader>hh mnA~<esc>`n', },
    { 'help', 'nnoremap <leader>hl mn78i=<esc>`n', },
    { 'help', 'setlocal nospell' },

    { 'json', 'setlocal conceallevel=0' },
    { 'os_workflow', 'setlocal conceallevel=0' },

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

    { 'mplot', 'nnoremap <localleader>b <cmd>!mplot %:S \\| gnuplot -<cr>' },

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

    { 'sh', 'inoremap ,sh #!/bin/sh<CR><C-U><Esc>:set ft=sh<CR>a', },
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

    { 'cem', 'inoremap <localleader>b <!-- Compass:  --><CR><CR><!-- Compass --><Esc>2k0f:la', },

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
    { '*.compass', 'set filetype=cem' },
    { '*.cem'    , 'set filetype=cem' },
    { '*.gnuplot', 'set filetype=gnuplot'},
    { '*.har'    , 'set filetype=json' },
    { '*.ce'     , 'set filetype=ce' },
    { '*.maxima' , 'set filetype=maxima' },
    { '.gitignore', 'set filetype=conf' }, -- close enough
    { '.gitignore', 'inoremap ,dt :read !do-targets' },
    { '*.BAT', 'set filetype=dosbatch' }, -- Assume Windows Batch files

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
    -- { '*', 'lua fix_completeopt()' },
}

bufenter_augroup_id = vim.api.nvim_create_augroup('bufenter_augroup', { clear = true })
for _, autocmd in ipairs(bufEnterAutocmds) do
    vim.api.nvim_create_autocmd('BufEnter', { pattern = autocmd[1], group = bufenter_augroup_id, command = autocmd[2] })
end


vim.api.nvim_create_augroup('MPEvents', { clear = true })
--vim.api.nvim_create_autocmd('TermOpen', { pattern = '*',        group = 'MPEvents', command = 'setlocal nonumber norelativenumber | startinsert | echom "Term Open.."' })
vim.api.nvim_create_autocmd('BufEnter', { pattern = "term://*", group = 'MPEvents', command = 'startinsert' })
vim.api.nvim_create_autocmd('TextYankPost', { pattern = '*', group = 'MPEvents', command = 'silent! lua vim.highlight.on_yank { timeout = 500 }' })

local ignore_dirs = { }

if home_dir ~= nil then
    table.insert(ignore_dirs, home_dir .. "/.config/")
end

table.insert(ignore_dirs, os.getenv("DOTFILES"))
table.insert(ignore_dirs, "/tmp/")

-- iterate backwards and remove any nils
for i = #ignore_dirs, 1, -1 do
    if ignore_dirs[i] == nil then
        table.remove(ignore_dirs, i)
    end
end


local function write_directory()
  local file_path = vim.fn.expand('%:p:h')  -- Get the full path of the current file

  -- Check if file path starts with any of the ignored directories
  for _, dir in ipairs(ignore_dirs) do
      if file_path:sub(1, #dir) == dir then
          return
      end
  end

  if home_dir == nil then print("HOME not set") end

  local dir_name = home_dir .. "/.config/d"

  local success, msg = os.execute("mkdir -p \"" .. dir_name .. "\"")
  if not success then
      print("Could not make dir " .. dir_name )
      return
  end

  local record_file_path = home_dir .. "/.config/d/dirs.tsv"  -- The record file

  -- Get the current date
  local date = os.date("*t")
  local year, month, day = date.year, date.month, date.day

  -- Try to open the record file
  file, err = io.open(record_file_path, "r")

  local content
  if file then
      -- Read the entire content
      content = file:read("*a")
      file:close()
  else
      content = ""
  end

  -- Check for the entry
  local found_entry = false
  for line in content:gmatch("[^\n]+") do
      local fields = {}
      for field in line:gmatch("[^\t]+") do
        table.insert(fields, field)
      end

      local l_year, l_month, l_day = tonumber(fields[1]), tonumber(fields[2]), tonumber(fields[3])

      -- If the date of the line is not equal to the current date, stop the search
      if l_year ~= year or l_month ~= month or l_day ~= day then break end

      if fields[4] == file_path then
        -- If the file path is already in the record, stop the search
        found_entry = true
        break
    end
  end

  -- If the entry is not found, add it to the top of the file
  if not found_entry then
    local entry = string.format("%d\t%02d\t%02d\t%s\n", year, month, day, file_path)
    -- Prepend the entry to the content
    content = entry .. content

    -- Write the new content back to the file
    file, err = io.open(record_file_path, "w")
    if not file then
        print(err)
        return
    end
    file:write(content)
    file:close()
  end
end

-- Call the function each time a file is opened, only if not on windows
if not in_windows then vim.api.nvim_create_autocmd('BufReadPost', { pattern = '*', group = 'MPEvents', callback = write_directory }) end

-- Remove trailing whitespace. Use keeppatterns so that
-- the search history isn't ruined with the \v\s+$ junk.
-- Setting the marks is required so that the cursor doesn't jump
-- around.
-- vim.cmd([[autocmd BufWrite * execute "normal! mz" |  keeppatterns %s/\v\s+$//e | normal `z]])
vim.api.nvim_create_autocmd('BufWrite', { pattern = '*.cs,*.md,*.txt,*.lua,COMMIT_EDITMSG,*.msh', group = 'MPEvents', command = 'execute "normal! mz" |  keeppatterns %s/\\v\\s+$//e | normal `z' })

function remove_trailing_blank_lines()
    -- Get number of lines in buffer. 0 is only for unloaded buffer.
    local line_count = vim.api.nvim_buf_line_count(0)
    if line_count < 2 then
        -- Save at the end.
        vim.cmd('update')
        return
    end

    -- Get contents of final line
    local last_line = vim.api.nvim_buf_get_lines(0, -2, -1, false)[1]
    -- If it's blank or whitespace, delete it
    if last_line:match('^%s*$') then
        vim.api.nvim_buf_set_lines(0, -2, -1, false, {})
        -- recurse until no more blank lines
        remove_trailing_blank_lines()
    end
    vim.cmd('update')
end

-- Remove trailing blank lines only before quitting file. Was a bit annoying on every save.
vim.api.nvim_create_autocmd('QuitPre', { pattern = '*', group = 'MPEvents', callback = remove_trailing_blank_lines })

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
