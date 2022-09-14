# Carrying over from source [b]ashrc
function sb --description 'Reload fish config file'
    source ~/.config/fish/config.fish
    printf "Reloaded %s\n" ~/.config/fish/config.fish
end
