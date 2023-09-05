#!/bin/sh

DOTFILES="$(find ~ -name 'dotfiles' -type d | head -n 1)"

if test -z "$DOTFILES"; then
	printf "Could not find dotfiles\n"
	exit 1
fi

# $1 is the normal expected system location.
# $2 is the location of file in this repository.
# checkfile [destination location] [dotfile relative location]
checkfile() {
    # If the file is already a symbolic link, assume
    # that it is correctly pointing to what we want.
    if [ -L "$1" ]; then return 0; fi

    if [ -f "$1" ]; then
        prompt "Do you want to overwrite $1? (y/n) "

        if yesresponse "$response"; then
            printf "Linking %s to %s...\n\n" "$1" "$2"
            ln -s -f  "$DOTFILES"/"$2" "$1"
        else
            printf "Skipping file %s...\n\n" "$1"
        fi
    else
        prompt "Install $1? ([y]/n)"

        if yesresponse "$response"; then
            printf "Linking %s to %s...\n" "$1" "$2"
            # Make the required subdirectories if required
            mkdir -p "$(dirname "$1")"
            ln -s "$DOTFILES"/"$2" "$1"
            printf "\n"
        fi
    fi
}

# Test whether something is a command
iscommand() {
    command -v "$1" >/dev/null 2>/dev/null
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

install_npm() {
    if iscommand npm; then return 0; fi

    # npm should come along with node in Ubuntu
    if iscommand apt; then sudo apt install nodejs; fi
}

install_bash_language_server() {
    install_npm && sudo npm install -g bash-language-server
}

# Try installing various dotfiles
#           final destination                   relative repo location
checkfile   ~/.config/i3/config                 i3/config
checkfile   ~/.config/nvim/init.lua             .config/nvim/init.lua
checkfile   ~/.bashrc                           .bashrc
checkfile   ~/.bash_aliases                     .bash_aliases
checkfile   ~/.config/alacritty/alacritty.yml   .config/alacritty/alacritty.yml
checkfile   ~/.config/git/config                .gitconfig
checkfile   ~/.config/i3blocks/config           i3blocks/config
checkfile   ~/.config/tmux/bash_completion_tmux.sh           scripts/bash_completion_tmux.sh
checkfile   ~/.config/fish/functions                      .config/fish/functions
checkfile   ~/.config/fish/completions                      .config/fish/completions
checkfile   ~/.config/fish/conf.d                      .config/fish/conf.d
checkfile   ~/.config/fish/config.fish                      .config/fish/config.fish
checkfile   ~/.config/lf/lfrc                   .config/lf/lfrc
checkfile   ~/.tmux.conf                        .tmux.conf
checkfile   ~/.config/vsnip                     .config/vsnip/
checkfile   ~/.config/NuGet/config/mp.config    .config/NuGet/config/mp.config
checkfile   ~/.nuget/config/mp.config           .config/NuGet/config/mp.config
checkfile   ~/.config/lazygit/config.yml        .config/lazygit/config.yml

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
    git clone https://github.com/mitchpaulus/sensible.vim.git $plugindir/sensible.vim
fi

if [ ! -d "$HOME/mitchpaulus.github.io/" ]; then
    prompt "Do you want to set up website (y/n)? "
    if yesresponse "$response"; then
        scripts/install-website.sh
    fi
fi

if [ ! -d "$HOME/config-notes" ]; then
    prompt "Do you want to set up computer config notes (y/n)? "
    if yesresponse "$response"; then
        git clone https://github.com/mitchpaulus/config-notes.git ~/config-notes
    fi
fi

if uname -a | grep -q -i "arch"; then
    sudo pacman -S acpi alacritty compton feh firefox fish git i3 i3blocks \
        neovim openvpn openssh ranger rofi shellcheck tmux xclip \
        zathura zathura-pdf-mupdf
else
    printf "Did not grab packages for particular OS.\n"
fi

# Set up ssh with website server
prompt "Set up SSH with website? [y]/n"
if yesresponse "$response"; then
    scripts/install-website-ssh.sh
fi

if ! iscommand bash-language-server; then
    prompt "Install bash language server? [y]/n? "
    if yesresponse "$response"; then
        install_bash_language_server
    fi
fi

if ! iscommand mgitstatus; then
    prompt "Install mgitstatus? [y]/n? "
    if yesresponse "$response"; then
        install/install_mgitstatus
    fi
fi
