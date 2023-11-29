# `cron`

View logs:

```sh
journalctl -f -u cron.service  # -f for following
```

Run as `root` by default. <https://serverfault.com/a/247045>


Actual binary is at `/usr/sbin/cron`.
The script to start/stop is at `/etc/init.d/cron`.

```
sudo /etc/init.d/cron start
sudo /etc/init.d/cron stop
```

Base environment I got on Ubuntu on WSL:

```
HOME=/home/mp
LOGNAME=mp
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
LANG=C.UTF-8
SHELL=/bin/sh
PWD=/home/mp

whoami == mp
```

For WSL, [this article](https://julienharbulot.com/cron-windows.html) says you can add script to:
`C:\Users\<user name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.

/etc/environment file can be used to set environment variables for all users.

By default only had this single line:

```
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"
```
