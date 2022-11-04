function rlast --description "Remove last n number of chars from string. Doesn't matter what order the args are in."
    if printf '%s' $argv[1] | grep -q '^[1-9][0-9]*$'
        set num $argv[1]
        set string_val $argv[2]
    else
        set num $argv[2]
        set string_val $argv[1]
    end
    string sub --end=-$num $string_val
end
