function eiv --description "[E]dit [i]nit.[v]im"
    set init_file  "$DOTFILES/.config/nvim/init.vim"
    if test -e "$init_file"
        "$EDITOR" "$init_file"
    else
        printf "%s not found.\n" "$init_file"
    end
end
