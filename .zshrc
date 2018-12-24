# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=5000
SAVEHIST=5000
unsetopt beep
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/mp/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
EDITOR=vim
PS1='%{$fg[red]%}%~ %# '

alias ll='ls -l --color -h'
