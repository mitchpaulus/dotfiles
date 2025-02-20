# Cron Alternative

[Directives](https://www.freedesktop.org/software/systemd/man/latest/systemd.directives.html)

<https://www.freedesktop.org/software/systemd/man/latest/systemd.syntax.html#>

```
# /etc/systemd/system/myservice.service
# Service Unit File
[Unit]
Description=My Service

[Service]
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
