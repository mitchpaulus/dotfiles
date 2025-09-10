ISO to USB

```sh
lsblk                                   # find device, e.g. /dev/sdX
sudo umount /dev/sdX*                   # unmount any partitions
sudo dd if=./image.iso of=/dev/sdX bs=4M iflag=fullblock oflag=direct status=progress conv=fsync
sync
```
