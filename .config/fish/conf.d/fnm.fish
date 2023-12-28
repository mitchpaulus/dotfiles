# fnm
path_prepend "$HOME"/.fnm
path_prepend "$HOME"/.local/share/fnm
if command --query fnm
    fnm env | source
end
