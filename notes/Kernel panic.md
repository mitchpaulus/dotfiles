Tuesday 2023-07-18:

Fixed issue after Manjaro update, would not boot.
Message on screen was like:

```
Initramfs unpacking failed: invalid magic at start of compressed archive
Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)
CPU: 2 PID: 1 Comm: ....
```

Solution was at: <https://forum.manjaro.org/t/initramfs-unpacking-failed-invalid-magic-as-start-of-compressed/137451>

- Created bootable Manjaro USB stick
```
sudo manjaro-chroot -a
sudoedit /etc/mkinitcpio.conf  # Uncommented COMPRESSION=gzip line at end of file
mkinitcpio -P
update-grub
exit
```
