function install_units
    if test ! -e ~/.units
        ln -s -r "$DOTFILES"/.units "$HOME"/.units
    end
end
