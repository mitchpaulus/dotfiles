Comma separated

# Data fields

- 0: Year (Not really used in EnergyPlus simulations)
- 1: Month (1-12, Required)
- 2: Day (1-31, Required)
- 3: Hour (1-24, Required Hour 1 is 00:01 to 01:00)
- 4: Minute (1-60)
- 5: Data Source and Uncertainty Flags
- 6: Dry Bulb Temperature (C, 99.9 missing)
- 7: Dew Point Temperature (C, 99.9 missing)
- 8: Relative Humidity (% or 0-100, 999 missing)
- 9: Atmospheric Station Pressure (Pa, 999999 missing)
- 10: Extraterrestrial Horizontal Radiation (Wh/m2, Not currently used, 9999 missing)
- 11: Extraterrestrial Direct Normal Radiation (Wh/m2, Not currently used, 9999 missing)
- 12: Horizontal Infrared Radiation Intensity (Wh/m2, 9999 missing. If missing calculated from Opaque Sky Cover field)
- 13: Global Horizontal Radiation (Wh/m2, not currently used, 9999 missing)
- 14: Direct Normal Radiation (Wh/m2,  >=9999 missing) (Amount of solar radiation in Wh/m2 received directly from the solar disk on a surface perpendicular to the sun’s rays, during the number of minutes preceding the time indicated.) If the field is missing (≥ 9999 ) or invalid (< 0 ), it is set to 0. Counts of such missing values are totaled and presented at the end of the run period.
- 15: Diffuse Horizontal Radiation (Wh/m2, >=9999 missing) (Amount of solar radiation in Wh/m2 received from the sky (excluding the solar disk) on a horizontal surface during the number of minutes preceding the time indicated.) If the field is missing (≥ 9999 ) or invalid (< 0 ), it is set to 0.
- 16: Global Horizontal Illuminance (lux, not currently used, 999999 missing)
- 17: Direct Normal Illuminance (lux, not currently used, 999999 missing)
- 18: Diffuse Horizontal Illuminance (lux, not currently used, 999999 missing)
- 19: Zenith Luminance (Cd/m2, not currently used, 9999 missing)
- 20: Wind Direction (degrees, 999 missing) This is the Wind Direction in degrees where the convention is that North = 0.0, East = 90.0, South = 180.0, West = 270.0. (Wind direction in degrees at the time indicated. If calm, direction equals zero.) Values can range from 0 to 360. Missing value is 999.
- 21: Wind Speed (m/s, 0-40, 999 missing)
- 22: Total Sky Cover (tenths of coverage, 99 missing, 0 - 10)
- 23: Opaque Sky Cover (tenths of coverage, 99 missing, 0 - 10) This is not used unless the field for Horizontal Infrared Radiation Intensity is missing and then it is used to calculate Horizontal Infrared Radiation Intensity. Minimum value is 0; maximum value is 10; missing value is 99.
- 24: Visibility (km, not currently used, 9999 missing)
- 25: Ceiling Height (m, not currently used, 99999 missing)
- 26: Present Weather Observation (0 or 9) 0 = Weather observation made. 9 = Weather observation not made, or missing
- 27: Present Weather Codes (999999999 missing)
- 28: Precipitable Water (mm, not currently used, 999 missing)
- 29: Aerosol Optical Depth (thousandths, not currently used, .999 missing)
- 30: Snow Depth (cm, 999 missing)
- 31: Days Since Last Snowfall (days, not currently used, 99 missing)
- 32: Albedo (ratio, not currently used, doesn't say missing, average albedo on Earth is ~0.3)
- 33: Liquid Precipitation Depth (mm, 999 missing)
- 34: Liquid Precipitation Quantity (hr, not currently used, 99 missing)


## Data source and uncertainty

Data Flag                                        | Flag Values
-------------------------------------------------|------------
Dry Bulb Temperature Data Source                 | A-F
Dry Bulb Temperature Data Uncertainty            | 0-9
Dew Point Temperature Data Source                | A-F
Dew Point Temperature Data Uncertainty           | 0-9
Relative Humidity Data Source                    | A-F
Relative Humidity Data Uncertainty               | 0-9
Atmospheric Station Pressure Data Source         | A-F
Atmospheric Station Pressure Data Uncertainty    | 0-9
Horizontal Infrared Radiation Data Source        | A-H, ?
Horizontal Infrared Radiation Data Uncertainty   | 0-9
Global Horizontal Radiation Data Source          | A-H, ?
Global Horizontal Radiation Data Uncertainty     | 0-9
Direct Normal Radiation Data Source              | A-H, ?
Direct Normal Radiation Data Uncertainty         | 0-9
Diffuse Horizontal Radiation Data Source         | A-H, ?
Diffuse Horizontal Radiation Data Uncertainty    | 0-9
Global Horizontal Illuminance Data Source        | I, ?
Global Horizontal Illuminance Data Uncertainty   | 0-9
Direct Normal Illuminance Data Source            | I, ?
Direct Normal Illuminance Data Uncertainty       | 0-9
Diffuse Horizontal Illuminance Data Source       | I, ?
Diffuse Horizontal Illuminance Data Uncertainty  | 0-9
Zenith Luminance Data Source                     | I, ?
Zenith Luminance Data Uncertainty                | 0-9
Wind Direction Data Source                       | A-F
Wind Direction Data Uncertainty                  | 0-9
Wind Speed Data Source                           | A-F
Wind Speed Data Uncertainty                      | 0-9
Total Sky Cover Data Source                      | A-F
Total Sky Cover Data Uncertainty                 | 0-9
Opaque Sky Cover Data Source                     | A-F
Opaque Sky Cover Data Uncertainty                | 0-9
Visibility Data Source                           | A-F, ?
Visibility Data Uncertainty                      | 0-9
Ceiling Height Data Source                       | A-F, ?
Ceiling Height Data Uncertainty                  | 0-9
Precipitable Water Data Source                   | A-F
Precipitable Water Data Uncertainty              | 0-9
Broadband Aerosol Optical Depth Data Source      | A-F
Broadband Aerosol Optical Depth Data Uncertainty | 0-9
Snow Depth Data Source                           | A-F, ?
Snow Cover Data Uncertainty                      | 0-9
Days Since Last Snowfall Data Source             | A-F, ?
Days Since Last Snowfall Data Uncertainty        | 0-9

Solar Radiation and Illuminance Data Source Flag Codes

Flag Code Definition
A Post-1976 measured solar radiation data as received from NCDC or other sources
B Same as ”A” except the global horizontal data underwent a calibration correction
C Pre-1976 measured global horizontal data (direct and diffuse were not measured before 1976), adjusted from solar to local time, usually with a calibration correction
D Data derived from the other two elements of solar radiation using the relationship, global = diffuse + direct × cosine (zenith)
E Modeled solar radiation data using inputs of observed sky cover (cloud amount) and aerosol optical depths derived from direct normal data collected at the same location
F Modeled solar radiation data using interpolated sky cover and aerosol optical depths derived from direct normal data collected at the same location
G Modeled solar radiation data using observed sky cover and aerosol optical depths estimated from geographical relationships
H Modeled solar radiation data using interpolated sky cover and estimated aerosol optical depths
I Modeled illuminance or luminance data derived from measured or modeled solar radiation data
? Source does not fit any of the above categories. Used for nighttime values and missing data

Solar Radiation and Illuminance Data Uncertainty Flag Codes

Flag Uncertainty Range (%)
1 Not used
2 2 - 4
3 4 - 6
4 6 - 9
5 9 - 13
6 13 - 18
7 18 - 25
8 25 - 35
9 35 - 50
0 Not applicable



Meteorological Data Source Flag Codes

Flag Definition
A Data as received from NCDC, converted to SI units
B Linearly interpolated
C Non-linearly interpolated to fill data gaps from 6 to 47 hours in length
D Not used
E Modeled or estimated, except: precipitable water, calculated from radiosonde data; dew point temperature calculated from dry bulb temperature and relative humidity; and relative humidity calculated from dry bulb temperature and dew point temperature
F Precipitable water, calculated from surface vapor pressure; aerosol optical depth, estimated from geographic correlation
? Source does not fit any of the above. Used mostly for missing data

Meteorological Uncertainty Flag Codes

1- 6 Not used
7 Uncertainty consistent with NWS practices and the instrument or observation used to obtain the data
8 Greater uncertainty than 7 because values were interpolated or estimated
9 Greater uncertainty than 8 or unknown.
0 Not definable.


## Header Lines

LOCATION,
    A1, \field city
        \type alpha
    A2, \field State Province Region
        \type alpha
    A3, \field Country
        \type alpha
    A4, \field Source
        \type alpha
    N1, \field WMO
        \note usually a 6 digit field. Used as alpha in EnergyPlus
        \type alpha
    N2 , \field Latitude
        \units deg
        \minimum -90.0
        \maximum +90.0
        \default 0.0
        \note + is North, - is South, degree minutes represented in decimal (i.e. 30 minutes is .5)
        \type real
    N3 , \field Longitude
        \units deg
        \minimum -180.0
        \maximum +180.0
        \default 0.0
        \note - is West, + is East, degree minutes represented in decimal (i.e. 30 minutes is .5)
        \type real
    N4 , \field TimeZone
        \units hr - not on standard units list???
        \minimum -12.0
        \maximum +12.0
        \default 0.0
        \note Time relative to GMT.
        \type real
    N5 ; \field Elevation
        \units m
        \minimum -1000.0
        \maximum< +9999.9
        \default 0.0
        \type real

DESIGN CONDITIONS,
    N1, \field Number of Design Conditions
    A1, \field Design Condition Source
        \note current sources are ASHRAE HOF 2009 US Design Conditions, Canadian Design Conditions
        \note and World Design Conditions
    A2, \field Design Condition Type (HEATING)
        \note fields here will be dependent on the source, they are shown in a header/data format
        \note in both the .rpt and .csv files that are produced by the WeatherConverter program
    ...
    An, \field Design Condition Type (COOLING)
        \note same as note on Heating Design Conditions

TYPICAL/EXTREME PERIODS,
N1, \field Number of Typical/Extreme Periods
A1, \field Typical/Extreme Period 1 Name
A2, \field Typical/Extreme Period 1 Type
A3, \field Period 1 Start Day
A4, \field Period 1 End Day
\note repeat (A1-A3) until number of typical periods
-- etc to # of periods entered


HOLIDAYS/DAYLIGHT SAVING,
A1, \field LeapYear Observed
    \type choice
    \key Yes
    \key No
    \note Yes if Leap Year will be observed for this file
    \note No if Leap Year days (29 Feb) should be ignored in this file
A2, \field Daylight Saving Start Day
A3, \field Daylight Saving End Day
N1, \field Number of Holidays (essentially unlimited)
A4, \field Holiday 1 Name
A5, \field Holiday 1 Day
\note repeat above two fields until Number of Holidays is reached

```
HOLIDAYS/DAYLIGHT SAVINGS,No,2 Sunday in March,1 Sunday in November,0
```

DATA PERIODS,
N1, \field Number of Data Periods
N2, \field Number of Records per hour
A1, \field Data Period 1 Name/Description
A2, \field Data Period 1 Start Day of Week
    \type choice
    \key Sunday
    \key Monday
    \key Tuesday
    \key Wednesday
    \key Thursday
    \key Friday
    \key Saturday
A3, \field Data Period 1 Start Day
A4, \field Data Period 1 End Day
\note repeat above to number of data periods
-- etc to # of periods entered

```
DATA PERIODS,1,1,Data,Tuesday,1/1/2019,12/31/2019
```
