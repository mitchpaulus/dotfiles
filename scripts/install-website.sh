#!/bin/sh

# This script clones down website and checks for the
# dependencies required for jekyll
if [ ! -d ~/mitchpaulus.github.io ]; then
    git clone https://github.com/mitchpaulus/mitchpaulus.github.io.git ~/mitchpaulus.github.io
fi


if command -v pacman >/dev/null; then
    if ! ( pacman -Qi ruby >/dev/null 2>/dev/null ); then
        printf "Need to install ruby...\n"
        sudo pacman -S ruby
    fi

fi

gem install bundler jekyll


