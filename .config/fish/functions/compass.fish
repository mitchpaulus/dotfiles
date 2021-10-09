function compass
    if test -d "$REPOS/Compass/"
        tmux new-session -c "$REPOS"/Compass/ -s Compass
    else
        printf 'Did not find compass repository at %s/Compass\n' "$REPOS"
    end
end
