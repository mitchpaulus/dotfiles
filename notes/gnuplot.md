# gnuplot

Example:

```gnuplot
set terminal pngcairo size 960,720 font "Segoe UI,10" fontscale 1.600
set boxwidth 0.1
set xlabel "Flr00C_OAFan_Pres.SpcLby.1 [in. H₂O]" noenhanced
set ylabel "Percent" noenhanced
set output "965155e0-7a6d-4286-b852-794c5da309ff.png"
set xrange [*:*]
set title "3-20 to 4-17-21"
set grid
set style fill solid border -1
plot "965155e0-7a6d-4286-b852-794c5da309ff.dat" using 1:2 with boxes notitle lc rgb "#004B87"

```

## Plotting

```gnuplot
plot {<ranges>} <plot-element> {, <plot-element>, <plot-element>}
```

```gnuplot
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
    }
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
  zerrorfill   |
```

## Colorspec

```
rgbcolor "colorname"   # e.g. "blue", can find available using 'show colornames'
rgbcolor "0xRRGGBB"    # string containing hexadecimal constant
rgbcolor "0xAARRGGBB"  # string containing hexadecimal constant
rgbcolor "# RRGGBB"    # string containing hexadecimal in x11 format
rgbcolor "# AARRGGBB"  # string containing hexadecimal in x11 format
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
