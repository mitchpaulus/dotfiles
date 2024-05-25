This is knowledge that I've gained while debugging i3 keybindings.

First, the output from `showkeys -scancodes` in a console and `xev` will be different.
The X server will take raw scancodes and do things to them.
Like [this][1] says "It adds 8 to the keycode before passing it on."

I was trying debug a keybinding that already was bound (I didn't know it at the time).
In that case, `xev` will not show the keypress, it shows `FocusIn` and `FocusOut` events.

If it actually goes through, the `keycode` on line 3 is what you'd want for i3.

```
KeyPress event, serial 28, synthetic NO, window 0xa00001,
    root 0x460, subw 0x0, time 29275433, (491,680), root:(1453,682),
    state 0x10, keycode 122 (keysym 0x1008ff11, XF86AudioLowerVolume), same_screen YES,
    XLookupString gives 0 bytes:
    XmbLookupString gives 0 bytes:
    XFilterEvent returns: False
```

Also, for `xev`, will normally want to use the `-event keyboard` option to see the keypresses only.

To see the mapping between X keycodes and keysyms, you can use `xmodmap -pke`.

## References

- <https://unix.stackexchange.com/questions/382842/how-to-find-the-raw-keycodes-for-xkb>
[1]: https://unix.stackexchange.com/questions/49650/how-to-get-keycodes-for-xmodmap
