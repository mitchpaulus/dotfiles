complete -c xlim -s v -l version -d "Print version information"
complete -c xlim -s h -l help -d "Print help"
complete -c xlim --exclusive -s x -l xl -l excel -d "Write to Excel file"
complete -c xlim -l line-nums -d "Print with line numbers instead of identifiers"
# The --strip-cwd-prefix is required, since by default, the paths output will start with './' and
# fish hides any completions start with a dot. See https://github.com/fish-shell/fish-shell/issues/3707
complete -c xlim -x -a "(fd --strip-cwd-prefix -e xlim)"
