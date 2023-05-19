# Database

I'm having a hard time finding a database to meet my needs, thinking of building something extremely simple myself.

Wants:

- Simple schema
  - String name -> Time Series Data (Numerics only), only need 4 sig figs.
- Second precision
- Single binary
- Normal HTTP if run as a service
- Simple caching, just store last x number of queries or something.
- Should also work without server/service running, just reading file if necessary.

- Indexed at day level. So queries that start/end on days are fast
