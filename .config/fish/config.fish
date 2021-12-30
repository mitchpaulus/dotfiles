#!/usr/bin/fish

set -g fish_prompt_pwd_dir_length 5

set -gx DOTFILES ~/dotfiles
set -gx MPNOTES ~/dotfiles/notes
set -gx LOCALBIN ~/.local/bin
set -gx FILEMANAGER lf

# Good ole U.S. of A.
set -gx TEXLIVE_INSTALL_PAPER letter
set -gx TEXLIVE_INSTALL_PREFIX "$HOME"/texlive

# See https://github.com/neovim/neovim/issues/14090#issuecomment-913837694
# and https://github.com/neovim/neovim/issues/15487
set -gx MANPAGER 'nvim +Man!'

set -g H /mnt/c/Users/mpaulus

# set -gxp MANPATH "$TEXLIVE_INSTALL_PREFIX"/2021/texmf-dist/doc/man
# set -gxp INFOPATH "$TEXLIVE_INSTALL_PREFIX"/2021/texmf-dist/doc/man

set -gx CLASSPATH ".:/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH"
set -gx AWKPATH ".:/usr/local/share/awk:$DOTFILES/awk_functions"
set -gx DOTREMINDERS ~/.config/remind/remind.rem
set -gx FZF_DEFAULT_OPTS '--reverse --margin 10% --border'
set -gx BAT_THEME 'Monokai Extended'
# Microsoft doesn't need my telemetry
set -gx DOTNET_CLI_TELEMETRY_OPTOUT 1

# Required for Haxall - See https://github.com/haxall/haxall
set -gx FAN_BUILD_JDKHOME /usr/java/jdk-14.0.2/

# Neovim/Vim for all the things
if command -v nvim >/dev/null 2>&1
    set -gx EDITOR nvim
    set -gx VISUAL nvim
else if command -v vim >/dev/null 2>&1
    set -gx EDITOR vim
    set -gx VISUAL vim
end


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


function fish_prompt
    set exit_code "$status"

    if test -n "$SSH_CONNECTION"
        set ssh_text (printf '%s@%s '  (whoami) (hostname) )
    else
        set ssh_text ''
    end

    set_color cyan
    printf "%s%s >\n:: "  $ssh_text (prompt_pwd)

    if test "$exit_code" -eq 0
        set_color normal
    else
        set_color red
        printf "(%s) :: " "$exit_code"
        set_color normal
    end
end

function fish_greeting
    if command -v random_remind >/dev/null 2>&1
        random_remind
    else
        printf '%s\n' "$fish_greeting"
    end
end

# See
# - https://github.com/microsoft/terminal/issues/3158#issuecomment-789043641
# - https://github.com/microsoft/terminal/pull/8330
# - https://github.com/microsoft/terminal/issues/8166
# Removed quoting since it jacked with the syntax highlighting
if test -n "$WT_SESSION"
    function windows-terminal --on-event fish_prompt
        printf \e]9\;9\;%s\e\\ (wslpath -m "$PWD")
    end
end

function __path_add
    # If the directory exists and isn't in the path, add it to the beginning of the path.
    if not contains $argv[1] $PATH; and test -d $argv[1]
        set -gxp PATH $argv[1]
    end
end

function add_date
    commandline -i (date '+%Y-%m-%d')
end

abbr -a ab 'awk \'BEGIN { FS=OFS="\t" }'

function fish_underscore_command
    commandline (underscore_files (commandline))
end

function add_count_lines
    commandline -i '| wc -l'
end

function add_copy_to_clip_exe
    commandline -i '| clip.exe'
end

# \e is ALT, mapped to Caps Lock
bind \ed add_date
bind \eu fish_underscore_command
bind \eB awk_begin
bind \ew add_count_lines
bind \ec add_copy_to_clip_exe

__path_add "$DOTFILES"/scripts/
__path_add "$DOTFILES"/python
__path_add "$DOTFILES"/haskell
__path_add /usr/local/texlive/2020/bin/x86_64-linux
__path_add "$TEXLIVE_INSTALL_PREFIX"/2021/bin/x86_64-linux
__path_add "/opt/fantom-1.0.76/bin"
__path_add "$HOME/.gem/ruby/2.7.0/bin"
__path_add "$HOME/.gem/ruby/3.0.0/bin"
__path_add "$HOME/bin"
__path_add "$HOME/.local/bin"


set -gxp PYTHONPATH "$DOTFILES"/python


# v for VIM
abbr -a v $EDITOR

abbr -a wttr 'curl \'wttr.in/Dallas?format=%l:+%C+%t+%h+%w\''

abbr -a gi "$EDITOR .gitignore"

# Consecutive numbering by default.
abbr -a mdformat 'mdformat --number'

abbr -a x 'chmod +x'

# Git shortcuts
if command -v git >/dev/null 2>&1
    abbr -a a 'git add'
    abbr -a d 'git diff -w'
    abbr -a s 'git status -u'
    abbr -a c 'git commit'
    abbr -a p 'git push'
    abbr -a dc 'git diff -w --cached'
    abbr -a fp 'git fetch --prune'
    abbr -a gu 'git add -u; git status -u'
    abbr -a ga 'git add -A; git status -u'
    abbr -a uc 'git add -u; git commit'
    abbr -a merge 'git merge --ff-only; git status -u'
end

# Go to git repositories
function r
    if test -z "$FILEMANAGER"
        printf 'The environment variable FILEMANAGER is not set\n'
    end

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

# When more than 1 character is too much
abbr f "$FILEMANAGER"

function lf --wraps=lf
    set config_dir  "$HOME/.config/lf"
    # Make config directory if it doesn't exist
    if test '!' -d "$config_dir"; mkdir -p  "$config_dir"; or return 1; end
    command lf -last-dir-path "$config_dir"/lf_lastdir $argv; and cd (cat "$config_dir"/lf_lastdir)
end

abbr -a u 'cd ..'

abbr t task

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

# Get .autocorrect length
abbr -a al 'wc -l ~/.autocorrect'

# Edit idf files
abbr -a i "$EDITOR *.idf"

function en --description 'Edit a note'
    set file (select_note)
    and "$EDITOR" "$MPNOTES"/"$file".md
end

function gn --description 'Grep notes';
    rg -i $argv[1] $MPNOTES
end

function cn --description 'Create note'
    # If file name given, edit file directly, otherwise cd to directory.
    if count $argv > /dev/null
        # Check if I put a ".md" extension at the end.
        if string match -q '*.md' $argv[1]
            "$EDITOR" "$DOTFILES"/notes/$argv[1]
        else
            "$EDITOR" "$DOTFILES"/notes/$argv[1].md
        end
    else
        cd "$DOTFILES"/notes
    end
end

function cs --description '[C]reate [s]cript. Just go to the scripts directory if no file name.'
    cd "$DOTFILES"/scripts
    if count $argv > /dev/null
        "$EDITOR" $argv[1]

        if test -e $argv[1]
            chmod +x $argv[1]
        end
    end
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

if test -f ~/.config/fish/secrets.fish
    source ~/.config/fish/secrets.fish
end

function update --description 'Universal package update'
    if command -s pacman >/dev/null
        sudo pacman -Syu
    else if command -s apt >/dev/null
        sudo apt update
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
