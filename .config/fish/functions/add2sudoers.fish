# Script to quickly add current user to sudoers
function add2sudoers
    printf "%s ALL=(ALL) NOPASSWD:ALL\n"  (whoami) | sudo tee /etc/sudoers.d/(whoami)
end
