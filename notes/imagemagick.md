# Imagemagick

PDF to PNG

magick -density <desired ppi> -units PixelsPerInch <FileName> -resize <number of pixels> <Converted File Name>

magick -density 1000 -units PixelsPerInch Diagram.pdf -resize 5000 Diagram2.png

results in a 5 inch width figure.

## Trimming

`-trim` option. The order on the command line matters. For example:

```
convert -density 1000 -units PixelsPerInch my_example.pdf -trim -resize 6000  my_example.png
```

is different than

```
convert -density 1000 -units PixelsPerInch my_example.pdf -resize 6000  -trim my_example.png
```

The first one will have the desired width. The second one resizes to the
right width, then crops that image, making the final image smaller than
desired.

## Permissions

When dealing with PDF conversions, always need to update the policy file.
Go to `/etc/ImageMagick-6/policy.xml` and update the policies at the end of the file.
Will usually have a comment above saying 'disable ghostscript format types'

```
-units Undefined, PixelsPerInch, PixelsPerCentimeter # Only makes sense with -density
```

## Concatenating Images

```
magick file1.png file2.png file3.png -append output.png
```
