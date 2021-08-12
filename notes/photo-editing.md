# Photo Editing

## Rotating Photos

On Windows/WSL, typically rotate photo in the default Photos app. This
only changes the exif data.

Then use 'exiftran' and fd/find/parallel to mass rotate the actual photo.

```
fd -x exiftran -ai
```
