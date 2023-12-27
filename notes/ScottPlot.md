Multiple Plot Controls with Shared Axes

<https://scottplot.net/faq/shared-axes/>

```csharp
readonly FormsPlot[] FormsPlots;

public LinkedPlots()
{
    InitializeComponent();

    // plot sample data
    formsPlot1.Plot.AddSignal(DataGen.Sin(51));
    formsPlot2.Plot.AddSignal(DataGen.Cos(51));

    // populate array of plots for easy iteration later
    FormsPlots = new FormsPlot[] { formsPlot1, formsPlot2 };
    foreach (var fp in FormsPlots)
        fp.AxesChanged += OnAxesChanged;
}

// ....

private void OnAxesChanged(object sender, EventArgs e)
{
    FormsPlot changedPlot = (FormsPlot)sender;
    var newAxisLimits = changedPlot.Plot.GetAxisLimits();

    foreach (var fp in FormsPlots)
    {
        if (fp == changedPlot)
            continue;

        // disable events briefly to avoid an infinite loop
        fp.Configuration.AxesChangedEventEnabled = false;
        fp.Plot.SetAxisLimits(newAxisLimits);
        fp.Render();
        fp.Configuration.AxesChangedEventEnabled = true;
    }
}

```

## Datetime data on SignalPlot

- Add sample rate, and offset to beginning date

```
var plt = new ScottPlot.Plot(600, 400);

// create data sample data
double[] ys = DataGen.RandomWalk(100);

TimeSpan ts = TimeSpan.FromSeconds(1); // time between data points
double sampleRate = (double)TimeSpan.TicksPerDay / ts.Ticks;
var signalPlot = plt.AddSignal(ys, sampleRate);

// Then tell the axis to display tick labels using a time format
plt.XAxis.DateTimeFormat(true);

// Set start date
signalPlot.OffsetX = new DateTime(1985, 10, 1).ToOADate();

plt.SaveFig("ticks_dateTime_signal.png");
```
