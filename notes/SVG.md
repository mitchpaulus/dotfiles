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

```
text-anchor = start | middle | end # x-align
```


## Rect

```
<rect x="10" y="10" width="100" height="100" fill="none" stroke="black" />
<text x="10" y="10">My text</text>
```

## Strokes

```
For circle, ellipse, line, path, polygon, polyline, rect, text, textPath, tref, tspan
```

## Circle




```
# Color grammar
color    ::= "#" hexdigit hexdigit hexdigit (hexdigit hexdigit hexdigit)?
              | "rgb("integer integer integer")"
              | "rgb("integer "%" integer "%" integer "%)"
              | color-keyword
hexdigit ::= [0-9A-Fa-f]

Commas are now optional.

color := #AB09C2 | rgb(10, 20, 30) | rgb(10%, 20%, 30%) | color-keyword
```

## `rsvg-convert`

Notes from working with it:

- `<image>` elements need to have a `href` that is `file://abs/path/to/file.png`.
- `<image>` elements need to have both `width` and `height` attributes.
