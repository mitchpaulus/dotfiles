My personal schema for trend configuration:

```json
{
    "bucket": "Bucket name",
    "equips": [
        { "name": "Equip name", "equipRef": "Equip name" | null }
    ],
    "points": [
        { "name": "Point name", tags: ["tag1", "tag2"], "equipRef": "Equip name" | null, "unit": "°F", "displayName": "Display Name" }
    ]
}
```


## Scenario Creation

Inputs:

- `List<List<Container>>` hierarchies
- `List<Label>` desired labels
- `Dictionary<Label, Dictionary<Container, Value (Like List<Trend>)>>` label results
- `Func Container, Label, Value -> bool` validity function

Algorithm:

- Loop over all hierarchies

```
var results = _labels.Select(label => FindMatchingContainers(label, hierarchy));
// results has an outer list with length equal to the number of labels. The inner list for each label corresponds to
// the containers that it was found in. The CartesianProduct then gets all the different combinations of selecting
// different containers from each list corresponding to the label. Each one of these combinations is a different valid
// scenario.
IEnumerable<IEnumerable<LabelContainerResult<TLabel, TContainer, TValue>>> cartesianProduct = results.CartesianProduct();
return cartesianProduct.Select(enumerable => enumerable.ToList());
```
