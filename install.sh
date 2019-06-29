#!/bin/sh

# $1 is the normal expected system location.
# $2 is the location of file in this repository.
checkfile() {
    # If the file is already a symbolic link, assume
    # that it is correctly pointing to what we want.
    if [ -L "$1" ]; then return 0; fi

    if [ -f "$1" ]; then
        prompt "Do you want to overwrite $1? (y/n) "

        if yesresponse "$response"; then
            printf "Linking %s to %s...\n\n" "$1" "$2"
            ln -sfr "$2" "$1"
        else
            printf "Skipping file %s...\n\n" "$1"
        fi
    else
        prompt "Install $1? ([y]/n)"

        if yesresponse "$response"; then
            printf "Linking %s to %s...\n" "$1" "$2"
            mkdir -p "$(dirname "$1")"
            ln -sfr "$2" "$1"
            printf "\n\n"
        fi
    fi
}

# Prompt user from something, store in 'response'
prompt() {
    printf "%s" "$1"
    read -r response
}

yesresponse() {
    if [ "$1" = "y" ] || [ "$1" = "Y" ] || [ "$1" = "yes" ] || [ -z "$1" ]; then
        return 0
    else
        return 1
    fi
}

# Try installing various dotfiles
checkfile   ~/.config/i3/config                 i3/config
checkfile   ~/.config/nvim/init.vim             vim/vimrc
checkfile   ~/.bashrc                           .bashrc
checkfile   ~/.bash_aliases                     .bash_aliases
checkfile   ~/.config/alacritty/alacritty.yml   .config/alacritty/alacritty.yml
checkfile   ~/.gitconfig                        .gitconfig

if [ ! -L ~/.tmux.conf ]; then
    prompt "Which version of tmux.conf do you want? 1 = new, 2 = old, 3 = skip "
    if [ "$response" = "1" ]; then
        checkfile ~/.tmux.conf "$CURRDIR"/.tmux.conf.new
    elif [ "$response" = "2" ]; then
        checkfile ~/.tmux.conf "$CURRDIR"/.tmux.conf
    fi
fi

if [ ! -f ~/.local/share/nvim/site/autoload/plug.vim ]; then
    prompt "Do you want to download vim-plug? ([y]/n) "
    if yesresponse "$response"; then
        curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
            https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    fi
fi

# Make neovim plugin directory for my plugins.
plugindir=~/.local/share/nvim/site/pack/mitch/start
mkdir -p $plugindir

prompt "Do you want to clone down vim plugins? (y/n) "
if yesresponse "$response"; then
    git clone https://github.com/mitchpaulus/autocorrect.vim.git $plugindir/autocorrect.vim
    git clone https://github.com/mitchpaulus/sensible.vim.git $plugindir/sensible.vim
fi

if [ ! -d "$HOME/mitchpaulus.github.io/" ]; then
    prompt "Do you want to set up website (y/n)? "
    if yesresponse "$response"; then
        git clone https://github.com/mitchpaulus/mitchpaulus.github.io.git ~/mitchpaulus.github.io

        if pacman -Qi ruby >/dev/null 2>/dev/null; then
            printf "Need to install ruby...\n"
            pacman -S ruby
        fi

        gem install bundler jekyll

    fi
fi

if [ ! -d "$HOME/config-notes" ]; then
    prompt "Do you want to set up computer config notes (y/n)? "
    if yesresponse "$response"; then
        git clone https://github.com/mitchpaulus/config-notes.git ~/config-notes
    fi
fi

# Set up ssh with website server
prompt "Set up SSH with website? [y]/n"
if yesresponse "$response"; then
    ssh-keygen -t rsa -b 4096
    ssh-copy-id root@199.192.25.72
    printf "Adding 'psy' as a known host to ~/.ssh/config...\n"
    printf "Host psy\n    User root\nHostname 199.192.25.72\n" >> ~/.ssh/config
fi

