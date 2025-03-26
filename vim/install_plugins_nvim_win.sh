#!/usr/bin/env mshell

soe
$REPOS? not ("$REPOS env var is not defined" wle 1 exit) iff
$LOCALAPPDATA? not ("$LOCALAPPDATA env var is not defined" wle 1 exit) iff

$"{$LOCALAPPDATA}/nvim/pack/mp/start/" mkdirp
$"{$LOCALAPPDATA}/nvim/pack/github/start/" mkdirp

#!/bin/sh
# set -e
# mkdir -p ~/.config/nvim/pack/mp/start/
# mkdir -p ~/.config/nvim/pack/github/start/

# while read -r plugin; do
    # # Check if REPOS is defined

    # if test -z "$REPOS"; then
        # printf "REPOS not defined"
        # exit 1
    # fi

    # if test -e ~/.config/nvim/pack/mp/start/"$plugin"; then
        # echo "Plugin $plugin already installed"
        # continue
    # fi

    # git clone git@github.com:mitchpaulus/"$plugin".git "$REPOS"/"$plugin"
    # ln -s "$REPOS"/"$plugin" ~/.config/nvim/pack/mp/start/"$plugin"
# done < plugins.txt

# while read -r opt_plugin; do
    # PACKAGE_NAME="$(printf "%s" "$opt_plugin" | cut -d'/' -f2)"
    # if test -d ~/.config/nvim/pack/github/start/"$PACKAGE_NAME"; then
        # echo "Plugin $opt_plugin already installed"
        # continue
    # fi
    # git clone --depth 1 git@github.com:"$opt_plugin".git ~/.config/nvim/pack/github/start/"$PACKAGE_NAME"
# done < opt_plugins.txt
