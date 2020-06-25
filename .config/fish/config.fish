#!/usr/bin/fish

set -g fish_prompt_pwd_dir_length 3

function fish_prompt
    set_color cyan
    printf "%s >\n:: " (prompt_pwd)
    set_color normal
end


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
function u; cd ..; end

# Carrying over from source [b]ashrc
function sb
    source ~/.config/fish/config.fish
    printf "Reloaded %s\n" ~/.config/fish/config.fish
end

# If working in WSL environment
if test -n "$WSL_DISTRO_NAME"
    function eh
        explorer.exe (wslpath -w (pwd))
    end
end

# Load configuration special to given computer
if test -f ~/.config/fish/host-config.fish
    source ~/.config/fish/host-config.fish
end

