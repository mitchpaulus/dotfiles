#!/bin/sh

# See discussions:
# https://github.com/gokcehan/lf/issues/234
# https://github.com/sharkdp/bat/issues/490#issuecomment-511338924

# $1 = file path
# $2 = optional number of lines to show

unset COLORTERM

# if two arguments (program counts as one)
if test "$#" -eq 3; then
    bat --italic-text always --color always --style 'plain' --theme 'ansi' --line-range ":$2" "$1"
else
    bat --italic-text always --color always --style 'plain' --theme 'ansi' "$1"
fi
