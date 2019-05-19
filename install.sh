#!/bin/env bash

checkfile() {
    if [[ -f "$2" ]]; then
        read -p "Do you want to overwrite $2? (y/n) " response

        if [[ "$response" == "y" ]]; then
            printf "Linking %s to %s...\n\n" "$2" "$1"
            ln -sfr "$1" "$2"
        else
            printf "Skipping file %s...\n\n" "$2"
        fi
    else
        read -p "Install $2? ([y]/n)" response

        if [[ "$response" == "y" ]] || [[ "$response" == "" ]]; then
            printf "Linking %s to %s...\n" "$2" "$1"
            mkdir -p "$(dirname "$2")"
            ln -sfr "$1" "$2"
            printf "\n\n"
        fi
    fi
}


CURRDIR="$(dirname "$0")"

checkfile "$CURRDIR"/i3/config ~/.config/i3/config
checkfile vim/vimrc ~/.config/nvim/init.vim
checkfile .bashrc ~/.bashrc
checkfile .bash_aliases ~/.bash_aliases
checkfile alacritty.yml ~/.config/alacritty/alacritty.yml
checkfile .gitconfig ~/.gitconfig

read -p "Which version of tmux.conf do you want? 1 = new, 2 = old" response
if [[ "$response" == "1" ]]; then
    checkfile "$CURRDIR"/.tmux.conf.new ~/.tmux.conf
elif [[ "$response" == "2" ]]; then
    checkfile "$CURRDIR"/.tmux.conf ~/.tmux.conf
fi

read -p "Do you want to download vim-plug? ([y]/n) " response
if [[ "$response" == "y" ]] || [[ "$response" == "" ]]; then
    curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
            https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
fi

# Make neovim plugin directory for my plugins.
plugindir=~/.local/share/nvim/site/pack/mitch/start
mkdir -p $plugindir

read -p "Do you want to clone down vim plugins? (y/n) " response
if [[ "$response" == "y" ]] || [[ "$response" == "" ]]; then
    git clone https://github.com/mitchpaulus/autocorrect.vim.git $plugindir/autocorrect.vim
    git clone https://github.com/mitchpaulus/sensible.vim.git $plugindir/sensible.vim
fi

if [[ ! -d "~/mitchpaulus.github.io/" ]]; then
    read -p "Do you want to clone down website (y/n)? " response
    if [[ "$response" == "y" ]] || [[ "$response" == "" ]]; then
        git clone https://github.com/mitchpaulus/mitchpaulus.github.io.git ~/mitchpaulus.github.io
    fi
fi
