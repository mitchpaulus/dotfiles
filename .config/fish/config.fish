#!/usr/bin/fish

function v
    nvim $argv
end

# Git shortcuts
if command -v git >/dev/null 2>&1
    function a;  git add       $argv; end
    function d;  git diff      $argv; end
    function s;  git status -u $argv; end
    function c;  git commit    $argv; end
    function p;  git push      $argv; end
end

function r; ranger --choosedir="$HOME/.rangerdir"; cd (cat $HOME/.rangerdir);  end
function gd; cd ~/dotfiles; end
function u; cd ..; end

# Carrying over from source [b]ashrc
function sb
    source ~/.config/fish/config.fish
    printf "Reloaded %s\n" ~/.config/fish/config.fish
end

# Carrying over from [e]dit [b]ashrc
function eb
    nvim ~/.config/fish/config.fish
end


