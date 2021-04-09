# Go to meetings folder
function gm
    set dir  '/mnt/c/Users/mpaulus/OneDrive - Command Commissioning/meetingnotes'
    if test -d  "$dir"
        cd "$dir"
    else
        printf '%s is not a directory.\n' "$dir"
    end
end
