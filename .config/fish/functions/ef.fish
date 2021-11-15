function ef --description "Edit fish functions"
    set function_to_edit (find $DOTFILES/.config/fish/functions -name "*.fish" -printf '%f\n' | fzf)

    if test $status -eq 0
        "$EDITOR" "$DOTFILES/.config/fish/functions/$function_to_edit"
    end
end
