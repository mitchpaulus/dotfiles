function odn
    cd "/mnt/c/Users/mpaulus/OneDrive - Command Commissioning/dailynotes/"; or return 1
    if [ -n "$TMUX" ]
        tmux rename-window "notes"
    end
    nvim (find . -type f -name "[2]*.markdown" | sort | tail -n 1)
end

set -gx PATH /usr/java/jdk-14.0.2/bin/ $PATH
