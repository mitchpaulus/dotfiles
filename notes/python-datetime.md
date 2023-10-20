# Date/Times in Python

<https://docs.python.org/3/library/datetime.html>

```python
import datetime

# https://docs.python.org/3/library/datetime.html#datetime-objects
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)


# instance attributes
date.year, month, day, hour, minute, second, microsecond
datetime.tzinfo
datetime.fold

datetime.isoformat() # YYYY-MM-DDTHH:MM:SS

# Instance methods
datetime.date() -> date
datetime.time() -> time
```

# timedelta

`timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)`

# Can add and subtract from datetime/date classes

- Objects of these types are immutable.
- Objects of these types are hashable, meaning that they can be used as dictionary keys.

## Timezones

Need to rely on external library to properly deal with timezones with DST.

Popular ones:
 - [pytz](https://pypi.org/project/pytz/)
 - [dateutil](https://dateutil.readthedocs.io/en/stable/)

# Formats

Directive | Meaning
----------|------------------------------------------------------
%d        | Day of the month as a zero-padded decimal number.
%m        | Month as a zero-padded decimal number.
%y        | Year without century as a zero-padded decimal number.
%Y        | Year with century as a decimal number.
%H        | Hour (24-hour clock) as a zero-padded decimal number.
%I        | Hour (12-hour clock) as a zero-padded decimal number.
%p        | Locale’s AM or PM.
%M        | Minute as a zero-padded decimal number.
%S        | Second as a zero-padded decimal number.

There is no non-zero-padded version of the hour.
