## Local imports not being resolved

- [https://github.com/microsoft/pyright/issues/272](https://github.com/microsoft/pyright/issues/272)
- Need to add `executionEnvironments` to location in "pyrightconfig.json"
```
{
    "executionEnvironments": [
        {
            "root": "code"
        }
    ]
}
```
