# pyhaystack


```python
session = pyhaystack.connect(**json.load(open("connection.json", "r")))


# session.find_entity :: String -> Dict[Entity]
session.find_entity(filter_expr='func')


```

## Entities

```python
entity.dis  # Description field of the entry
entity.id   # Fully qualified Id
entity.tags # tags of the entity. Type: pyhaystack.client.entity.tags.ReadOnlyEntityTags. Operates like a dictionary with tag names as keys.
```

## Tag Dictionary

Possible data types of values

```
SkySpark == Python
String == str
Marker Tag == hszinc.datatypes.MarkerType
DateTime == datetime.datetime
```
