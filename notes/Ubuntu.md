# Ubuntu

## Packages

Source lists:

- `/etc/apt/sources.list`
- All files in `/etc/apt/sources.list.d/*`

## Installing .deb

```
sudo dpkg -i <package>.deb
# If missing dependencies
sudo apt-get install -f
```

```
# version
lsb_release -a
cat /etc/os-release

sudo do-release-upgrade # Ubuntu upgrade
```
