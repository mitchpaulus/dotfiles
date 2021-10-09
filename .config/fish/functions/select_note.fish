function select_note
    fd --type f -e md '' "$MPNOTES" -x printf "%s\n" '{/}' | sed 's/\.md//' | fzf -1
end
