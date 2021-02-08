function eh
    if command -v explorer.exe >/dev/null 2>/dev/null
        explorer.exe (wslpath -w (pwd))
    else if command -v dolphin >/dev/null 2>/dev/null
        dolphin . &
    else
        printf "No GUI file manager set up.\n"
    end
end
