from typing import Callable, Optional, Union, Any
import uuid

# General iterface convention:
# - Shapes should have a to_vba() and to_svg() method
# - Shapes should have a min_x and min_y method to get the minimum x and y coordinate

# Type alias for float | Callable[[], float]
Coord = float | Callable[[], float]

def compute(x):
    if callable(x):
        return x()
    else:
        return x


class Drawing:
    def __init__(self) -> None:
        self._shapes = {}

    def rect(self, name: Optional[str] = None) -> 'Rectangle':
        if name is None:
            name = f"rect{len(self._shapes)}"

        if name in self._shapes:
            raise KeyError(f"Shape with name {name} already exists")

        self._shapes[name] = Rectangle(name)
        return self._shapes[name]

    def line(self, name: Optional[str] = None) -> 'Line':
        if name is None:
            name = f"line{len(self._shapes)}"

        if name in self._shapes:
            raise KeyError(f"Shape with name {name} already exists")

        self._shapes[name] = Line(name)
        return self._shapes[name]

    def text(self, name: Optional[str] = None) -> 'Text':
        if name is None:
            name = f"text{len(self._shapes)}"

        if name in self._shapes:
            raise KeyError(f"Shape with name {name} already exists")

        self._shapes[name] = Text(name)
        return self._shapes[name]

    def circle(self, name: Optional[str] = None) -> 'Circle':
        if name is None:
            name = f"circle{len(self._shapes)}"

        if name in self._shapes:
            raise KeyError(f"Shape with name {name} already exists")

        self._shapes[name] = Circle(name)
        return self._shapes[name]


    def to_svg(self, min_x: float, min_y: float, width: float, height: float):
        print(f'<svg viewBox="{min_x} {min_y} {width} {height}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">\n', end='')
        for i in self._shapes:
            shape = self._shapes[i]
            print(shape.to_svg(), end="")
        print('</svg>')


# Use fluent syntax
class Rectangle:
    def __init__(self, name):
        self._x: Coord = 0.0
        self._y: Coord = 0.0
        self._width: Coord = 1
        self._height: Coord = 1
        self._name = name
        self._text = None
        self._font_size = None

        self._fill: Optional[tuple[int, int, int]] = None

    def x(self, x = None) -> Any:
        if x is None:
            return self._x

        self._x = x
        return self

    def y(self, y = None) -> Any:
        if y is None:
            return self._y
        self._y = y
        return self

    def text(self, text: str) -> 'Rectangle':
        """This is a text element that is tied to the center of the rectangle."""
        self._text = Text(uuid.uuid4().hex).text(text).x(self.center_x()).y(self.center_y()).xAnchor("middle").yAnchor("middle")
        return self

    def font_size(self, font_size: float) -> 'Rectangle':
        self._font_size = font_size
        return self

    def x2(self) -> Coord:
        return lambda: compute(self._x) + compute(self._width)

    def y2(self) -> Coord:
        return lambda: compute(self._y) + compute(self._height)

    def center_x(self):
        return lambda: compute(self._x) + compute(self._width) / 2

    def center_y(self):
        return lambda:compute(self._y) + compute(self._height) / 2

    def width(self, width: Coord) -> 'Rectangle':
        self._width = width
        return self

    def height(self, height: Coord) -> 'Rectangle':
        self._height = height
        return self

    def name(self, name: str) -> 'Rectangle':
        self._name = name
        return self

    def no_fill(self) -> 'Rectangle':
        self._fill = None
        return self

    def fill(self, r: int, g: int, b: int) -> 'Rectangle':
        # Validate the RGB values
        if r < 0 or r > 255:
            raise ValueError(f"Red value {r} is not in the range 0-255")
        if g < 0 or g > 255:
            raise ValueError(f"Green value {g} is not in the range 0-255")
        if b < 0 or b > 255:
            raise ValueError(f"Blue value {b} is not in the range 0-255")
        self._fill = (r, g, b)
        return self

    def to_vba(self):
        vba = f"Set newShape = ActiveSheet.Shapes.AddShape(msoShapeRectangle, {compute(self._x)}, {compute(self._y)}, {compute(self._width)}, {compute(self._height)})\n"
        if self._fill:
            vba += f"newShape.Fill.ForeColor.RGB = RGB({self._fill[0]}, {self._fill[1]}, {self._fill[2]})\n"
        else:
            vba += f"newShape.Fill.Visible = msoFalse\n"

        vba += f"newShape.Name = \"{self._name}\"\n"

        return vba

    def to_svg(self):
        x = compute(self._x)
        # The y-origin is at the top in SVG instead of bottom, so we need to subtract the height
        y = -compute(self._y) - compute(self._height)
        width = compute(self._width)
        height = compute(self._height)

        if self._fill:
            fill_str = f'fill="rgb{self._fill}"'
        else:
            fill_str = 'fill="none"'

        rect_tag = f'<rect stroke="black" stroke-width="0.1" x="{x}" y="{y}" width="{width}" height="{height}" {fill_str} />\n'

        if self._text:
            if self._font_size:
                self._text.font_size(self._font_size)
            rect_tag += self._text.to_svg()

        return rect_tag

    def right_of(self, other, distance = 72) -> 'Rectangle':
        self._x = lambda: compute(other._x) + compute(other._width) + distance
        self._y = lambda: compute(other.center_y()) - compute(self._height) / 2
        return self

    def below(self, other, distance = 72) -> 'Rectangle':
        self._x = lambda: compute(other.center_x()) - compute(self._width) / 2
        self._y = lambda: compute(other._y) + compute(other._height) + distance
        return self

    def left_of(self, other, distance = 72) -> 'Rectangle':
        self._x = lambda: compute(other._x) - compute(self._width) - distance
        self._y = lambda: compute(other.center_y()) - compute(self._height) / 2
        return self

    def above(self, other, distance = 72) -> 'Rectangle':
        self._x = lambda: compute(other.center_x()) - compute(self._width) / 2
        self._y = lambda: compute(other._y) - compute(self._height) - distance
        return self

    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'

class Line:
    def __init__(self, name):
        self._x1: Coord = 0.0
        self._y1: Coord = 0.0
        self._x2: Coord = 1
        self._y2: Coord = 1
        self._name = name

    def x1(self, x1: Coord) -> 'Line':
        self._x1 = x1
        return self

    def y1(self, y1: Coord) -> 'Line':
        self._y1 = y1
        return self

    def x2(self, x2: Coord) -> 'Line':
        self._x2 = x2
        return self

    def y2(self, y2: Coord) -> 'Line':
        self._y2 = y2
        return self

    def to_vba(self):
        vba = f"ActiveSheet.Shapes.AddShape(msoShapeLine, {compute(self._x1)}, {compute(self._y1)}, {compute(self._x2)}, {compute(self._y2)})\n"
        return vba

    def to_svg(self):
        return f'<line x1 = "{compute(self._x1)}" y1 = "{compute(self._y1)}" x2 = "{compute(self._x2)}" y2 = "{compute(self._y2)}" />\n'

    def __str__(self):
        return f'Line({self.x1}, {self.y1}, {self.x2}, {self.y2})'


class Text:
    def __init__(self, name) -> None:
        self._x = 0
        self._y = 0
        self._text = "Text"
        self._name = name
        self._font_size = None
        self._xAnchor = "start"
        self._yAnchor = "auto"
        self._font_family = "sans-serif"

    def x(self, x: Coord) -> 'Text':
        self._x = x
        return self

    def y(self, y: Coord) -> 'Text':
        self._y = y
        return self

    def text(self, text = None) -> Any:
        if text is None:
            return self._text

        self._text = text
        return self

    def font_size(self, font_size: float) -> 'Text':
        self._font_size = font_size
        return self

    def xAnchor(self, xAnchor: str) -> 'Text':
        self._xAnchor = xAnchor
        return self

    def yAnchor(self, yAnchor: str) -> 'Text':
        self._yAnchor = yAnchor
        return self

    def to_vba(self):
        vba = f"ActiveSheet.Shapes.AddTextbox(msoTextOrientationHorizontal, {compute(self._x)}, {compute(self._y)}, 100, 50).TextFrame.Characters.Text = \"{self._text}\"\n"
        return vba

    def to_svg(self):
        x = compute(self._x)
        y = -compute(self._y)
        font_size = self._font_size or 12
        xAnchor = self._xAnchor
        dominant_baseline = self._yAnchor
        return f'<text font-family="{self._font_family}" x="{x}" y="{y}" font-size="{font_size}" text-anchor="{xAnchor}" dominant-baseline="{dominant_baseline}">{self._text}</text>\n'


class Circle:
    def __init__(self, name) -> None:
        self._x = 0
        self._y = 0
        self._r = 10
        self._name = name

    def x(self, x: Coord) -> 'Circle':
        self._x = x
        return self

    def y(self, y: Coord) -> 'Circle':
        self._y = y
        return self

    def r(self, r: Coord) -> 'Circle':
        self._r = r
        return self

    def to_vba(self):
        vba = f"ActiveSheet.Shapes.AddShape(msoShapeOval, {compute(self._x)}, {compute(self._y)}, {compute(self._r)}, {compute(self._r)})\n"
        return vba

    def to_svg(self):
        x = compute(self._x)
        y = -compute(self._y)
        r = compute(self._r)
        return f'<circle cx="{x}" cy="{y}" r="{r}" />\n'


class Sensor:
    def __init__(self, name) -> None:
        # Here x and y are the point of the sensor
        self._x = 0
        self._y = 0

        self._text = "T"

        self._name = name

    def x(self, x: Coord) -> 'Sensor':
        self._x = x
        return self

    def y(self, y: Coord) -> 'Sensor':
        self._y = y
        return self

    def width(self, width: Coord) -> 'Sensor':
        self._width = width
        return self

    def height(self, height: Coord) -> 'Sensor':
        self._height = height
        return self

    def text(self, text: str) -> 'Sensor':
        self._text = text
        return self

    def to_vba(self):
        # Make a cirle on top of a line, then group
        vba = f"Set newCircle = ActiveSheet.Shapes.AddShape(msoShapeOval, {compute(self._x)}, {compute(self._y) + 20}, 20, 20)\n"
        # Set no fill
        vba += f"newCircle.Fill.Visible = msoFalse\n"
        # Set the text
        vba += f"newCircle.TextFrame.Characters.Text = \"{self._text}\"\n"
