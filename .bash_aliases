alias ea='"$EDITOR" ~/.bash_aliases'
alias r='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'
# [S]ource .[b]ashrc
alias sb='source ~/.bashrc && printf ".bashrc reloaded.\n"'
alias vim='nvim'
alias v='nvim'

# Update a .gitignore file for Visual Studio projects.
vsignore() {
    curl https://raw.githubusercontent.com/github/gitignore/master/VisualStudio.gitignore > .gitignore
}
