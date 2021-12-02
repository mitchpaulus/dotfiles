# Exif Data

[Link to standard?](https://www.cipa.jp/std/documents/e/DC-X008-Translation-2019-E.pdf)

## Tags

`DateTimeOriginal`: This seems to a be good one to set to mark when the
photo was taken. Has the exact form:

YYYY:MM:DD HH:MM:SS

Believe that this should be in the local time of location that the photo
was taken in.

Based on this [Stack Overflow
answer](https://photo.stackexchange.com/a/69193), `DateTimeOriginal` is
the tag that Windows gives the highest priority to.

## Exiftool

- Package on Arch/Manjaro is: perl-image-exiftool.
- It's written in Perl.
