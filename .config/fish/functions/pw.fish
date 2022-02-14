function pw
    if command -q pwgen
        pwgen -n -c -y -B 14 1
    else
        printf 'pwgen not installed. `sudo apt install pwgen`.\n'
    end
end
