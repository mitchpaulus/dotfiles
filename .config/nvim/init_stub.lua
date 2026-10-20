-- Stub: load the real config from the dotfiles repo.
-- (Hard links get broken by git, so don't link this file.)
local repos = os.getenv('REPOS')
if not repos then
    vim.notify('REPOS environment variable not set; dotfiles init.lua not loaded', vim.log.levels.ERROR)
    return
end

local config = vim.fs.joinpath(repos, 'dotfiles', '.config', 'nvim', 'init.lua')
vim.env.MYVIMRC = config
dofile(config)
