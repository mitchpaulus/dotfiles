function m
    if test -f Makefile
        "$EDITOR" Makefile;
    else
        printf "Makefile not found\n"
    end
end
