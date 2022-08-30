# Data Model

[Reference](https://docs.influxdata.com/influxdb/cloud/reference/key-concepts/data-elements/)


Data is stored in `_measurement`s.
Buckets ~ Relational Database
Measurement ~ Relational Table

All data has `_time` column

Fields are the data that vary over time.
Fields have name and type

Tags are meta data to describe our field data.

Buckets can have retention policies.


## POints

In InfluxDB, a point represents a single data record, similar to a row in a SQL database table. Each point:

- has a measurement, a tag set, a field key, a field value, and a timestamp;
- is uniquely identified by its series and timestamp.
- In a series, each point has a unique timestamp. If you write a point to a series with a timestamp that matches an existing point, the field set becomes a union of the old and new field set, where any ties go to the new field set.

## series

A collection of data in the InfluxDB data structure that shares a measurement, tag set, and bucket.


## WritePrecision

Can write at different levels of time precision.

From <https://influxdb-client.readthedocs.io/en/stable/_modules/influxdb_client/domain/write_precision.html#WritePrecision>

MS = "ms"  (millisecond)
S = "s" (second)
US = "us" (?)
NS = "ns" (nanosecond = default)
