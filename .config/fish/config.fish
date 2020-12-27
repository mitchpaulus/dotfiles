#!/usr/bin/fish

set -g fish_prompt_pwd_dir_length 5

set -gx EDITOR nvim
set -gx VISUAL nvim
set -g H /mnt/c/Users/mpaulus

function fish_prompt
    set_color cyan
    printf "%s >\n:: " (prompt_pwd)
    set_color normal
end

function __path_add
    # If the directory exists and isn't in the path, add it.
    if not contains $argv[1] $PATH; and test -d $argv[1]
        set -gxp PATH $argv[1]
    end
end

__path_add ~/dotfiles/scripts/
__path_add /usr/local/texlive/2020/bin/x86_64-linux
__path_add "$HOME/.gem/ruby/2.7.0/bin"
__path_add "$HOME/bin"
__path_add "$HOME/.local/bin"

set -gx CLASSPATH ".:/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH"

set -gx DOTREMINDERS ~/.config/remind/remind.rem

set -gx FZF_DEFAULT_OPTS '--reverse --margin 10% --border'

set -gx BAT_THEME 'Monokai Extended'

# v for VIM
function v --wraps="$EDITOR"
    "$EDITOR" $argv
end

function wttr; curl 'wttr.in/Dallas?format=%l:+%C+%t+%h+%w'; end

# Git shortcuts
if command -v git >/dev/null 2>&1
    function a;  git add       $argv; end
    function d --wraps='git diff';  git diff -w      $argv; end
    function s;  git status -u $argv; end
    function c;  git commit    $argv; end
    function p;  git push      $argv; end
    function dc; git diff -w --cached $argv; end
end

function r --wraps=ranger; ranger --choosedir="$HOME/.rangerdir"; cd (cat $HOME/.rangerdir); end

function lf --wraps=lf
    "$HOME"/bin/lf -last-dir-path "$HOME/.config/lf/lf_lastdir" $argv; and cd (cat "$HOME/.config/lf/lf_lastdir")
end

function u; cd ..; end

function m
    if test -f Makefile
        "$EDITOR" Makefile;
    else
        printf "Makefile not found\n"
    end
end

function t --wraps=task
    task $argv
end

function g
    cd (fzf -1 < ~/.config/goto/dirs.txt | awk -F "	" '$1')
end

function ev --description "Edit vimrc file"
    if test -f "$HOME/.config/nvim/init.vim"
        "$EDITOR" "$HOME/.config/nvim/init.vim"
    else
        printf "vimrc file not found.\n"
    end
end

function eg --description "Edit goto dirs file"
    "$EDITOR" ~/.config/goto/dirs.txt
end

function ag
    pwd >> ~/.config/goto/dirs.txt
end

function i --description 'Edit idf files'
    "$EDITOR" *.idf
end

function en --description 'Edit a note'
    set file (fd --type f '' ~/dotfiles/notes/ -x printf "%s\n" '{/}' | sed 's/\.md//' | fzf -1) && "$EDITOR" ~/dotfiles/notes/"$file".md
end
# Carrying over from source [b]ashrc
function sb --description 'Reload fish config file'
    source ~/.config/fish/config.fish
    printf "Reloaded %s\n" ~/.config/fish/config.fish
end

# If working in WSL environment, set up command to bring up Windows Explorer in current directory.
if test -n "$WSL_DISTRO_NAME"
    function eh
        explorer.exe (wslpath -w (pwd))
    end
end

# Load configuration special to given computer
if test -f ~/.config/fish/host-config.fish
    source ~/.config/fish/host-config.fish
end

function update --description 'Universal package update'
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
