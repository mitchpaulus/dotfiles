# Search notes
function sn --description 'Grep ([s]earch) [n]otes'
    if has rg
        rg $argv[1] "$DOTFILES"/notes
    else
        grep $argv[1] "$DOTFILES"/notes
    end
end
