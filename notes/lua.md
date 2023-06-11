# lua

[learn lua in 15 minutes](https://learnxinyminutes.com/docs/lua/)
[learn lua in 15 minutes Num 2](http://tylerneylon.com/a/learn-lua/?ref=hackr.io)
[Lua for Neovim](https://vonheikemen.github.io/devlog/tools/configuring-neovim-using-lua/)
[Lua cheat sheet](https://devhints.io/lua)

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

vim.inpsect(thing) # Human readable

lua =expr -- is same as
lua print(vim.inspect(expr))
```

Most of the global lua neovim commands are under the `vim.api`
namespace.

```lua
-- looping over array https://stackoverflow.com/a/39991824/5932184
for _, value in ipairs(list) do
    doStuff(value)
end
```

```lua
-- Table functions
table.insert(list, value) -- appends to end
table.insert(list, 2, value) -- inserts at index 2 (1-based)
table.remove(list, index)
```

io.open (filename [, mode])
This function opens a file, in the mode specified in the string mode.
In case of success, it returns a new file handle.

The mode string can be any of the following:

"r": read mode (the default);
"w": write mode;
"a": append mode;
"r+": update mode, all previous data is preserved;
"w+": update mode, all previous data is erased;
"a+": append update mode, previous data is preserved, writing is only allowed at the end of file.

The mode string can also have a 'b' at the end, which is needed in some systems to open the file in binary mode.
