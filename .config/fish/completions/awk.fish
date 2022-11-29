complete -c awk -s f -l file -x -a '(find . -name "*.awk" -printf "%P\n")'
