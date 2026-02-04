# Meteostat

[API docs](https://dev.meteostat.net/api)

<https://meteostat.p.rapidapi.com> - Base url

`X_RAPIDAPI_KEY`

```
curl --request GET \
	--url 'https://meteostat.p.rapidapi.com/stations/meta?id=10637' \
	--header 'x-rapidapi-host: meteostat.p.rapidapi.com' \
	--header 'x-rapidapi-key: {key}'
```


<https://dev.meteostat.net/api/stations/hourly>

```
GET https://meteostat.p.rapidapi.com/stations/hourly

Can only get month at a time.

Parameter	Description	Type	Required	Default
station	The weather station ID	String	Yes	undefined
start	  The start date of the period (YYYY-MM-DD)	String	Yes	undefined
end	The end date of the period (YYYY-MM-DD)	String	Yes	undefined
tz	The time zone according to the tz database	String	No	UTC (America/Chicago)
model	Substitute missing records with statistically optimized model data	String	No	true
freq	The time frequency of the records. Can be used for custom aggregation	String	No	null
units	The unit system of the meteorological parameters	String	No	metric (metric, imperial, scientific)
```

```
The response body includes the following properties. Please note that all units mentioned below refer to the default units setting.

The list is in the root level 'data' attribute

Parameter	Description	Type
time	Time of observation (YYYY-MM-DD hh:mm:ss)	String
temp	The air temperature in °C	Float
dwpt	The dew point in °C	Float
rhum	The relative humidity in percent (%)	Integer
prcp	The one hour precipitation total in mm	Float
snow	The snow depth in mm	Integer
wdir	The wind direction in degrees (°)	Integer
wspd	The average wind speed in km/h	Float
wpgt	The peak wind gust in km/h	Float
pres	The sea-level air pressure in hPa	Float
tsun	The one hour sunshine total in minutes (m)	Integer
coco	The weather condition code	Integer
```
