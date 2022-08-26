function ep --description 'Edit python utility function'
    if test -f $DOTFILES/python/mputils.py
        $EDITOR $DOTFILES/python/mputils.py
    else
        printf "File '%s' not found\n" $DOTFILES/python/mputils.py
    end
end
