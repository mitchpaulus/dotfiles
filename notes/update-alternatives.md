On Debian based systems, there is the concept of "alternatives".
You can use the `update-alternatives` command to make changes to the list.

These alternatives are what is used for things like `sudoedit`. 

## Setting Editor for `sudo -e` or `sudoedit`

I like to set `SUDO_EDITOR` environment variable. Note that this appears to require a full path.
So in my fish config, I have to do something like:

```
set -gx SUDO_EDITOR (which nvim)
```
