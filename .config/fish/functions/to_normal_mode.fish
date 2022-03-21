function to_normal_mode
    if commandline -P
        commandline -f cancel
    else
        set fish_bind_mode default
        commandline -f backward-char repaint-mode
    end
end
