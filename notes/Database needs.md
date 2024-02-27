# Database

I'm having a hard time finding a database to meet my needs,
thinking of building something extremely simple myself.

Wants:

- Simple schema
  - String name -> Time Series Data (Numerics only), only need 4 sig figs.
- Second precision
- Single binary
- Normal HTTP if run as a service
- Simple caching, just store last x number of queries or something.
- Should also work without server/service running, just reading file if necessary.

- Indexed at day level. So queries that start/end on days are fast

Numbers to keep in mind:

1 byte = 256
2 bytes = 65,536
3 bytes = 16,777,216
4 bytes = 4,294,967,296

Seconds in a day: 86,400
Minutes in a day: 1440
Minutes in a year: 525,600

5 minutes data = 288/day, 105,120/year

10,000 trends @ 5 minutes = 1,051,200,000


1 Gb    = 1,073,741,824 bytes

Index by day

Then run length and dictionary encode both the time stamps and the string values.

Keep everything as strings.

Typical file system block size: 4096 bytes
