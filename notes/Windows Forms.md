

- [Preventing scrolling in combo boxes](https://stackoverflow.com/a/1883072/5932184)
  - `comboBox1.MouseWheel += (o, e) => ((HandledMouseEventArgs)e).Handled = true;`
