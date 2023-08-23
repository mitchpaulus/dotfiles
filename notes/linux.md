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

## Ports

```
lsof -i :8081
```

## Utility Conventions

<https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html>


Guideline 1:
    Utility names should be between two and nine characters, inclusive.
Guideline 2:
    Utility names should include lowercase letters (the lower character classification) and digits only from the portable character set.
Guideline 3:
    Each option name should be a single alphanumeric character (the alnum character classification) from the portable character set.
    The -W (capital-W) option shall be reserved for vendor options.
    Multi-digit options should not be allowed.
Guideline 4:
    All options should be preceded by the '-' delimiter character.
Guideline 5:
    One or more options without option-arguments, followed by at most one option that takes an option-argument,
    should be accepted when grouped behind one '-' delimiter.
Guideline 6:
    Each option and option-argument should be a separate argument, except as noted in Utility Argument Syntax, item (2).
Guideline 7:
    Option-arguments should not be optional.
Guideline 8:
    When multiple option-arguments are specified to follow a single option, they should be presented as a single argument, using <comma> characters within that argument or <blank> characters within that argument to separate them.
Guideline 9:
    All options should precede operands on the command line.
Guideline 10:
    The first -- argument that is not an option-argument should be accepted as a delimiter indicating the end of options. Any following arguments should be treated as operands, even if they begin with the '-' character.
Guideline 11:
    The order of different options relative to one another should not matter, unless the options are documented as mutually-exclusive and such an option is documented to override any incompatible options preceding it. If an option that has option-arguments is repeated, the option and option-argument combinations should be interpreted in the order specified on the command line.
Guideline 12:
    The order of operands may matter and position-related interpretations should be determined on a utility-specific basis.
Guideline 13:
    For utilities that use operands to represent files to be opened for either reading or writing, the '-' operand should be used to mean only standard input (or standard output when it is clear from context that an output file is being specified) or a file named -.
Guideline 14:
    If an argument can be identified according to Guidelines 3 through 10 as an option, or as a group of options without option-arguments behind one '-' delimiter, then it should be treated as such.
