#!/usr/bin/fish

set -g fish_prompt_pwd_dir_length 5

set -gx DOTFILES ~/dotfiles
set -gx MPNOTES ~/dotfiles/notes
set -gx LOCALBIN ~/.local/bin
set -gx FILEMANAGER lf

# See https://github.com/pypa/pipenv/issues/5075
# My annoyance with the Python ecosystem grows.
set -gx SETUPTOOLS_USE_DISTUTILS stdlib

# Make LOCALBIN directory if it doesn't exist
mkdir -p $LOCALBIN

# Good ole U.S. of A.
set -gx TEXLIVE_INSTALL_PAPER letter
set -gx TEXLIVE_INSTALL_PREFIX "$HOME"/texlive

# See https://github.com/neovim/neovim/issues/14090#issuecomment-913837694
# and https://github.com/neovim/neovim/issues/15487
set -gx MANPAGER 'nvim +Man!'

set -g H /mnt/c/Users/mpaulus

# set -gxp MANPATH "$TEXLIVE_INSTALL_PREFIX"/2021/texmf-dist/doc/man
# set -gxp INFOPATH "$TEXLIVE_INSTALL_PREFIX"/2021/texmf-dist/doc/man

# Search for ANTLR stuff. Recommended location is /usr/local/lib/antlr-x.x.x-complete.jar. Sort and get latest.
set -gx ANTLR_JAR (find /usr/local/lib -name 'antlr-*-complete.jar' | sort -V | tail -n 1)

if count $ANTLR_JAR > /dev/null
    set -gx CLASSPATH ".:"$ANTLR_JAR[1]":$CLASSPATH"
end

set -gx AWKPATH ".:/usr/local/share/awk:$DOTFILES/awk_functions"
set -gx DOTREMINDERS ~/.config/remind/remind.rem
set -gx FZF_DEFAULT_OPTS '--reverse --margin 10% --border'
set -gx BAT_THEME 'Monokai Extended'

# Recommended by jekyll
set -gx GEM_HOME $HOME/gems

# Microsoft doesn't need my telemetry
set -gx DOTNET_CLI_TELEMETRY_OPTOUT 1

set -gx TASKRC $HOME/.config/taskwarrior/.taskrc

set -gx JAVA_HOME /usr/local/jdk-17.0.2/

# Required for Haxall - See https://github.com/haxall/haxall
set -gx FAN_BUILD_JDKHOME "$JAVA_HOME"

path_prepend "$JAVA_HOME"/bin
path_prepend "$DOTFILES"/scripts/
path_prepend "$DOTFILES"/python
path_prepend "$DOTFILES"/haskell
path_prepend /usr/local/texlive/2020/bin/x86_64-linux
path_prepend /usr/local/texlive/2023/bin/x86_64-linux
path_prepend "$TEXLIVE_INSTALL_PREFIX"/2021/bin/x86_64-linux
path_prepend "$TEXLIVE_INSTALL_PREFIX"/2022/bin/x86_64-linux
path_prepend "/opt/fantom-1.0.76/bin"
# Recommended by jekyll
path_prepend $HOME/gems/bin
path_prepend $HOME/.local/share/gem/ruby/3.0.0/bin
path_prepend "$HOME/.gem/ruby/2.7.0/bin"
path_prepend "$HOME/.gem/ruby/3.0.0/bin"
path_prepend "$HOME/bin"
path_prepend "$HOME/.local/bin"
path_prepend "/mnt/d/PortablePrograms/tabula-win-1.2.1/tabula"
path_prepend $HOME/.pyenv/bin

# Neovim/Vim for all the things
if command -v nvim >/dev/null 2>&1
    set -gx EDITOR nvim
    set -gx VISUAL nvim
    set -gx SUDO_EDITOR (which nvim)
else if command -v vim >/dev/null 2>&1
    set -gx EDITOR vim
    set -gx VISUAL vim
    set -gx SUDO_EDITOR (which vim)
end

if command -v exa >/dev/null 2>&1
    function ls --wraps exa
        exa $argv
    end
end

# https://github.com/fish-shell/fish-shell/issues/6991
# For discussion on why you can't redirect the syntax error messages, which I disagree with.
# Just becuase I check above doesn't mean that it's guaranteed to exist on the line below.
command -q vivid; and set -gx LS_COLORS (vivid generate dracula)

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
# - https://learn.microsoft.com/en-us/windows/terminal/tutorials/new-tab-same-directory
# Removed quoting since it jacked with the syntax highlighting
if test -n "$WT_SESSION"
    # On a change of PWD, store the PWD using the 9;9 escape sequence
    function windows-terminal --on-variable PWD
        printf \e]9\;9\;%s\e\\ (wslpath -m "$PWD")
    end
end

function add_help
    commandline -i -- --help
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

# 2022-05-26, gave it a try. But I don't find myself using any of the bindings.
# fish_vi_key_bindings
fish_default_key_bindings

# \e is ALT, mapped to Caps Lock
bind \ed add_date
bind \eu fish_underscore_command
bind \eB awk_begin
bind \ew add_count_lines
bind \ec add_copy_to_clip_exe

bind \e1 1

# ALT-o to exit, don't need to set the command in each terminal emulator with this here.
bind \eo exit

bind qh add_help

# The purpose of this function is to be able to execute commands from keybindings,
# without explicitly hitting the Enter key.
function bind_exec
    commandline $argv[1]
    and commandline -f execute
end

function git_status
    bind_exec 'git status -u'
end

function git_diff; bind_exec 'git diff'; end
function git_commit; bind_exec 'git commit'; end
function repos; bind_exec 'r'; end
function filemanager; bind_exec 'f'; end
function workdir; bind_exec 'j'; end

function clear_terminal
    # Stolen from default C-L binding
    echo -n (clear | string replace \\e\\\[3J ""); commandline -f repaint
end

# Don't want to press Enter any more.
# Have to execute more than I have to enter in ';'
bind ';r' repos
bind ';f' filemanager
bind ';j' workdir
bind ';c' workdir

bind jc git_commit
bind jd git_diff
bind jf execute
bind jj workdir
bind jw workdir

# moved vl for clearing to match CTRL-L.
bind vj forward-char execute
bind vl clear_terminal
bind qk exit

function work_dir_search
    cd '/mnt/c/Users/mpaulus/Command Commissioning/'
    fzf-tmsu -d
    clear_terminal
end

bind zd work_dir_search

# Historical Vi binding stuff
# set fish_cursor_insert line
# bind -M insert \e1 1
# bind -M insert \ew add_count_lines
# bind -M insert \ed add_date
# bind -M insert jf to_normal_mode
# bind -M insert \cn down-or-search
# bind -M insert \cp up-or-search
# bind -M insert \ey accept-autosuggestion
# bind -M insert \cf accept-autosuggestion
# bind -M insert \eo exit
# bind H beginning-of-line
# bind L end-of-line

for dir in "$DOTFILES"/python "$REPOS"/ccllc-skyspark
    path_prepend_gen "$dir" PYTHONPATH
    path_prepend_gen "$dir" MYPYPATH
end

# v for VIM
abbr -a v $EDITOR

# Short for ANTLR, open all g4 files
abbr -a an "$EDITOR (fd -e g4)"
abbr -a ap "$EDITOR (fd -e g4 Parser)"
abbr -a al "$EDITOR (fd -e g4 Lexer)"

abbr -a wttr 'curl \'wttr.in/Dallas?format=%l:+%C+%t+%h+%w\''

abbr -a gi "$EDITOR .gitignore"

# Consecutive numbering by default.
abbr -a mdformat 'mdformat --number'

abbr -a x 'chmod +x'
abbr -a lg lazygit
abbr -a md 'mkdir'
abbr -a mk 'mkdir'
abbr -a mkd 'mkdir'
abbr -a pf 'printf'
abbr -a rd 'nvim README.md'

# 'Last Vim' - Awesome alias from: https://liam.rs/posts/From-bash-to-vim-and-back/
abbr -a lv 'nvim -c "normal \'0" -c bd1'

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
    abbr -a cl 'git clone'
    abbr -a stash 'git stash'
end

# When more than 1 character is too much
abbr -a f "$FILEMANAGER"

abbr -a uuid uuidgen

abbr -a py python3

# On basic Ubuntu install, python3 is installed, but no symlink for python
if not command --query python; and command --query python3
    if test -d "$LOCALBIN"
        ln -s -r -f (command -s python3) $LOCALBIN/python
    end
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


function lf --wraps=lf
    set config_dir  "$HOME/.config/lf"
    # Make config directory if it doesn't exist
    if test '!' -d "$config_dir"; mkdir -p  "$config_dir"; or return 1; end
    command lf -last-dir-path "$config_dir"/lf_lastdir $argv; and cd (cat "$config_dir"/lf_lastdir)
end

abbr -a u 'cd ..'
abbr -a t task
abbr -a mkdri mkdir

function g
    cd '/mnt/c/Users/mpaulus/Command Commissioning/'
    fzf-tmsu
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

# OPENER is used in the lf file mananger when using the 'l' key.
if test -n "$WSL_DISTRO_NAME"
    # This is located in a separate repo that will have to be cloned
    # See: https://github.com/mitchpaulus/wsl-opener
    set -gx OPENER wsl-opener

    # Command to bring up Windows Explorer in current directory.
    # Use 'Files' if installed.
    if command --query files.exe
        function eh
            files.exe (wslpath -w (pwd))
        end
    else
        function eh
            explorer.exe (wslpath -w (pwd))
        end
    end
else
    # This is a script in this dotfiles repo, so should always be good to go.
    set -gx OPENER unix-opener
end

# Nix Package Manager
test -d ~/.nix-profile; and nix_setup

# Load configuration special to given computer
test -f ~/.config/fish/host-config.fish; and source ~/.config/fish/host-config.fish
test -f ~/.config/fish/secrets.fish; and source ~/.config/fish/secrets.fish

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
     path_prepend "$HOME"/.cabal/bin
     path_prepend /home/mitch/.ghcup/bin
 end
#
# Yet another version manager. nvm = node version manager.
set -gx NVM_DIR "$HOME/.nvm"
if test -s "$NVM_DIR/nvm.sh"; bash "$NVM_DIR/nvm.sh"; end

# vim:ft=fish
