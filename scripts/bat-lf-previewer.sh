#!/bin/sh

# See discussions:
# https://github.com/gokcehan/lf/issues/234
# https://github.com/sharkdp/bat/issues/490#issuecomment-511338924

unset COLORTERM
bat --color always --style 'plain' --theme 'ansi-dark' "$1"
