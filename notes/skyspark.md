# SkySpark

## Video 12. Spark App (15:07)
- Began in 3.0.15.
- Can't recreate the split feature at 7:00
- Swivel tool analogous to Pivot tables in Excel, can group rows by
  different categories. Can change the types of visualizations for
  different metrics. For example, bar chart can be represented as bubble
  chart.

- Can export the tabular information in Swivel to Excel. Best if the
  data is 'text'.

- Can save views as 'Favorites', viewable from the Favorites app.


## Video 13. KPI App (7:04)

- 3 bubble chart view
    - Solid - single value
    - Hollow - Range
    - Pie - Delta

- KPIs are considered as "rules"

- In swivel options: 'Rule' should always be the column group
- By default, bubble are sized per column. In the options, you can set
  "Visualize across columns by unit".

- KPI is just a tag? (6:46)

## Video 14. Energy Views (13:58)

- Energy App is really a suite of apps
- Compass 'Aggregation Functions' called 'Folds' in SkySpark
- Can normalize the energy data by factors that we can create (2:15)
    - Not sure what base temperature is used for the 'Degree Day' or
      whether it's heating or cooling in the demo. I'm sure it's just
      something you can define yourself when making the factor.

- Profile Tab (or 'view' is the more technical SkySpark term?):
    - Most common usage: Look at average daily profiles.
    - Daily overlay - Kind of like stacked batch plot with continuous
      time.
    - Heat map visualization is here
    - Load Duration - answers the question: "How many hours have I been
      above a certain threshold?"

- Operation Tab (7:48)
    - Visualization with the both the usage and the on/off status of
      equipment.

- Tariff Tab (9:34)
    - Adds tariff data as a bar to some of the plots. No information given
    on how to enter the different tariff information.

- Swivel Tab (11:30)
    - All the basic pivot table functionality you would expect.


## Video 15. Historian Views (5:30)

- Chart view (0:00)
    - Basic charting against time.

- Equip view (1:56)
    - Basic charting for equipment. Plots all points for a given piece
      of equipment.

- Correlate view (2:45)
    - XY Plotter. Can only do single X-Y pair.
    - Ignoring is limited: Just days of the week and by some expression
      for a single point.

## Video 21. Settings App (2:43)

1. Host Namespace vs. Project Namespace
    - SysMods provide functionality at the "Host" level
    - Extensions provide additional functionality at the project level
2. SysMods
3. Exts
4. Host Settings
5. Project Settings
    - Project namespace has access to all the SysMods AND extensions

    Common project views:
        1. Project
        2. Rule
        3. UI

Overall, this video quite limited in the actual details about what the
different settings do.


## Video 23. Rule Views (8:12) v3.0.15

- Local view: Deals with rules running on the server that SkySpark is
  installed on.

- Rules are based on "functions"
- (1:55) Shows that rule cost from UI was only a certain $/hr.

- Generally like to break rules out into either Sparks or KPIs

- "Rules run on a local instance of SkySpark" (3:18)

- Rule runs against "Targets". SkySpark does not analyze the data
  "on-the-fly" like Compass does. In some cases, it looks you may need
  to "Recompute" data if things have changed.

- Debug view
    - (7:25) Debug -> Index -> Summary, can update `hisEngine` options
      that allow rules to be run in parallel.
