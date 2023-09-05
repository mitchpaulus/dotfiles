function gd;
    if test -d $HOME/dotfiles
        cd $HOME/dotfiles
    else if test -d $REPOS/dotfiles
        cd $REPOS/dotfiles
    else
        printf 'Could not find dotfiles directory\n'
    end
end
