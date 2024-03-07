# Time

Notes related to programming against time.

## Daylight Saving Time

DST is an absolute pain.
One question I had is if there was a standard way to disambiguate local time stamps during the fall back period,
where there times that are repeated for an hour.

Python has the following PEP [495](https://www.python.org/dev/peps/pep-0495/).
Their solution is to have a variable called `fold` that has a value of 0 or 1.
If in the ambiguous period, then 0 is the first instance of the time, and 1 is the following second instance of the time.
