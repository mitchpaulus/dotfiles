# lua

[learn lua in 15 minutes](https://learnxinyminutes.com/docs/lua/)
[learn lua in 15 minutes Num 2](http://tylerneylon.com/a/learn-lua/?ref=hackr.io)

[Lua for Neovim](https://vonheikemen.github.io/devlog/tools/configuring-neovim-using-lua/)

- Strings single or double quotes. `..` for concatenation
- while <boolean> do <code> end
- if <boolean> then <code> elseif <code> else <code> end
-  `nil` and `false` are only false things

- Handle exceptions: `pcall`.

## Neovim

Helpful help sections
```
:h lua-vimscript (vim.call, vim.cmd, vim.fn.{func})
```

```lua
-- For testing, will often do
-- :lua print(vim.inspect(<thing>))

vim.inpsect(<thing>) # Human readable
```
