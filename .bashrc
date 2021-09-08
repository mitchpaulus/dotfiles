#!/bin/bash

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=10000
HISTFILESIZE=20000
HISTTIMEFORMAT="%F %T	"

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
shopt -s globstar

# whiteback='\[\e[48;5;15m\]'
# blackfore='\[\e[30m\]'
yellowfore='\[\e[33m\]'
bluefore='\[\e[34m\]'
cyanfore='\[\e[36m\]'
# whitefore='\[\e[37m\]'
bright_yellow_fore='\[\e[93m\]'
reset='\[\e[0m\]'

ps1_in_git() {
    if git branch >/dev/null 2>&1; then printf "::"; else printf "☣\n"; fi
}

PS1="${bluefore}\w\n${bright_yellow_fore}"'$(ps1_in_git)'"${reset} "

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    ( test  -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" ) || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias dir='dir --color=auto'
    alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

alias diff='diff --color=auto'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Alias definitions.
# shellcheck disable=SC1090
if [ -f ~/.bash_aliases ]; then . ~/.bash_aliases; fi

bind '"\C-p": history-search-backward'
bind '"\C-n": history-search-forward'

getlast() {
    fc -ln "$1" "$1" | sed '1s/^[[:space:]]*//'
}

# [Q]uick [F]ind.
qf() { find . -iname "*$1*" ; }

function pathadd {
  case ":$PATH:" in
    *":$1:"*) :;; # already there
    *) if [ -z "$2" ]; then PATH="$1:$PATH"; else PATH="$PATH:$1"; fi ;; # or PATH="$PATH:$1"
  esac
}

# Required for using Antlr
export CLASSPATH=".:/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH"

# Pretty print the path variable
pathpp() { printf "%s" "$PATH" | awk 'BEGIN { RS=":" } { print }' | sort ; }

# [E]dit .[b]ashrc
eb() { "$EDITOR" ~/.bashrc ; }

ev() { "$EDITOR" ~/dotfiles/vim/vimrc ; }

# Edit notes
en() {
    if [ "$TMUX" ]; then
        tmux switch-client -t "work:notes"
    else
        printf "Not running tmux.\n"
    fi
}

# Go to dotfiles
gd() { cd ~/dotfiles || return ; }

wttr() { curl 'wttr.in/Dallas?format=%l:+%C+%t+%h+%w'; }

m() { "$EDITOR" Makefile ; }

# Save keystrokes moving up a directory.
u() { cd .. ;  }

# Open EnergyPlus I/O reference
epio() { cmd.exe /C start 'C:\EnergyPlusV9-3-0\Documentation\InputOutputReference.pdf'; }

epdoc() { explorer.exe 'C:\EnergyPlusV9-3-0\Documentation'; }

hnotes() { "$EDITOR" '/mnt/c/Users/mpaulus/GoogleDrive/notes/home tasks.md' ; }

alias vim='nvim'
alias v='nvim'

# [S]ource .[b]ashrc
alias sb='source ~/.bashrc && printf ".bashrc reloaded.\n"'

export EDITOR=nvim

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    # shellcheck disable=SC1091
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    # shellcheck disable=SC1091
    . /etc/bash_completion
  fi
fi

# Add single letter commands for common git operations
if command -v git >/dev/null 2>&1; then
    a() { git add       "$@"; }
    d() { git diff      "$@"; }
    s() { git status -u "$@"; }
    c() { git commit    "$@"; }
    p() { git push      "$@"; }
fi

# Quickly make new session and base work session
ns() { tmux new-session -s "$*"; }

nw() { tmux new-session -s work; }

ta() {
    case "$(tmux ls 2>&1)" in
        "no server running"* )  tmux ls;;
        *)
            if [ "$(tmux ls | wc -l)" -gt 1 ]; then
                tmux attach-session -t "$(tmux ls | awk -F ':' '{print $1}' | fzf)"
            else
                tmux attach-session -t "$(tmux ls | awk -F ':' '{print $1;exit}')"
            fi
        ;;
    esac
}

# Open daily notes.
odn()
{
    cd "/mnt/c/Users/mpaulus/OneDrive - Command Commissioning/dailynotes/" || exit 1
    if [ -n "$TMUX" ]; then
        tmux rename-window "notes"
    fi
    "$EDITOR" "$(find . -type f -name "[2]*.markdown" | sort | tail -n 1)"
}

# -R is to make this a read only operation if nvim is the EDITOR
helpbash() { nvim -R ~/dotfiles/help/bash.markdown; }

# Mount a Windows network drive like M:\. Use like 'winmount m'
winmount() { if [ ! -d /mnt/"${1,,}" ]; then sudo mkdir -p /mnt/"${1,,}"; fi ; sudo mount -t drvfs "${1^^}": /mnt/"${1,,}" ; }

# Source git tab-completion if available.
if [[ -a ~/git-completion.bash ]]; then
    # shellcheck disable=SC1090
    source ~/git-completion.bash
fi

if [[ ! -a ~/.config/tmux/bash_completion_tmux.sh ]]; then
    mkdir -p ~/.config/tmux/
    curl https://raw.githubusercontent.com/imomaliev/tmux-bash-completion/master/completions/tmux > ~/.config/tmux/bash_completion_tmux.sh
    chmod 755 ~/.config/tmux/bash_completion_tmux.sh
fi
# shellcheck disable=SC1090
source ~/.config/tmux/bash_completion_tmux.sh

# Enable bash-completion for stack if it is installed.
if [[ $(command -v stack) ]]; then
    eval "$(stack --bash-completion-script stack)"
fi

pathadd "$HOME"/dotfiles/scripts/

# Add computer specific commands and overwrites.
if [[ -f ~/.host-bashrc ]]; then
    # shellcheck disable=SC1090
    source ~/.host-bashrc
fi

# I hate all these programs that have to automatically add lines to my configs. But alas, here they are.
[ -f ~/.fzf.bash ] && source ~/.fzf.bash
# Node version manager
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
