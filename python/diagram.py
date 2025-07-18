from typing import Callable, Optional, Union
import uuid
import sys

# General interface convention:
# - Shapes should have a to_vba() and to_svg() method, and to_vba_pp(slide_height_pts, scale_factor) method
# - Shapes should have a min_x and min_y method to get the minimum x and y coordinate

# Type alias for float | Callable[[], float]

# Everything here has the positive y-axis going up


Value = float | Callable[[], float]

def compute(x) -> float:
    if callable(x):
        return x()
    else:
        return x


class Drawing:
    def __init__(self, name = None) -> None:
        self._shapes = {}
        self._default_font_size = 12
        self._pp_slide_height = int(7.5 * 72) # 540 points
        self._pp_scale_factor = 1 # Scale factor of pts / input unit
        self._default_stroke_width = 1
        self._name = name if name else f"drawing{uuid.uuid4().hex}"

    def pp_scale_factor(self, scale_factor: float) -> 'Drawing':
        self._pp_scale_factor = scale_factor
        return self

    def rect(self, name: Optional[str] = None) -> 'Rectangle':
        if name is None:
            name = f"rect{len(self._shapes)}"

        if name in self._shapes:
            raise KeyError(f"Shape with name {name} already exists")

        self._shapes[name] = Rectangle(name)
        self._shapes[name]._drawing = self
        return self._shapes[name]

    def line(self, name: Optional[str] = None) -> 'Line':
        if name is None:
            name = f"line{len(self._shapes)}"

        if name in self._shapes:
            raise KeyError(f"Shape with name {name} already exists")

        self._shapes[name] = Line(name)
        self._shapes[name]._drawing = self
        return self._shapes[name]

    def text(self, name: Optional[str] = None, text: Optional[str] = None) -> 'Text':
        if name is None:
            name = f"text{len(self._shapes)}"

        if name in self._shapes:
            raise KeyError(f"Shape with name {name} already exists")

        self._shapes[name] = Text(name, text, self._default_font_size)
        return self._shapes[name]

    def circle(self, name: Optional[str] = None) -> 'Circle':
        if name is None:
            name = f"circle{len(self._shapes)}"

        if name in self._shapes:
            raise KeyError(f"Shape with name {name} already exists")

        self._shapes[name] = Circle(name)
        return self._shapes[name]

    def default_font_size(self, font_size: float) -> 'Drawing':
        self._default_font_size = font_size
        return self

    def default_stroke_width(self, stroke_width: float) -> 'Drawing':
        self._default_stroke_width = stroke_width
        return self

    def to_svg(self, min_x: float, min_y: float, width: float, height: float):
        lines = []

        lines.append(f'<svg viewBox="{min_x} {min_y} {width} {height}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="stroke-width: {self._default_stroke_width}">\n')
        for i in self._shapes:
            shape = self._shapes[i]
            lines.append(shape.to_svg())
        lines.append('</svg>')

        return "".join(lines)

        #  print(f'<svg viewBox="{min_x} {min_y} {width} {height}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">\n', end='')
        #  for i in self._shapes:
            #  shape = self._shapes[i]
            #  print(shape.to_svg(), end="")
        #  print('</svg>')

    def to_vba(self):
        lines = []
        for i in self._shapes:
            shape = self._shapes[i]
            lines.append(shape.to_vba())
        return "".join(lines)

    def to_vba_pp(self):
        lines = []
        for i in self._shapes:
            shape = self._shapes[i]
            # Check if to_vba_pp exists, otherwise use to_vba
            if hasattr(shape, 'to_vba_pp'):
                lines.append(shape.to_vba_pp(self._pp_slide_height, self._pp_scale_factor))
            else:
                lines.append(shape.to_vba())
        return "".join(lines)

    def merge(self, other: 'Drawing') -> 'Drawing':
        """Merge another drawing into this one."""
        for name, shape in other._shapes.items():
            if name in self._shapes:
                # Try with drawing name prefixed
                name = f"{other._name}_{name}"
            if name in self._shapes:
                raise KeyError(f"Shape with name {name} already exists in drawing")

            self._shapes[name] = shape
        return self

    def shift_x(self, dx: float) -> 'Drawing':
        """Shift all shapes in the drawing by dx."""
        for shape in self._shapes.values():
            if hasattr(shape, 'shift_x'):
                shape.shift_x(dx)
            else:
                raise NotImplementedError(f"Shape {shape} does not support shifting in x direction")
        return self

    def shift_y(self, dy: float) -> 'Drawing':
        """Shift all shapes in the drawing by dy."""
        for shape in self._shapes.values():
            if hasattr(shape, 'shift_y'):
                shape.shift_y(dy)
            else:
                raise NotImplementedError(f"Shape {shape} does not support shifting in y direction")
        return self

# Use fluent syntax
class Rectangle:
    def __init__(self, name):
        self._x: float = 0.0
        self._y: float = 0.0
        self._width: float = 1
        self._height: float = 1
        self._name = name
        self._text = None
        self._font_size = None
        self._stroke_width = 1
        self._drawing: Optional[Drawing] = None

        self._fill: Optional[tuple[int, int, int]] = None

    def dup(self, name: Optional[str] = None) -> 'Rectangle':
        if name is None:
            name = f"rect{uuid.uuid4().hex}"

        if name in self._drawing._shapes:
            raise KeyError(f"Shape with name {name} already exists in drawing")

        new_rect = Rectangle(name)
        new_rect._x = self._x
        new_rect._y = self._y
        new_rect._width = self._width
        new_rect._height = self._height
        new_rect._text = self._text
        new_rect._font_size = self._font_size
        new_rect._stroke_width = self._stroke_width
        new_rect._fill = self._fill
        new_rect._drawing = self._drawing
        self._drawing._shapes[name] = new_rect

        return new_rect


    def x(self, x) -> 'Rectangle':
        """Bottom left x-coordinate of the rectangle"""
        self._x = x
        return self

    def y(self, y = None) -> 'Rectangle':
        """Bottom left y-coordinate of the rectangle"""
        self._y = y
        return self

    def stroke_width(self, stroke_width) -> 'Rectangle':
        self._stroke_width = stroke_width
        return self

    def text(self, text: str) -> 'Rectangle':
        """This is a text element that is tied to the center of the rectangle."""
        self._text = Text(uuid.uuid4().hex, text, self._font_size).x(self.center_x()).y(self.center_y()).xAnchor("middle").yAnchor("middle")
        return self

    def font_size(self, font_size: float) -> 'Rectangle':
        self._font_size = font_size
        return self

    def x2(self) -> Value:
        return lambda: compute(self._x) + compute(self._width)

    def y2(self) -> Value:
        return lambda: compute(self._y) + compute(self._height)

    def center_x(self):
        return lambda: compute(self._x) + compute(self._width) / 2

    def center_y(self):
        return lambda:compute(self._y) + compute(self._height) / 2

    def width(self, width: float) -> 'Rectangle':
        self._width = width
        return self

    def height(self, height: float) -> 'Rectangle':
        self._height = height
        return self

    def name(self, name: str) -> 'Rectangle':
        self._name = name
        return self

    def no_fill(self) -> 'Rectangle':
        self._fill = None
        return self

    def bottom(self):
        return self._y

    def top(self):
        return compute(self._y) + compute(self._height)

    def left(self):
        return self._x

    def right(self):
        return compute(self._x) + compute(self._width)

    def shift_x(self, dx: float) -> 'Rectangle':
        self._x = self._x + dx
        return self

    def shift_y(self, dy: float) -> 'Rectangle':
        self._y = self._y + dy
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

    def to_vba_pp(self, pp_slide_height_pts, scale_factor):
        #  y1 = compute(self._y)
        #  y1 = pp_slide_height_pts - y1
        top = self.top() * scale_factor
        top = pp_slide_height_pts - top
        x = compute(self._x) * scale_factor
        width = compute(self._width) * scale_factor
        height = compute(self._height) * scale_factor
        
        vba = f"Set newShape = currentSlide.Shapes.AddShape(msoShapeRectangle, {x}, {top}, {width}, {height})\n"
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

        rect_tag = f'<rect stroke="black" stroke-width="{compute(self._stroke_width)}" x="{x}" y="{y}" width="{width}" height="{height}" {fill_str} />\n'

        if self._text:
            if self._font_size:
                self._text.font_size(self._font_size)
            else:
                # Make it 75 percent of the height
                self._text.font_size(compute(self._height) * 0.75)

            rect_tag += self._text.to_svg()

        return rect_tag

    def right_of(self, other, distance = 0) -> 'Rectangle':
        self._x = compute(other._x) + compute(other._width) + distance
        self._y = compute(other.center_y()) - compute(self._height) / 2
        return self

    def below(self, other, distance = 72) -> 'Rectangle':
        self._x =  compute(other.center_x()) - compute(self._width) / 2
        self._y =  compute(other._y) + compute(other._height) + distance
        return self

    def left_of(self, other, distance = 72) -> 'Rectangle':
        self._x =  compute(other._x) - compute(self._width) - distance
        self._y =  compute(other.center_y()) - compute(self._height) / 2
        return self

    def above(self, other, distance = 72) -> 'Rectangle':
        self._x =  compute(other.center_x()) - compute(self._width) / 2
        self._y =  compute(other._y) - compute(self._height) - distance
        return self

    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'

class Line:
    def __init__(self, name):
        self._x1: Value = 0.0
        self._y1: Value = 0.0
        self._x2: Value = 1
        self._y2: Value = 1
        self._drawing: Optional[Drawing] = None
        self._name = name
        self._dash_pattern: Optional[str] = None

    def x1(self, x1: Value) -> 'Line':
        self._x1 = x1
        return self

    def y1(self, y1: Value) -> 'Line':
        self._y1 = y1
        return self

    def x2(self, x2: Value) -> 'Line':
        self._x2 = x2
        return self

    def y2(self, y2: Value) -> 'Line':
        self._y2 = y2
        return self

    def coords(self, x1: Value, y1: Value, x2: Value, y2: Value) -> 'Line':
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        return self

    def dup(self, name: Optional[str] = None) -> 'Line':
        if name is None and self._drawing is not None:
            name = f"line{len(self._drawing._shapes)}"
        elif name is None and self._drawing is None:
            name = f"line{uuid.uuid4().hex}"
        if self._drawing is not None and name in self._drawing._shapes:
            raise KeyError(f"Shape with name {name} already exists in drawing")

        new_line = Line(name)
        new_line._x1 = self._x1
        new_line._y1 = self._y1
        new_line._x2 = self._x2
        new_line._y2 = self._y2
        new_line._drawing = self._drawing
        self._drawing._shapes[name] = new_line

        return new_line

    def dash_pattern(self, pattern: str) -> 'Line':
        """Set the dash pattern for the line. Example: '5, 2' for a dashed line."""
        self._dash_pattern = pattern
        return self

    def to_vba(self):
        vba = f"ActiveSheet.Shapes.AddShape(msoShapeLine, {compute(self._x1)}, {compute(self._y1)}, {compute(self._x2)}, {compute(self._y2)})\n"
        return vba

    def to_vba_pp(self, pp_slide_height_pts, scale_factor):
        y1 = compute(self._y1)
        y2 = compute(self._y2)

        y1 = y1 * scale_factor
        y2 = y2 * scale_factor

        y1 = pp_slide_height_pts - y1
        y2 = pp_slide_height_pts - y2

        x1 = compute(self._x1) * scale_factor
        x2 = compute(self._x2) * scale_factor

        vba = f"Set line = currentSlide.Shapes.AddLine({x1}, {y1}, {x2}, {y2})\n"
        vba += f"line.Line.ForeColor.RGB = RGB(0, 0, 0)\n"
        return vba

    def shift_x(self, dx: float) -> 'Line':
        self._x1 = compute(self._x1) + dx
        self._x2 = compute(self._x2) + dx
        return self

    def shift_y(self, dy: float) -> 'Line':
        self._y1 = compute(self._y1) + dy
        self._y2 = compute(self._y2) + dy
        return self

    def set_x(self, x: float) -> 'Line':
        self._x1 = x
        self._x2 = x
        return self

    def set_y(self, y: float) -> 'Line':
        self._y1 = y
        self._y2 = y
        return self

    def to_svg(self):
        element = f'<line x1="{compute(self._x1)}" y1="{-compute(self._y1)}" x2="{compute(self._x2)}" y2="{-compute(self._y2)}" stroke="black"'
        if self._dash_pattern:
            element += f' stroke-dasharray="{self._dash_pattern}"'
        element += ' />\n'
        return element

    def __str__(self):
        return f'Line({self.x1}, {self.y1}, {self.x2}, {self.y2})'


class Text:
    def __init__(self, name, text, font_size) -> None:
        self._x: float = 0
        self._y: float = 0
        self._text = text
        self._name = name
        self._font_size = font_size
        self._xAnchor = "start"
        self._yAnchor = "auto"
        self._font_family = "sans-serif"

    def x(self, x: float) -> 'Text':
        self._x = x
        return self

    def y(self, y: float) -> 'Text':
        self._y = y
        return self

    def shift_x(self, dx: float) -> 'Text':
        self._x = self._x + dx
        return self

    def shift_y(self, dy: float) -> 'Text':
        self._y = self._y + dy
        return self


    def text(self, text = None) -> 'Text':
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

    def to_vba_pp(self, pp_slide_height_pts, scale_factor):
        x = compute(self._x) * scale_factor

        y = compute(self._y) * scale_factor
        y = pp_slide_height_pts - y

        vba = f"Set newShape = currentSlide.Shapes.AddTextbox(msoTextOrientationHorizontal, {x}, {y}, 1, 1)\n"
        vba += "newShape.TextFrame.AutoSize = ppAutoSizeShapeToFitText\n"
        vba += f"newShape.TextFrame.TextRange.Font.Size = {self._font_size}\n"
        # Set all margins to 0
        vba += "newShape.TextFrame.MarginLeft = 0\n"
        vba += "newShape.TextFrame.MarginRight = 0\n"
        vba += "newShape.TextFrame.MarginTop = 0\n"
        vba += "newShape.TextFrame.MarginBottom = 0\n"
        vba += f"newShape.TextFrame.TextRange.Text = \"{self._text}\"\n"
        # Add name
        vba += f"newShape.Name = \"{self._name}\"\n"

        if self._xAnchor == "middle":
            vba += "newShape.TextFrame.TextRange.ParagraphFormat.Alignment = ppAlignCenter\n"
        elif self._xAnchor == "end":
            vba += "newShape.TextFrame.TextRange.ParagraphFormat.Alignment = ppAlignRight\n"

        if self._yAnchor == "middle":
            vba += "newShape.TextFrame.VerticalAnchor = msoAnchorMiddle\n"

        if self._font_family:
            vba += f"newShape.TextFrame.TextRange.Font.Name = \"{self._font_family}\"\n"

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

    def x(self, x: Value) -> 'Circle':
        self._x = x
        return self

    def y(self, y: Value) -> 'Circle':
        self._y = y
        return self

    def r(self, r: Value) -> 'Circle':
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

    def x(self, x: Value) -> 'Sensor':
        self._x = x
        return self

    def y(self, y: Value) -> 'Sensor':
        self._y = y
        return self

    def width(self, width: Value) -> 'Sensor':
        self._width = width
        return self

    def height(self, height: Value) -> 'Sensor':
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
