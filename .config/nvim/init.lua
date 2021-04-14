
vim.g.mapleader = ' '
vim.g.maplocalleader = ','


--[[ "Use jk to escape insert mode. Suggested here:
"http://learnvimscriptthehardway.stevelosh.com/chapters/10.html
"inoremap jk <esc>
" Now switching to jf for a few reasons:
" 1. jk stills causes some RSI problems
" 2. df and fd were annoying since there are many words that end with
"    either of those characters. The biggest offender was f in if statements.
" 3. j is the best leader character, since almost no words end with that.
" 4. So jf splits the duty between both hands using strong pointer finger.  ]]

vim.cmd("inoremap jf <esc>")

-- Fast quitting
vim.cmd("nnoremap q :q<CR>")

vim.cmd("nnoremap K 5k")
vim.cmd("nnoremap J 5j")
