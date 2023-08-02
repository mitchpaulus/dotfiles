#!/bin/sh

set -e

NVIM_DATA_DIR="$(wslpath -u "$(winenv USERPROFILE)")"/AppData/Local/nvim-data/site/autoload
mkdir -p "$NVIM_DATA_DIR"
curl -fLo "$NVIM_DATA_DIR"/plug.vim https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

NVIM_DIR="$(wslpath -u "$(winenv USERPROFILE)")"/AppData/Local/nvim/
mkdir -p "$NVIM_DIR"
cp ../.config/nvim/init.lua "$(wslpath -u "$(winenv USERPROFILE)")"/AppData/Local/nvim/init.lua
