# Boot

Once in a while, my tower becomes a useful pile of trash and won't boot.
Some notes from last occurrence:

1. Make sure motherboard is set to only 'UEFI' not 'Legacy + UEFI'

2. Have a live USB with Manjaro on it ready.

<https://wiki.manjaro.org/index.php?title=GRUB/Restore_the_GRUB_Bootloader>

3. Boot into live USB.

4. Need to then mount main drive, EFI drive, and then other system drives.
    - ChatGPT gave me:
        sudo mount /dev/sdXn /mnt  # Mount root partition
        sudo mount /dev/sdYn /mnt/boot/efi  # Mount EFI partition, where sdYn is the EFI partition
    - However, `manjaro-chroot -a` should do all of this properly for me (and did work in this case)

5. Then do all the update grub stuff

```
sudo pacman -Syu grub
sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=manjaro --recheck
sudo update-grub
```
