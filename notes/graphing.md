coordinates:

Typically have separate x and y versions of each.
data -> chart -> figure -> print

# Typical linear scaling

Data -> Chart

x: (x min, 0) -> (x max, 1)
y: (y min, 0) -> (y max, 1)

Chart -> Figure

x: (0, left margin: 0.2)  -> (1, right margin: 0.95)
y: (0, bottom margin: 0.2)  -> (1, top margin: 0.95)

Figure -> Print

For SVG with y going down.

x: (0, 0) -> (1, fig width)
y: (1, 0) -> (0, fig height)
