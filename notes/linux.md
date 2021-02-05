# Linux

## Permissions

- Order is user, group, all others
- u: user who owns file, g: other users in group, o: all other users, a: all users ('ugo')

- In Octal = User, Group, All Others


## User Management

- Add user: `useradd`
- Add existing user account to group: `usermod -a -G groupname username`.
  `-a` is for append.
  `-G` is for secondary group.

- May need to log out/log in to see changes
- `tmux` may need to be restarted in order to see the changes as well


## Clipboard

3 clipboards: primary, secondary, and clipboard.
