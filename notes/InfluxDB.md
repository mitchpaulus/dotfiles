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
influx write --host http://localhost:8086 --token <token> --bucket 'Bucket Name' --org-id '1234556' -p s -f data.lp --format lp
```

Basic line protocol:

```
measurement value=<VALUE> <UNIX_TIMESTAMP>
measurement value=10.2 1625097600
```

## Pricing Cloud

As of 2024-12-13
Usage-Based Plan
$0.0025/Mb for data in
$0.09/GB for data out
$0.012/100 queries
$0.002/GB-hour for storage or $1.44/GB-month (30-days)

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

## Error Handling C#

<https://github.com/influxdata/influxdb-client-csharp/issues/135>

## Python

`pip install influxdb-client`


## List Measurements

<https://docs.influxdata.com/influxdb/v2.7/query-data/flux/explore-schema/#list-measurements>

```
import "influxdata/influxdb/schema"

schema.measurements(bucket: "example-bucket")
```

Look at script `influx_meas` for shell script implementation.

## Flux

```
from(bucket:"example-bucket") |> range(start: 2021-01-01, stop: 2022-01-01) |> filter(fn: (r) => r._measurement == "trend name")
```

## Annotated CSV - Response

<https://docs.influxdata.com/influxdb/v2/reference/syntax/annotated-csv/>

## Typical data query

```
from(bucket: "example-bucket")
  |> range(start: 2021-01-01, stop: 2022-02-01)
  |> filter(fn: (r) => r._measurement == "cpu" or r._measurement == "mem")
  |> yield()
```

## Regex

```
expression =~ /regex/
expression !~ /regex/
```

```
2021-01-01
2021-01-01T00:00:00Z
2021-01-01T00:00:00.000Z
```

## Optimize Writes

- Batch to 5000
- Sort tags by key (Go's bytes.Compare function)
- Coarsest time
- gzip compression

<https://docs.influxdata.com/influxdb/v2/write-data/best-practices/optimize-writes/>
