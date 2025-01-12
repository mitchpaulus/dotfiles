# Fonts

## Favorite Mono Fonts

- Fira Code Mono
- [Ioveska](https://github.com/be5invis/Iosevka)
- Inconsolata
- JetBrains Mono


## Installing

Ubuntu (among others) [link](https://www.atechtown.com/install-fonts-in-ubuntu/):

Copy to folder:
 - Installing for single user, `~/.fonts`
 - All Users: `/usr/local/share/fonts` or `/usr/share/fonts/`

Refresh font cache:

```
sudo fc-cache
```

## X bitmap fonts

- On Arch, package is 'xorg-fonts-misc'

## Listing Fonts

```sh
fc-list
```

## Add font to Latex

```
mktextfm 'fontfile' # Maybe?
```

## TTF and OTF

References:
- <https://www.makeuseof.com/tag/otf-vs-ttf-fonts-one-better/>

TTF (TrueType Font): Apple and Microsoft, late 1980's. Contains screen and printer data.
OTF (OpenType Font): Adobe and Microsoft, somewhat based on TTF.

OTF allows for more features.
Ligatures and alternate characters can be defined in the single file,
vs. TTF which may have had to be additional files.

## Iosevka not showing in KDE/Konsole

[Fontconfig is too strict](https://github.com/be5invis/Iosevka/issues/2101)
