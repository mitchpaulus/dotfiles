function chext --description 'Change extension of file'
    printf "%s%s" (string match -r '.*\.' $argv[1]) $argv[2]
end
