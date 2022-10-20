function mppw --description "Gen password with default settings"
    pwgen -cnysB -r '[]{}<>"\':.+;,?' 14 1
end
