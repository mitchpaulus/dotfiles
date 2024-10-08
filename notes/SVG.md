# SVG Minimum Requirements

```html
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">  </svg>
```

The viewBox attribute defines the position and dimension, in user space, of an SVG viewport.

```
viewBox="left top width height"
```

Basically make the viewBox to the same internal dimensions. The width/height on the svg tag is the final rendered size.

If aspect ratios do not align, then `preserveAspectRatio` option is important.

y alignment for text:

dominant-baseline = auto | text-bottom | alphabetic | ideographic | middle | central | mathematical | hanging | text-top

x alignment for text:

text-anchor = start | middle | end


## Rect

```
<rect x="10" y="10" width="100" height="100" fill="none" stroke="black" />
<text x="10" y="10">My text</text>
```

## Strokes

```
For circle, ellipse, line, path, polygon, polyline, rect, text, textPath, tref, tspan
```
