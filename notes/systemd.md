# Cron Alternative

[Directives](https://www.freedesktop.org/software/systemd/man/latest/systemd.directives.html)

<https://www.freedesktop.org/software/systemd/man/latest/systemd.syntax.html#>

```
# /etc/systemd/system/myservice.service
# Service Unit File
[Unit]
Description=My Service

[Service]
Environment=VAR1=VALUE1 VAR2=VALUE2 # Or on separate lines
ExecStart=/path/to/script.sh
Type=oneshot
```

```conf
# /etc/systemd/system/myservice.timer
[Unit]
Description=Run My Service every 5 minutes

[Timer]
OnCalendar=*:00,05,10,15,20,25,30,35,40,45,50,55
# OnCalendar=Mon..Fri *-*-* 07:40:00
Persistent=true

[Install]
WantedBy=timers.target
```

```
systemctl list-timers --all
journalctl -u myservice -f # -f for follow
```

Type    | Description                                                                                        | Use Case
--------|----------------------------------------------------------------------------------------------------|---------------------------------------------------
simple  | The default; the service starts immediately.                                                       | Most services that don’t fork or run in background
forking | The service forks and the parent exits. systemd considers it started after forking.                | Daemons that fork (e.g., sshd)
oneshot | Runs a single command and stops. Optionally remains "active" after exit with RemainAfterExit=true. | Initialization tasks, scripts
notify  | The service notifies systemd when it's ready. Requires sd_notify support.                          | Complex or stateful services
dbus    | The service is ready when it registers a specified D-Bus name.                                     | D-Bus-integrated services
idle    | The service waits until no other jobs are starting, then runs.                                     | Tasks that can be deferred

```
# Enable the timer
sudoedit mytimer.timer
sudo systemctl daemon-reload
sudo systemctl enable mytimer.timer # Creates symlink to /etc/systemd/system/timers.target.wants/mytimer.timer
sudo systemctl start mytimer.timer
sudo systemctl list-timers --all
```

[Time format](https://www.freedesktop.org/software/systemd/man/latest/systemd.time.html#)

```sh
~/.config/systemd/user/ # User location
```

## Search Paths

```
System Unit Search Path

/etc/systemd/system.control/*
/run/systemd/system.control/*
/run/systemd/transient/*
/run/systemd/generator.early/*
/etc/systemd/system/*
/etc/systemd/system.attached/*
/run/systemd/system/*
/run/systemd/system.attached/*
/run/systemd/generator/*
…
/usr/local/lib/systemd/system/*
/usr/lib/systemd/system/*
/run/systemd/generator.late/*

User Unit Search Path

~/.config/systemd/user.control/*
$XDG_RUNTIME_DIR/systemd/user.control/*
$XDG_RUNTIME_DIR/systemd/transient/*
$XDG_RUNTIME_DIR/systemd/generator.early/*
~/.config/systemd/user/*
$XDG_CONFIG_DIRS/systemd/user/*
/etc/systemd/user/*
$XDG_RUNTIME_DIR/systemd/user/*
/run/systemd/user/*
$XDG_RUNTIME_DIR/systemd/generator/*
$XDG_DATA_HOME/systemd/user/*
$XDG_DATA_DIRS/systemd/user/*
…
/usr/local/lib/systemd/user/*
/usr/lib/systemd/user/*
$XDG_RUNTIME_DIR/systemd/generator.late/*
```
