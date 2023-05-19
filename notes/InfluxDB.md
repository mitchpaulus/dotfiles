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


## Points

In InfluxDB, a point represents a single data record, similar to a row in a SQL database table. Each point:

- has a measurement, a tag set, a field key, a field value, and a timestamp;
- is uniquely identified by its series and timestamp.
- In a series, each point has a unique timestamp. If you write a point to a series with a timestamp that matches an existing point, the field set becomes a union of the old and new field set, where any ties go to the new field set.

## series

A collection of data in the InfluxDB data structure that shares a measurement, tag set, and bucket.

## Write Precision

Can write at different levels of time precision.

From <https://influxdb-client.readthedocs.io/en/stable/_modules/influxdb_client/domain/write_precision.html#WritePrecision>

MS = "ms"  (millisecond)
S = "s" (second)
US = "us" (?)
NS = "ns" (nanosecond = default)

## Where is the data located?

<https://docs.influxdata.com/influxdb/v2.4/reference/internals/file-system-layout/?t=Linux>

If installed standalone

Path	Default
Engine path	  ~/.influxdbv2/engine/
Bolt path	    ~/.influxdbv2/influxd.bolt
SQLite path	  ~/.influxdbv2/influxd.sqlite
Configs path	~/.influxdbv2/configs

If installed as package:

Path	Default
Engine path	/var/lib/influxdb/engine/
Bolt path	/var/lib/influxdb/influxd.bolt
SQLite path	/var/lib/influxdb/influxd.sqlite
Configs path	/var/lib/influxdb/configs
Default config file path	/etc/influxdb/config.toml

## Installation

Easy installation. Download zip with single file binary. Run it.
Normally capture the output to files:

```sh
./influxd >stdin.txt 2>stdout.txt &
```

Migration to new database is just running new executable as long as the data hasn't moved from locations above.

## Writing

Example CLI:

```sh
influx write --host HOST --token <token> --bucket 'Bucket Name' --org-id '1234556' -p s -f data.lp --format lp
```

## Pricing Cloud

Usage-Based Plan
- Data In
  Volume of data written in MB
  $0.002/MB
- Query Count
  Total individual query executions
  $0.01 per 100 query executions
- Storage
  Total disk usage in GB-hours
  $0.002/GB-hour
- Data Out
  Data transferred out of InfluxDB in GB
  $0.09/GB

$250 credit for you to use in your first 30 days on the Usage-Based Plan

## Duration Types

```
1ns // 1 nanosecond
1us // 1 microsecond
1ms // 1 millisecond
1s  // 1 second
1m  // 1 minute
1h  // 1 hour
1d  // 1 day
1w  // 1 week
1mo // 1 calendar month
1y  // 1 calendar year
```
