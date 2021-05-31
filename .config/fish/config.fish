#!/usr/bin/fish

set -g fish_prompt_pwd_dir_length 5

# Neovim/Vim for all the things
if command -v nvim >/dev/null 2>&1
    set -gx EDITOR nvim
    set -gx VISUAL nvim
else if command -v vim >/dev/null 2>&1
    set -gx EDITOR vim
    set -gx VISUAL vim
end

set -gx DOTFILES ~/dotfiles

set -gx FILEMANAGER lf

# Good ole U.S. of A.
set -gx TEXLIVE_INSTALL_PAPER letter
set -gx TEXLIVE_INSTALL_PREFIX "$HOME"/texlive

if command -v exa >/dev/null 2>&1
    function ls --wraps exa
        exa $argv
    end
end

# Add a REPOS environment variable for all those git repositories.
if test -d '/mnt/c/Users/mpaulus/source/repos'
    set -gx REPOS '/mnt/c/Users/mpaulus/source/repos'
else if test -d "$HOME"/repos
    set -gx REPOS "$HOME"/repos
end

# This from DistroTube https://www.youtube.com/watch?v=ab3rY0X5kD4
set -gx MANPAGER "nvim -c 'set ft=man' -"

set -g H /mnt/c/Users/mpaulus

function fish_prompt
    set exit_code "$status"
    if test "$exit_code" -eq 0
        set_color cyan
        printf "%s >\n:: " (prompt_pwd)
        set_color normal
    else
        set_color cyan
        printf "%s >\n" (prompt_pwd)
        set_color red
        printf "(%s) :: " "$exit_code"
        set_color normal
    end
end

function __path_add
    # If the directory exists and isn't in the path, add it.
    if not contains $argv[1] $PATH; and test -d $argv[1]
        set -gxp PATH $argv[1]
    end
end

function add_date
    commandline -i (date '+%Y-%m-%d')
end

function fish_underscore_command
    commandline (underscore_files (commandline))
end

bind \ed add_date
bind \eu fish_underscore_command

__path_add "$DOTFILES"/scripts/
__path_add "$DOTFILES"/haskell
__path_add "$TEXLIVE_INSTALL_PREFIX"/2021/bin/x86_64-linux
__path_add /usr/local/texlive/2020/bin/x86_64-linux
__path_add "$HOME/.gem/ruby/2.7.0/bin"
__path_add "$HOME/.gem/ruby/3.0.0/bin"
__path_add "$HOME/bin"
__path_add "$HOME/.local/bin"

set -gxp MANPATH "$TEXLIVE_INSTALL_PREFIX"/2021/texmf-dist/doc/man
set -gxp INFOPATH "$TEXLIVE_INSTALL_PREFIX"/2021/texmf-dist/doc/man


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
    function a --wraps='git add';  git add       $argv; end
    function d --wraps='git diff';  git diff -w $argv; end
    function s --wraps='git status';  git status -u $argv; end
    function c --wraps='git commit';  git commit $argv; end
    function p --wraps='git push';  git push      $argv; end
    function dc --wraps='git diff'; git diff -w --cached $argv; end
end

# function r --wraps=ranger; ranger --choosedir="$HOME/.rangerdir"; cd (cat $HOME/.rangerdir); end
# Go to git repositories
function r
    if test -n "$REPOS"
        "$FILEMANAGER" "$REPOS"
    else
        printf "The environment variable REPOS is not set\n"
    end
end

if test -d '/mnt/c/Users/mpaulus/Command Commissioning'
    function j
        "$FILEMANAGER" '/mnt/c/Users/mpaulus/Command Commissioning'
    end
end


function f --wraps="$FILEMANAGER" --description 'When two characters is too many.'
    "$FILEMANAGER"
end

function lf --wraps=lf
    set config_dir  "$HOME/.config/lf"
    # Make config directory if it doesn't exist
    if test '!' -d "$config_dir"; mkdir -p  "$config_dir"; or return 1; end
    command lf -last-dir-path "$config_dir"/lf_lastdir $argv; and cd (cat "$config_dir"/lf_lastdir)
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

function eil --description "[E]dit [i]nit.[l]ua"
    set init_file  "$DOTFILES/.config/nvim/init.lua"
    if test -e "$init_file"
        "$EDITOR" "$init_file"
    else
        printf "%s not found.\n" "$init_file"
    end
end

function ev --description "Edit vimrc file"
    if test -e "$HOME/.config/nvim/init.vim"
        "$EDITOR" "$HOME/.config/nvim/init.vim"
    else if  test -e "$HOME/.config/nvim/init.lua"
        "$EDITOR" "$HOME/.config/nvim/init.lua"
    else if  test -e "$HOME"/.vimrc
        "$EDITOR" "$HOME"/.vimrc
    else
        printf "vimrc file not found.\n"
    end
end

# If a build of Neovim from source is found, use that.
if test -f "$REPOS"/neovim/build/bin/nvim
    function nvim --description 'Source build of Neovim' --wraps 'nvim'
        env VIMRUNTIME="$REPOS"/neovim/runtime "$REPOS"/neovim/build/bin/nvim $argv
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
    set file (fd --type f -e md '' "$DOTFILES"/notes/ -x printf "%s\n" '{/}' | sed 's/\.md//' | fzf -1); and "$EDITOR" "$DOTFILES"/notes/"$file".md
end

function gn --description 'Go to notes directory'
    cd "$DOTFILES"/notes
end

function gr --description 'Go to code repositories';
    if test -d "$REPOS"
        cd "$REPOS"
    else
        printf '$REPOS environment variable not found.\n'
    end
end

# Carrying over from source [b]ashrc
function sb --description 'Reload fish config file'
    source ~/.config/fish/config.fish
    printf "Reloaded %s\n" ~/.config/fish/config.fish
end

# Set up specific commands if working in WSL environment
if test -n "$WSL_DISTRO_NAME"
    # Command to bring up Windows Explorer in current directory.
    function eh
        explorer.exe (wslpath -w (pwd))
    end

    # This is a variable used by `lf`. wsl-opener is a personal opener script
    # See: https://github.com/mitchpaulus/wsl-opener
    set -gx OPENER wsl-opener
end

# Load configuration special to given computer
if test -f ~/.config/fish/host-config.fish
    source ~/.config/fish/host-config.fish
end

function update --description 'Universal package update'
    if command -s pacman >/dev/null
        sudo pacman -Syu
    else if command -s apt >/dev/null
        sudo apt update
    end
end

function compass
    if test -d "$REPOS/Compass/"
        tmux new-session -c "$REPOS"/Compass/ -s Compass
    else
        printf 'Did not find compass repository at %s/Compass\n' "$REPOS"
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

function ta --description "tmux attach"
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

# ghcup-env
set -q GHCUP_INSTALL_BASE_PREFIX[1]; or set GHCUP_INSTALL_BASE_PREFIX "$HOME"
if test -f "$HOME"/.ghcup/env
     __path_add "$HOME"/.cabal/bin
     __path_add /home/mitch/.ghcup/bin
 end
#
# Yet another version manager. nvm = node version manager.
set -gx NVM_DIR "$HOME/.nvm"
if test -s "$NVM_DIR/nvm.sh"; bash "$NVM_DIR/nvm.sh"; end

# vim:ft=fish
