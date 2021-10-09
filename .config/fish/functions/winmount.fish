function winmount
    set lowercase_letter (string lower $argv[1])
    set uppercase_letter (string upper $argv[1])

    if [ ! -d /mnt/"$lowercase_letter" ]
        sudo mkdir -p /mnt/"$lowercase_letter"
    end
    sudo mount -t drvfs "$uppercase_letter": /mnt/"$lowercase_letter"
end
