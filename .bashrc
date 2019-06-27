# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
shopt -s globstar

whiteback='\[\e[48;5;15m\]'
blackfore='\[\e[30m\]'
bluefore='\[\e[34m\]'
cyanfore='\[\e[36m\]'
reset='\[\e[0m\]'

PS1="${cyanfore}\w\n${cyanfore}:: ${reset}"

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias dir='dir --color=auto'
    alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Alias definitions.
if [ -f ~/.bash_aliases ]; then . ~/.bash_aliases; fi

bind '"\C-p": history-search-backward'
bind '"\C-n": history-search-forward'

getlast() {
    fc -ln "$1" "$1" | sed '1s/^[[:space:]]*//'
}

# [Q]uick [F]ind.
qf() {
    find . -iname "*$1*"
}

pdfmerge() {
    gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -sOutputFile="$@"
}

export EDITOR=nvim

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# Source git tab-completion if available.
if [[ -a ~/git-completion.bash ]]; then
    source ~/git-completion.bash
fi

# Enable bash-completion for stack if it is installed.
if [[ $(command -v stack) ]]; then
    eval "$(stack --bash-completion-script stack)"
fi

# Add computer specific commands and overwrites.
if [[ -f ~/.host-bashrc ]]; then
    source ~/.host-bashrc
fi
