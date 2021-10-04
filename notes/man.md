# man

`man` searches for files using the contents of a file
`/etc/manpath.config`. This consists of hard coded absolute paths to a
few locations such as:

```
MANDATORY_MANPATH			/usr/man
MANDATORY_MANPATH			/usr/share/man
MANDATORY_MANPATH			/usr/local/share/man
```

Also, some mappings between binary locations and man locations.

```
MANPATH_MAP	/bin			/usr/share/man
MANPATH_MAP	/usr/bin		/usr/share/man
MANPATH_MAP	/sbin			/usr/share/man
MANPATH_MAP	/usr/sbin		/usr/share/man
MANPATH_MAP	/usr/local/bin		/usr/local/man
MANPATH_MAP	/usr/local/bin		/usr/local/share/man
MANPATH_MAP	/usr/local/sbin		/usr/local/man
MANPATH_MAP	/usr/local/sbin		/usr/local/share/man
MANPATH_MAP	/usr/X11R6/bin		/usr/X11R6/man
MANPATH_MAP	/usr/bin/X11		/usr/X11R6/man
MANPATH_MAP	/usr/games		/usr/share/man
MANPATH_MAP	/opt/bin		/opt/man
MANPATH_MAP	/opt/sbin		/opt/man
```
