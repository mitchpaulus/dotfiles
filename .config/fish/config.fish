#!/usr/bin/fish

set -g fish_prompt_pwd_dir_length 3

set -gx EDITOR nvim
set -gx VISUAL nvim
set -g H /mnt/c/Users/mpaulus

function fish_prompt
    set_color cyan
    printf "%s >\n:: " (prompt_pwd)
    set_color normal
end

set -gx PATH ~/dotfiles/scripts/ $PATH
set -gx PATH /usr/local/texlive/2020/bin/x86_64-linux $PATH

function v
    nvim $argv
end

function wttr; curl 'wttr.in/Dallas?format=%l:+%C+%t+%h+%w'; end

# Git shortcuts
if command -v git >/dev/null 2>&1
    function a;  git add       $argv; end
    function d;  git diff -w      $argv; end
    function s;  git status -u $argv; end
    function c;  git commit    $argv; end
    function p;  git push      $argv; end
    function dc; git diff -w --cached $argv; end
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

function update
    if command -s pacman
        sudo pacman -Syu
    end
end

function compass
    if test -d '/mnt/c/Users/mpaulus/source/repos/Compass/'
        tmux new-session -c /mnt/c/Users/mpaulus/source/repos/Compass/ -s Compass
    else
        printf 'Did not find compass repository at /mnt/c/Users/mpaulus/source/repos/Compass/\n'
    end
end


function ta
    set -l IFS
    switch (tmux ls 2>&1)
        case "no server running*"
            printf "No tmux server currently running\n"
        case '*'
            if test (tmux ls | wc -l) -gt 1
                tmux attach-session -t (tmux ls | awk -F ':' '{print $1}' | fzf)
            else
                tmux attach-session -t (tmux ls | awk -F ':' '{print $1;exit}')
            end
    end
end

# vim:ft=fish
