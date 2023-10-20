# Weather Data

<ftp://ftp.ncdc.noaa.gov/pub/data/noaa/>

Otherwise, can use browser at:

<https://www1.ncdc.noaa.gov/pub/data/noaa/>


Format document:

<ftp://ftp.ncdc.noaa.gov/pub/data/noaa/isd-format-document.pdf>

or

<https://www1.ncdc.noaa.gov/pub/data/noaa/isd-format-document.pdf>

DFW Airport Weather Station:

722590-03927

`ftp://ftp.ncdc.noaa.gov/pub/data/noaa/2021/722590-03927-2021.gz`

Can then use `gunzip` to unzip the file.

```
wget ftp://ftp.ncdc.noaa.gov/pub/data/noaa/2021/722590-03927-2021.gz && gunzip 722590-03927-2021.gz
```

ISD Format

1-4: Total Variable Characters
5-10: USAF
11-15: WBAN
16-23: Date in YYYYMMDD form
24-27: UTC Time in HHMM form
28: Source
29-34: Latitude [+-][0-9]{5} Scaling factor: 1000 +99999 = Missing
35-41: Longitude [+-][0-9]{5}
42-46: Code
47-51: Elevation (m)
52-56: Call letter identifier
57-60: Quality control process name
61-63: Wind direction angle
64: Wind direction quality
65: Wind direction Type
66-69: Wind speed (m/s) Scaling factor: 10
70: Wind speed quality
71-75: Ceiling Height dimension (m)
76: Ceiling Height Quality
77: Ceiling determination code
78: CAVOK code
79-84: Visibility distance (m)
85: Visibility quality code
86: Visibility variability code
87: Visibility variability quality code
88-92: Dry Bulb Air Temperature (C), Scale factor: 10 [+-][0-9]{4} '+9999' is missing
93: Dry Bulb Air Temperature Quality
94-98: Dew Point Air Temperature (C), Scale factor: 10 [+-][0-9]{4} '+9999' is missing
99: Dew Point Temperature quality code
100-104: Air pressure (Hectopascals), Scale factor: 10
105: Air pressure quality code

106-108: ADD: If section exists

Precipitation Data
AA[1-4]: Liquid-precipitation  2 4 1 1 = 8
AB1: Liquid-precipitation monthly total 5 1 1 = 7
AC1: Precipitation observation history 1 1 1 = 3
AD1: Liquid precipitation greatest amount in 24 hours, for the month 5 1 4 4 4 1 = 19
AE1: Liquid precipitation, number of days with specific amounts, for the month 2 1 2 1 2 1 2 1 = 12
