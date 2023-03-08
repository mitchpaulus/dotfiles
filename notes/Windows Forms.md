

- [Preventing scrolling in combo boxes](https://stackoverflow.com/a/1883072/5932184)
  - `comboBox1.MouseWheel += (o, e) => ((HandledMouseEventArgs)e).Handled = true;`


# DPI scaling


- [Automatic Scaling](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/forms/autoscale?view=netdesktop-7.0)

ContainerControl's have AutoScaleMode and AutoScaleDimensions

AutoScaleDimensions is

AutoScaleFactor = scaling ratio between the current and design-time scaling automatic scaling dimensions.

PerformAutoScale called by OnLayout method.
