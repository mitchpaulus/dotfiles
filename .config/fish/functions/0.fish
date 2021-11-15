function 0
    if test -f "$HOME"/.config/mp/dirs.txt
        cat dirs.txt
    else
        printf "No $HOME/.config/mp/dirs.txt file found.\n"
    end
end
