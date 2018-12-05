alias ea='gvim ~/.bash_aliases'
alias r='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'
alias gs='git status -u'
alias gd='git diff'
# [S]ource .[b]ashrc
alias sb='source ~/.bashrc && printf ".bashrc reloaded.\n"'
