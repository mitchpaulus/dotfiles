function cphis --description "Fuzzy search and copy a line from history to clipboard"
    if command -v clip.exe >/dev/null 2>/dev/null
        history | fzf | tr -d '\r\n' | clip.exe
    else
        printf "Need to update this function to work with other clipboards.\n"
    end
end

