#!/bin/env bash

checkfile() {
    if [[ -f "$2" ]]; then
        read -p "Do you want to overwrite $2? (y/n) " response

        if [[ "$response" == "y" ]]; then
            printf "Linking %s to %s...\n" "$2" "$1"
            ln -sfr "$1" "$2"
        else
            printf "Skipping file %s...\n" "$2"
        fi
    else
        printf "Linking %s to %s...\n" "$2" "$1"
        echo ln -sfr "$1" "$2"
        ln -sfr "$1" "$2"
    fi
}

CURRDIR="$(dirname "$0")"

checkfile "$CURRDIR"/.minttyrc ~/.minttyrc
checkfile "$CURRDIR"/.tmux.conf ~/.tmux.conf
checkfile "$CURRDIR"/i3/config ~/.config/i3/config
