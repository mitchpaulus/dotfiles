# fnm
path_prepend "$HOME"/.fnm
if command --query fnm
    fnm env | source
end
