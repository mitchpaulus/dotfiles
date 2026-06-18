#!/usr/bin/env mshell
# See discussions:
# https://github.com/gokcehan/lf/issues/234
# https://github.com/sharkdp/bat/issues/490#issuecomment-511338924

# $1 = file path
# $2 = optional number of lines to show
'COLORTERM' unsetenv
args len 2 = if [--line-range $":{$2}"] else [] end lineRange!
['bat' '--italic-text' always --color always --style 'plain' --theme 'Visual Studio Dark+' @lineRange $1]!
