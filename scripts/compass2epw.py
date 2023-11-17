#!/usr/bin/env python3

from typing import List, Optional
import sys

# - 0: Year (Not really used in EnergyPlus simulations)
# - 1: Month (1-12, Required)
# - 2: Day (1-31, Required)
# - 3: Hour (1-24, Required Hour 1 is 00:01 to 01:00)
# - 4: Minute (1-60)
# - 5: Data Source and Uncertainty Flags
# - 6: Dry Bulb Temperature (C, 99.9 missing)
# - 7: Dew Point Temperature (C, 99.9 missing)
# - 8: Relative Humidity (% or 0-100, 999 missing)
# - 9: Atmospheric Station Pressure (Pa, 999999 missing)
# - 10: Extraterrestrial Horizontal Radiation (Wh/m2, Not currently used, 9999 missing)
# - 11: Extraterrestrial Direct Normal Radiation (Wh/m2, Not currently used, 9999 missing)
# - 12: Horizontal Infrared Radiation Intensity (Wh/m2, 9999 missing. If missing calculated from Opaque Sky Cover field)
# - 13: Global Horizontal Radiation (Wh/m2, not currently used, 9999 missing)
# - 14: Direct Normal Radiation (Wh/m2,  >=9999 missing) (Amount of solar radiation in Wh/m2 received directly from the solar disk on a surface perpendicular to the sun’s rays, during the number of minutes preceding the time indicated.) If the field is missing (≥ 9999 ) or invalid (< 0 ), it is set to 0. Counts of such missing values are totaled and presented at the end of the runperiod.
# - 15: Diffuse Horizontal Radiation (Wh/m2, >=9999 missing) (Amount of solar radiation in Wh/m2 received from the sky (excluding the solar disk) on a horizontal surface during the number of minutes preceding the time indicated.) If the field is missing (≥ 9999 ) or invalid (< 0 ), it is set to 0.
# - 16: Global Horizontal Illuminance (lux, not currently used, 999999 missing)
# - 17: Direct Normal Illuminance (lux, not currently used, 999999 missing)
# - 18: Diffuse Horizontal Illuminance (lux, not currently used, 999999 missing)
# - 19: Zenith Luminance (Cd/m2, not currently used, 9999 missing)
# - 20: Wind Direction (degrees, 999 missing) This is the Wind Direction in degrees where the convention is that North = 0.0, East = 90.0, South = 180.0, West = 270.0. (Wind direction in degrees at the time indicated. If calm, direction equals zero.) Values can range from 0 to 360. Missing value is 999.
# - 21: Wind Speed (m/s, 0-40, 999 missing)
# - 22: Total Sky Cover (tenths of coverage, 99 missing, 0 - 10)
# - 23: Opaque Sky Cover (tenths of coverage, 99 missing, 0 - 10) This is not used unless the field for Horizontal Infrared Radiation Intensity is missing and then it is used to calculate Horizontal Infrared Radiation Intensity. Minimum value is 0; maximum value is 10; missing value is 99.
# - 24: Visibility (km, not currently used, 9999 missing)
# - 25: Ceiling Height (m, not currently used, 99999 missing)
# - 26: Present Weather Observation (0 or 9) 0 = Weather observation made. 9 = Weather observation not made, or missing
# - 27: Present Weather Codes (999999999 missing)
# - 28: Precipitable Water (mm, not currently used, 999 missing)
# - 29: Aerosol Optical Depth (thousandths, not currently used, .999 missing)
# - 30: Snow Depth (cm, 999 missing)
# - 31: Days Since Last Snowfall (days, not currently used, 99 missing)
# - 32: Albedo (ratio, not currently used, doesn't say missing, average albedo on Earth is ~0.3)
# - 33: Liquid Precipitation Depth (mm, 999 missing)
# - 34: Liquid Precipitation Quantity (hr, not currently used, 99 missing)

def to_24_hour(hour: int, am_pm: str) -> int:
    """Converts 12-hour time to 24-hour time.

    Args:
        hour: Hour in 12-hour time.
        am_pm: AM or PM.

    Returns:
        Hour in 24-hour time.
    """
    if am_pm.upper() == 'AM':
        if hour == 12:
            return 0
        return hour
    elif am_pm.upper() == 'PM':
        if hour == 12:
            return hour
        return hour + 12
    else:
        raise ValueError('AM/PM must be AM or PM.')


def convert_record(compass_record: str) -> Optional[str]:
    split_comma = compass_record.split(',')

    datetime = split_comma[0]

    if datetime == 'Date and Time':
        return None

    dry_bulb_deg_f = split_comma[1]
    # wet_bulb_deg_f = split_comma[2]
    dew_point_deg_f = split_comma[3]

    split_datetime = datetime.split(' ')

    split_date = split_datetime[0].split('/')
    month = int(split_date[0])
    day = int(split_date[1])
    year = int(split_date[2])

    split_time = split_datetime[1].split(':')
    hour = int(split_time[0])
    minute = int(split_time[1])

    am_pm = split_datetime[2]

    hour_24 = to_24_hour(hour, am_pm)

    dry_bulb_deg_c = (float(dry_bulb_deg_f) - 32) * 5 / 9
    dew_point_deg_c = (float(dew_point_deg_f) - 32) * 5 / 9

    fields = [
        year,
        month,
        day,
        hour_24 + 1,
        minute + 1,
        "A7A7A0A7?0?0?0?0?0?0?0?0A7A7F0F0?0?0F0F0?0?0",
        f"{dry_bulb_deg_c:.2f}",
        f"{dew_point_deg_c:.2f}",
        999, # 8, Relative Humidity, allow EnergyPlus to calculate
        999999, # 9, Atmospheric Station Pressure, allow EnergyPlus to calculate
        9999, # 10, Extraterrestrial Horizontal Radiation, Not currently used, 9999 missing
        9999, # 11, Extraterrestrial Direct Normal Radiation, Not currently used, 9999 missing
        9999, # 12, Horizontal Infrared Radiation Intensity, 9999 missing. If missing calculated from Opaque Sky Cover field
        9999, # 13, Global Horizontal Radiation, Not currently used, 9999 missing
        9999, # 14, Direct Normal Radiation, >=9999 missing
        9999, # 15, Diffuse Horizontal Radiation, >=9999 missing
        999999, # 16, Global Horizontal Illuminance, Not currently used, 999999 missing
        999999, # 17, Direct Normal Illuminance, Not currently used, 999999 missing
        999999, # 18, Diffuse Horizontal Illuminance, Not currently used, 999999 missing
        9999, # 19, Zenith Luminance, Not currently used, 9999 missing
        999, # 20, Wind Direction, 999 missing
        999, # 21, Wind Speed, 0-40, 999 missing
        99, # 22, Total Sky Cover, tenths of coverage, 99 missing, 0 - 10
        99, # 23, Opaque Sky Cover, tenths of coverage, 99 missing, 0 - 10
        9999, # 24, Visibility, km, Not currently used, 9999 missing
        99999, # 25, Ceiling Height, m, Not currently used, 99999 missing
        9, # 26, Present Weather Observation, 0 or 9, 0 = Weather observation made. 9 = Weather observation not made, or missing
        999999999, # 27, Present Weather Codes, 999999999 missing
        999, # 28, Precipitable Water, mm, Not currently used, 999 missing
        999, # 29, Aerosol Optical Depth, thousandths, Not currently used, .999 missing
        999, # 30, Snow Depth, cm, 999 missing
        99, # 31, Days Since Last Snowfall, days, Not currently used, 99 missing
        '.999', # 32, Albedo, ratio, Not currently used, doesn't say missing, average albedo on Earth is ~0.3
        999, # 33, Liquid Precipitation Depth, mm, 999 missing
        99, # 34, Liquid Precipitation Quantity, hr, Not currently used, 99 missing
    ]

    epw_record = ','.join([str(field) for field in fields])
    return epw_record


def convert(compass_records: List[str]) -> List[str]:
    """Converts compass records to epw records.

    Args:
        compass_records: List of compass records.

    Returns:
        List of epw records.
    """
    epw_records = []
    for compass_record in compass_records:
        epw_record = convert_record(compass_record)
        epw_records.append(epw_record)
    return epw_records


if __name__ == '__main__':
    # Read lines from sys.stdin
    output = convert(sys.stdin.readlines())

    # Write lines to sys.stdout
    for line in output:
        if line is not None:
            sys.stdout.write(line)
            sys.stdout.write('\n')
