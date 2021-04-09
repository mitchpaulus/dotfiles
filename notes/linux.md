# Linux

## Permissions

- Order is user, group, all others
- u: user who owns file, g: other users in group, o: all other users, a: all users ('ugo')

- In Octal = User, Group, All Others


## User Management

- Add user: `useradd`. However, this is a low-level utility, recommended
  replacement is `adduser`. [SO](https://unix.stackexchange.com/a/182193/296724). See `man useradd` as well.
- Add existing user account to group: `usermod -a -G groupname username`.
  `-a` is for append.
  `-G` is for secondary group.

- **May need to log out/log in to see changes**
- `tmux` may need to be restarted in order to see the changes as well

- View groups for current user: `groups`

## Passwords / View all users

- `[sudo] passwd user`: Update password. Stored in `/etc/passwd`
- `cat /etc/passwd` to see all available users on computer.

## Clipboard

3 clipboards: primary, secondary, and clipboard.

## Zip Files

```
zip zipfilename files...
fd | zip -@ zipfilename  # Using files from standard input, one per line.
unzip zipfilename -d extractDir  # Only one file can be processed at a time.
```


