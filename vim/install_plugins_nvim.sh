#!/bin/sh
set -e
mkdir -p ~/.config/nvim/pack/mp/start/

while read -r plugin; do
    if test -d ~/.config/nvim/pack/mp/start/"$plugin"; then
        echo "Plugin $plugin already installed"
        continue
    fi
    git clone git@github.com:mitchpaulus/"$plugin".git ~/.config/nvim/pack/mp/start/"$plugin"
done < plugins.txt
