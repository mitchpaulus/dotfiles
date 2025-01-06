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
