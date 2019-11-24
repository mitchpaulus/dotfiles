# Manjaro - KDE Tower

2019-05-25: Played around with some font stuff. Looked at some of the
information in this post
[here](https://www.reddit.com/r/archlinux/comments/5r5ep8/make_your_arch_fonts_beautiful_easily/).

Only added two of the symlinks, the one for no bitmaps and the one for
lcdfilter

```
sudo ln -s /etc/fonts/conf.avail/70-no-bitmaps.conf /etc/fonts/conf.d
sudo ln -s /etc/fonts/conf.avail/10-sub-pixel-rgb.conf /etc/fonts/conf.d
sudo ln -s /etc/fonts/conf.avail/11-lcdfilter-default.conf /etc/fonts/conf.d
```
# Work Surface

Disabled the Microsoft Telemetry Compatibility. Went off this post and
disabled the scheduled tasks for:

`https://answers.microsoft.com/en-us/windows/forum/windows_10-performance/microsoft-telemetry-compatibility/cefa7c8e-49c9-4965-aef6-2d5f01bb38f2`

Microsoft Compatibility Appraiser
ProgramDataUpdater

2019-11-09:
When installing stack from the repository:
You need to either 1) install latest stable ghc package from [extra] or 2) install ncurses5-compat-libs from AUR for the prebuilt binaries installed by stack to work.

# General

If iCue software breaks for keyboard, follow steps at:
```
https://help.corsair.com/hc/en-us/articles/360025166712-Performing-a-Clean-Reinstallation-of-the-Corsair-Utility-Engine-iCUE-
```
This removes all remnants of a previous profile.

# Thinkpad

2019-10-12: Ran into issue with wifi-menu and netctl. Had to follow
instructions from
https://unix.stackexchange.com/questions/121060/arch-linux-not-connecting-to-wifi-anymore#121125

All I did was `killall dhcpcd` and then re-ran wifi menu. Have no idea
why that fixed anything.

The interface of network profile 'wlp3s0-MySpectrumWiFidf-2G' is already up
