Searches `packpath`, which is normally the same as `rtp` by default.

Good locations:

```
~/.config/nvim
~/.local/share/nvim/site
```

Then put plugins in structure like:

```
~/.config/nvim/pack/PACKAGE/start/PLUGIN/<vim plugin dirs like 'plugin', 'syntax' etc.
```

If you don't want it to load all on startup, put it in `opt` instead of `start`.
