function path_prepend
    # If the directory exists and isn't in the path, add it to the beginning of the path.
    if not contains $argv[1] $PATH; and test -d $argv[1]
        set -gxp PATH $argv[1]
    end
end
