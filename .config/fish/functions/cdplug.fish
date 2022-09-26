function cdplug --description 'Quickly change to Neovim plugin dir'
    if test -d $HOME"/.local/share/nvim/plugged"
        cd $HOME"/.local/share/nvim/plugged"
    else if test -d $HOME/.config/nvim/plugged
        cd $HOME/.config/nvim/plugged
    else
        printf 'Could not find dir. Add to cdplug.fish function script\n' >&2
        false
    end
end
