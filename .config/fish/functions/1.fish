function 1
    mkdir -p ~/.config/mp
    if test -f ~/.config/mp/dirs.txt
        set DIR (awk 'NR == 1' ~/.config/mp/dirs.txt)
        if test -z $DIR
            printf 'Directory 1 is blank\n'
        else if test -d $DIR
            cd $DIR
            # See https://github.com/fish-shell/fish-shell/issues/6413 for why this is necessary.
            # Without it, the prompt doesn't update.
            commandline -f repaint
        else
            printf 'Directory "%s" does not exist\n'
        end
    else
        printf 'File \'~/.config/mp/dirs.txt\' not set up\n'
    end
end
