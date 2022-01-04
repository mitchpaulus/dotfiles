# fnm
path_prepend /home/mp/.fnm
if command --query fnm
    fnm env | source
end
