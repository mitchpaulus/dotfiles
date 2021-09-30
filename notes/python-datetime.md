# Date/Times in Python

https://docs.python.org/3/library/datetime.html

```
import datetime

# https://docs.python.org/3/library/datetime.html#datetime-objects
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)


# instance attributes
date.year, month, day, hour, minute, second, microsecond
datetime.tzinfo
datetime.fold

# Intance methods
datetime.date() -> date
datetime.time() -> time
```

- Objects of these types are immutable.
- Objects of these types are hashable, meaning that they can be used as dictionary keys.

## Timezones

Need to rely on external library to properly deal with timezones with DST.

Popular ones:
 - [pytz](https://pypi.org/project/pytz/)
 - [dateutil](https://dateutil.readthedocs.io/en/stable/)
