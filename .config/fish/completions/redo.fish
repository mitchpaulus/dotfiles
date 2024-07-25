complete -c redo -f
complete -c redo -k -a '(find  -name .git -prune -o -name .redo -prune -o -name __pycache__ -prune -o -type f "!" -name "*.do"  -print | cut -c 3- | sort)'
complete -c redo -k -a '(rt)'
