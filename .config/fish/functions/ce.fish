function ce --description 'Change Extension'
    if test (count $argv) -lt 2
        printf 'ce FILE EXT'
        return 1
    end

    # Check which argument is longer, assume extension is the shorter of the two.
    if test (string length $argv[1]) -gt (string length $argv[2])
        path change-extension $argv[2] $argv[1]
    else
        path change-extension $argv[1] $argv[2]
    end
end
