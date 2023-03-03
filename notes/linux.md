# Linux

## References

- <https://explainshell.com/>: Helps explain shell syntax you might come across

## Permissions

- Order is user, group, all others
- u: user who owns file, g: other users in group, o: all other users, a: all users ('ugo')

- In Octal = Special permissions User, Group, All Others
- General default permissions, directory: 755, file: 644.
  This comes from typical `umask` of 0022.
- Special permission go in order:
    - Set UID (+4)
    - Set GID (+2)
    - Set Sticky Bit (only matters for directories)

[Useful Stack Overflow](https://askubuntu.com/a/581295)

### Directory Permissions

[From Stack](https://unix.stackexchange.com/a/18098/296724)

The execute permission on directories allows accessing files inside the
directory. The read permission allows enumerating the directory entries.
The write permission allows creating and removing entries in it.

Having read or write permission on a directory without execute
permission is not useful. Having execute but not read permission is
occasionally useful: it allows accessing files only if you know their
exact name, a sort of primitive password protection.

So in practice the useful permissions on a directory are:

    ---: no access
    --x: can access files whose name is known (occasionally useful)
    r-x: normal read-only access
    rwx: normal read and write access


- [Permissions for git directory](https://serverfault.com/a/27040)

```
setfacl -R -m g:<whatever group>:rwX gitrepo
find gitrepo -type d | xargs setfacl -R -m d:g:<whatever group>:rwX
```

ACL = Access Control List


## User Management

- Add user: `useradd`. However, this is a low-level utility, recommended
  replacement is `adduser`. [SO](https://unix.stackexchange.com/a/182193/296724). See `man useradd` as well.
- Config file for `adduser` is at: `/etc/adduser.conf`
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

## API/ABI

[From SO](https://stackoverflow.com/a/41402442/5932184)

> An oversimplified summary:
>   API: "Here are all the functions you may call."
>   ABI: "This is *how* to call a function."

## Where to put Program Files?

[From here](https://askubuntu.com/a/551932), looks like `opt` is the
best place for program files, then symlink the binaries to ~/.local/bin
or equivalent.


## Changing Default Shell

```
sudo chsh -s /usr/bin/fish mp
```

## System Calls

```c
fd = int open(const char *pathname, int flags);
// fd usually small positive integer
// -1 for error, check `errno` to get description

#include <unistd.h>
ssize_t read(int fd, void *buf, size_t count);
```

## UIDs, GIDs

All users have a UID, stored in `/etc/passwd`. Each user must belong to a minimum of one group.
A user also has a *primary* associated group. Group information is in `/etc/group`
