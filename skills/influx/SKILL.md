---
name: 'influx'
description: 'We use influx as our time series database for building automation system data. This skill describes the setup and tools for making use of that data.'
---

We use influx as our time series database for building automation system data.
We use the Open Source version v2.
This skill describes the setup and tools for making use of that data.

You can get a list of our buckets using the script:

`influx_buckets`

and a list of the available trends (measurements):

`influx_meas`

We store each trend as a unique measurement.
You can use the `influx` CLI directly to get back annotated CSV data from a flux query.
