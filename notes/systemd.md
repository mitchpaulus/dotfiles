# Cron Alternative

<https://www.freedesktop.org/software/systemd/man/latest/systemd.syntax.html#>

```
/etc/systemd/system

# Service Unit File
[Unit]
Description=My Service

[Service]
ExecStart=/path/to/script.sh
Type=oneshot

```

```
systemctl list-timers --all
```

Type    | Description                                                                                        | Use Case
--------|----------------------------------------------------------------------------------------------------|---------------------------------------------------
simple  | The default; the service starts immediately.                                                       | Most services that don’t fork or run in background
forking | The service forks and the parent exits. systemd considers it started after forking.                | Daemons that fork (e.g., sshd)
oneshot | Runs a single command and stops. Optionally remains "active" after exit with RemainAfterExit=true. | Initialization tasks, scripts
notify  | The service notifies systemd when it's ready. Requires sd_notify support.                          | Complex or stateful services
dbus    | The service is ready when it registers a specified D-Bus name.                                     | D-Bus-integrated services
idle    | The service waits until no other jobs are starting, then runs.                                     | Tasks that can be deferred
