# gnuplot

Example Histogram:

```gnuplot
set terminal pngcairo size 960,720 font "Segoe UI,10" fontscale 1.600
set boxwidth 0.1
set xlabel "Flr00C_OAFan_Pres.SpcLby.1 [in. H₂O]" noenhanced
set ylabel "Percent" noenhanced
set output "965155e0-7a6d-4286-b852-794c5da309ff.png"
set xrange [*:*]
set title "3-20 to 4-17-21"
set grid
set style fill solid border -1 # This is black border line around the edges of the boxes
plot "965155e0-7a6d-4286-b852-794c5da309ff.dat" using 1:2 with boxes notitle lc rgb "#004B87"

```

## Plotting

```gnuplot
plot {<ranges>} <plot-element> {, <plot-element>, <plot-element>}
```

```gnuplot
plot-element:
{<iteration>}
(
  <definition> |
  {sampling-range} <function> |
  <data source> |
  keyentry {axes <axes>}
)
{<title-spec>}
{with <style options>}
```

```
<title-spec> : notitle | title "string"
```

Functions
```
[0:10] x * 10 + 2
```

```
<data source>: <source>
  {binary <binary list>}
  {{nonuniform} matrix}
  {index <index list> | index "<name>"}
  {every <every list>}
  {skip <number-of-lines>}
  {using <using list>}
  {smooth <option>}
  {bins <options>}
  {volatile} {noautoscale}
```

```
<using list>:
   <entry> {:<entry> {:<entry> ...}} {’format’}
```

- Skipping header line: <https://jchain.github.io/gnuplot-how-to-skip-the-first-line-in-the-data-file.html>
  - `plot "foo.dat" every ::1 using 1:2 with lines`
  - Simpler: `plot 'file.txt'` skip 1

### `with styling`

```
with <plot-style> {
  { (linestyle | ls) <line_style> }
  | {
    {linetype  | lt <line_type>}
    {linewidth | lw <line_width>}
    {linecolor | lc <colorspec>}
    {pointtype | pt <point_type>}
    {pointsize | ps <point_size>}
    {fill | fs <fillstyle>}
    {fillcolor | fc <colorspec>}
    {nohidden3d}
    {nocontours}
    {nosurface}
    {palette}
    }*
}

<plot-style> :
  boxerrorbars |
  boxes        | (Histogram)
  boxplot      | (Box and whisker)
  boxxyerror   |
  candlesticks |
  circles      |
  ellipses     |
  dots         | (Tiny dots, useful for when there are many points)
  filledcurves |
  financebars  |
  fsteps       |
  histeps      |
  histograms   |
  image        |
  impulses     |
  labels       |
  lines        | (normal line plot)
  linespoints  |
  parallelaxes |
  points       | (normal scatter plot)
  steps        |
  rgbalpha     |
  rgbimage     |
  vectors      | (Vector plots)
  xerrorbars   |
  xyerrorbars  |
  yerrorbars   |
  xerrorlines  |
  xyerrorlines |
  yerrorlines  |
  zerrorfill
```

## Colorspec

```
rgbcolor "colorname"   # e.g. "blue", can find available using 'show colornames'
rgbcolor "0xRRGGBB"    # string containing hexadecimal constant
rgbcolor "0xAARRGGBB"  # string containing hexadecimal constant
rgbcolor "#RRGGBB"    # string containing hexadecimal in x11 format
rgbcolor "#AARRGGBB"  # string containing hexadecimal in x11 format
rgbcolor <integer val> # integer value representing AARRGGBB
rgbcolor variable      # integer value is read from input file
palette frac <val>     # <val> runs from 0 to 1
palette cb <value>     # <val> lies within cbrange
palette z
variable               # color index is read from input file
bgnd                   # background color
black
```

## Tics

```
set xtics
    {axis | border}
    {{no}mirror}
    {in | out}
    {scale {default | <major> {,<minor>}}}
    {{no}rotate {by <ang>}}
    { offset <offset> | nooffset }
    { left | right | center | autojustify }
    {add}
    {  autofreq |
       <incr>   |
       <start>, <incr> {,<end>} |
       ({"<label>"} <pos> {<level>} {,{"<label>"}...})
   }
   {format "formatstring"}
   {font "name{,<size>}"}
   {{no}enhanced}
   { numeric | timedate | geographic }
   {{no}logscale}
   { rangelimited }
   { textcolor <colorspec> }
```

```
set xtics ("10,000 10000, "20,000" 20000, "30,000" 30000)
set xtics 1,2,10
```


## Key/Legend

```
set key
    {on|off}
    {default}
    {
        {inside | outside | fixed} |
        {lmargin | rmargin | tmargin | bmargin} |
        {at <position>}
    }
    {left | right | center}
    {top | bottom | center}
    {vertical | horizontal}
    {Left | Right}
    {{no}enhanced}
    {{no}opaque}
    {{no}reverse}
    {{no}invert}
    {samplen <sample_length>}
    {spacing <line_spacing>}
    {width <width_increment>}
    {height <height_increment>}
    {{no}autotitle {columnheader}}
    {title {"<text>"} {{no}enhanced} {center | left | right}}
    {font "<face>,<size>"}
    {textcolor <colorspec>}
    {{no}box {linestyle <style> | linetype <type> | linewidth <width>}}
    {maxcols {<max no. of columns> | auto}}
    {maxrows {<max no. of rows> | auto}}
```

## Axis Limits

```
set xrange
    [{{<min>}:{<max>}}]
    {{no}reverse}
    {{no}writeback}
    {{no}extend}

set xrange restore
```

```
<min> -> Explicit Numeric | <autoscaled>
<autoscaled> -> <lower bound> < * < <upper bound> |
                <lower bound> < * |
                * < <upper bound> |
                *
```

```
set datafile separator { whitespace | tab | comma | "<chars>" }
```

## Converting Numbers to Strings

- `sprintf(format, variables)`

## Time

```gnuplot
# Suppose the file "data" contains records like
03/21/95 10:00 6.02e23
# This file can be plotted by
set xdata time
set timefmt "%m/%d/%y"
set xrange ["03/21/95":"03/22/95"]
set format x "%m/%d"
set timefmt "%m/%d/%y %H:%M"
plot "data" using 1:3
```

```
%a abbreviated name of day of the week
%A full name of day of the week
%b or %h abbreviated name of the month
%B full name of the month
%d day of the month, 01–31
%D shorthand for "%m/%d/%y" (only output)
%F shorthand for "%Y-%m-%d" (only output)
%k hour, 0–23 (one or two digits)
%H hour, 00–23 (always two digits)
%l hour, 1–12 (one or two digits)
%I hour, 01–12 (always two digits)
%j day of the year, 001–366
%m month, 01–12
%M minute, 00–60
%p ”am” or ”pm”
%r shorthand for "%I:%M:%S %p" (only output)
%R shorthand for "%H:%M" (only output)
%S second, integer 00–60 on output, (double) on input
%s number of seconds since start of year 1970
%T shorthand for "%H:%M:%S" (only output)
%U week of the year (CDC/MMWR ”epi week”) (ignored on input)
%w day of the week, 0–6 (Sunday = 0)
%W week of the year (ISO 8601 week date) (ignored on input)
%y year, 0-99 in range 1969-2068
%Y year, 4-digit
%z timezone, [+-]hh:mm
%Z timezone name, ignored string
```

## Font Size Rendering

Notes to myself on gnuplot font rendering.
tags: ppi dpi fonts gnuplot

On my computer at least: The fonts are rendered at 144 pixels per inch
The stored resolution of the PNG image is 96 ppi.

So for a high quality figure, can size the image for 3 * 144 = 432 ppi.
The fontscale property has to be set to 3 then to match the font size of
the text in the rest of the document.

The 144 likely comes from the fact that with my high resolution
displays, the font size is set to 150%, which would take the default
cairo/pango resolution of 96 and scale it to 144. Note that this is only
when using the Windows executable, if using the Unix version, this goes
back to the 96 ppi.

The size of a font typically measure from the lowest point of a
descender to the highest point of an ascender. Check out

`https://graphicdesign.stackexchange.com/questions/4035/what-does-the-size-of-the-font-translate-to-exactly`

A point is 1/72 of an inch. Have to be careful

From answer on [SO](https://stackoverflow.com/a/27336389),
PNGs have metadata about image resolution in pixels/meter about image resolution in pixels/meter.
`imagemagick` can update that meta data with a command like

```
gnuplot - | magick png:- -units PixelsPerInch -density 384 plot.png
```

## Data Blocks

```gnuplot
$var << EOD
...
...
EOD

plot $var using 1:2 ...
```

## Filtering

Probably easiest to rely on shelling out to awk or some external program.

```gnuplot
plot "< awk '$1 == 2' data.txt"
```

## Time

Time is number of seconds from the year 1970.

Can use
```gnuplot
integer = strptime("%Y", "2015")
```

## Inline data with special file

See 'Special-filenames' in gnuplot docs.

```gnuplot
plot '-'
1 2
3 4
e
```

## Replot

Can use `replot` to run several plot commands


## PNG markers

```
pointtype or pt
1 = +
2 = x
3 = sparkly x
4 = open square
5 = filled square
6 = open circle
7 = filled circle
8 = open triangle
9 = filled triangle
10 = open inverted triangle
11 = filled inverted triangle
12 = open diamond
13 = filled diamond
14 = open pentagon
15 = filled pentagon
16 = + (again?)
17 = x (again?)
18 = sparkly x (again?)
19 = open square (again?)
20 = filled square (again?)
21 = open circle (again?)
22 = filled circle (again?)
```

## Single digit month/day

<https://stackoverflow.com/questions/62410451/single-digit-month-and-day-format-specifier-in-gnuplot-5-2>

```
"%1m/%1d/%Y"
```

## Compiling 6 on WSL Ubuntu

Had to turn off the Qt terminal to get it to compile.

```bash
./configure --with-qt=no
make
sudo make install
```
