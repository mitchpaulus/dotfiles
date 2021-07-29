# Charting

## Types

Add `chartType` tag to *column* meta tag

 - bar
 - donut
 - heatMap
 - line
 - pie
 - runtime
 - scatter
 - stackedBar

Grid meta tag:

    title: string to add title to top of chart
    noData: string message to use if no data available to chart
    chartType: defines chart type for all series
    chartLegend: string enum for legend control
    chartLegendNoSort: disable sorting by dis in legend, force grid column order
    chartNoScroll: marker tag to disable scrolling

Column meta tags (individual series):

    chartType: defines chart type for column as y-axis
    chartGroup: defines explicit chart grouping
    color: series color
    strokeWidth: width of line plots
    strokeDasharray: on/off pattern string such as "6,4" for line plots
    opacity: alpha transparency for area fills as number from 0.0 to 1.0
    chartAreaMode: used to render line plot as area plot
    chartMin: defines series axis min value
    chartMax: defines series axis max value
    chartHeight: use a fixed height for series plot
    exclude: marks a series as excluded (not used to compute y-axis bounds)
    format: axis format

### Donut

Typical grid for donut chart is single row. First column sets label
underneath. Rest set values for the plot.
