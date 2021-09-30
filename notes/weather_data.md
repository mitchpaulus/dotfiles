# Weather Data

ftp://ftp.ncdc.noaa.gov/pub/data/noaa/

DFW Airport Weather Station:

722590-03927


ISD Format

1-4: Total Variable Characters
5-10: USAF
11-15: WBAN
16-23: Date in YYYYMMDD form
24-27: Time in HHMM form
28: Source
29-34: Latitude [+-][0-9]{5}
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

