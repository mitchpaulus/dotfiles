alias ea='"$EDITOR" ~/.bash_aliases'
alias r='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'

# Update a .gitignore file for Visual Studio projects.
vsignore() {
    curl https://raw.githubusercontent.com/github/gitignore/master/VisualStudio.gitignore > .gitignore
}
