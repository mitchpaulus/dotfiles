function cdep --description 'Change to EnergyPlus directory'

    # Check for existence of WSL_DISTRO_NAME environment variable
    if test -n "$WSL_DISTRO_NAME"
        cd (find /mnt/c/ -maxdepth 1 -type d -name 'EnergyPlus*' | sort -rV | head -n 1)
    end
end
