function path_prepend_gen
    # If the directory exists and isn't in the path, add it to the beginning of the path.
    if not contains $argv[1] $argv[2]; and test -d $argv[1]
        set -gxp $argv[2] $argv[1]
    end
end
