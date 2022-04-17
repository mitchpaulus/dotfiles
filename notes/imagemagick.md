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

