complete -c msh -s h -l help -d 'Show help'
complete -c msh -l parse -d "Print the parsed Abstract Syntax Tree"
complete -c msh -l lex -d "Print the tokens of the input"
complete -c msh -k -x -a "(__fish_complete_suffix .msh)"
