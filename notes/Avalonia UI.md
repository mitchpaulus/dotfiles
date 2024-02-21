# Getting Started

```
dotnet new avalonia.app -o MyApp
dotnet new sln --name Name
dotnet sln add MyApp/MyApp.csproj
```


- Take up full dimension:
  - `VerticalAlignment="Stretch"`

- Give Name that can be referenced
  - `Name="MyThing"`

- Font Color
  -`Foreground: Red`




## Binding

```C#
set {
    _property = value;
    OnPropertyChanged(nameof(Property)); // Updates UI elements
}
```

## ListBox

```csharp
public TrendDialogVm(List<IDataSource> sources)
{
    Sources = sources;
    SourceList = new ObservableCollection<IDataSource>(sources);
    SelectionModel = new SelectionModel<IDataSource>();
    SelectionModel.SelectionChanged += SelectionModelOnSelectionChanged;
    SelectionModel.SingleSelect = false; // KEY - otherwise this defaults to true
    _selectedSources = new ObservableCollection<IDataSource>();
}

private void SelectionModelOnSelectionChanged(object? sender, SelectionModelSelectionChangedEventArgs<IDataSource> e)
{
    if (sender is not SelectionModel<IDataSource> selectionModel) return;

    _selectedSources.Clear();

    foreach (var i in selectionModel.SelectedItems)
    {
        _selectedSources.Add(i);
    }

    OnPropertyChanged(nameof(SelectedSources));
}
```

## Commands

[help](https://docs.avaloniaui.net/docs/0.10.x/data-binding/binding-to-commands)

## New Window

```csharp
dotnet new avalonia.window -n InfluxDialog
```
