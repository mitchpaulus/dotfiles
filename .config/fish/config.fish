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
set -gx PATH "$HOME/bin" $PATH
set -gx PATH "$HOME/.local/bin" $PATH

set -gx CLASSPATH ".:/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH"

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

function lf
    "$HOME"/bin/lf -last-dir-path "$HOME/.config/lf/lf_lastdir" $argv; and cd (cat "$HOME/.config/lf/lf_lastdir")
end

function u; cd ..; end

function m; nvim Makefile; end

function t
    task $argv
end

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
    else if command -s apt
        sudo apt update
    end
end

function compass
    if test -d '/mnt/c/Users/mpaulus/source/repos/Compass/'
        tmux new-session -c /mnt/c/Users/mpaulus/source/repos/Compass/ -s Compass
    else
        printf 'Did not find compass repository at /mnt/c/Users/mpaulus/source/repos/Compass/\n'
    end
end

function winmount
    set lowercase_letter (string lower $argv[1])
    set uppercase_letter (string upper $argv[1])

    if [ ! -d /mnt/"$lowercase_letter" ]
        sudo mkdir -p /mnt/"$lowercase_letter"
    end
    sudo mount -t drvfs "$uppercase_letter": /mnt/"$lowercase_letter"
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
