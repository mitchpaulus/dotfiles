#!/usr/bin/python3
import sys
from typing import List, Iterable, Union, Optional
import math
import json
import pathlib
from dataclasses import dataclass

def alphanum_key(s):
    tokens = []
    idx = 0
    while idx < len(s):
        if s[idx].isdigit():
            start = idx
            while idx < len(s) and s[idx].isdigit():
                idx += 1
            tokens.append(int("".join(s[start:idx])))
        else:
            start = idx
            while idx < len(s) and not s[idx].isdigit():
                idx += 1
            tokens.append(s[start:idx].lower())

    return [(0, token) if isinstance(token, int) else (1, token) for token in tokens]

def version_sort(l: Iterable[str]) -> List[str]:
    """ Sort the given iterable in the way that humans expect."""
    return sorted(l, key=alphanum_key)

def version_sort_by(l, key_selector):
    return sorted(l, key = lambda x: alphanum_key(key_selector(x)))

def version_sort_in_place(l: List[str]):
    """ Sort the given list in the way that humans expect."""
    l.sort(key=alphanum_key)

def version_sort_by_in_place(l, key_selector):
    """
    Sort the given list in the way that humans expect.
    """
    l.sort(key = lambda x: alphanum_key(key_selector(x)))


def float_str_or_autosize(selector, value):
    if value == "":
        return ""
    elif value.lower() == "autosize":
        return "Autosize"
    elif value.lower() == "autocalculate":
        return "Autocalculate"
    else:
        return selector(value)

class ScheduleYear:
    def __init__(self, fields):
        self.name = fields[1]
        self.start_month = fields[2]


def idf2tsv(file) -> list[list[str]]:
    cleaned = []

    for line in file:
        # strip everything to right of first exclamation point
        line = line.split('!')[0]
        line = line.strip()
        cleaned.append(line)

    file_contents = "".join(cleaned)

    # split on semicolon, then on comma, strip each field

    # split on semicolon
    file_contents = file_contents.split(';')

    results = []

    # When splitting on
    for obj in file_contents[0:-1]:
        fields = obj.split(',')
        fields = [field.strip() for field in fields]
        results.append(fields)

    return results


def tsv2dict(file: list[list[str]]) -> dict[str, list[list[str]]]:
    """Returns grouping by Object Type. Object Type keys are all lowercase. The list of fields includes the object type as the first field."""
    results = {}

    for line in file:
        key = line[0].lower()
        if key in results:
            results[key].append(line)
        else:
            results[key] = [line]

    return results


@dataclass
class DayScheduleValues:
    name: str
    values: list[float]

    def full_load_hours(self, timesteps_per_hour: int) -> float:
        return sum(self.values) / timesteps_per_hour


@dataclass
class AnnualScheduleValues:
    name: str
    source_type: str
    day_schedules: list[Optional[list[Optional[DayScheduleValues]]]]
    constant_value: Optional[float] = None


def eflh(file: list[list[str]]):
    d = tsv2dict(file)

    print("Day Schedules EFLH")
    day_dict = eflh_days(file)
    print()

    week_dict = eflh_hours_weeks(d, day_dict)

    print("Annual Schedules EFLH")
    for sch in d.get('Schedule:Year'.lower(), []):
        eflh = analyze_eflh_sch_year(d, sch, week_dict)
        if eflh is not None:
            print(f"{sch[1]}: {eflh:.0f}")


def eflh_days_command(file: list[list[str]], header: bool = False):
    if header:
        print("\t".join(["Schedule", "EFLH"]))

    eflh_days(file)


def eflh_annual(file: list[list[str]], header: bool = False, base_dir: Optional[pathlib.Path] = None):
    rows = annual_fractional_schedule_eflh(tsv2dict(file), base_dir)

    if header:
        print("\t".join(["Schedule", "EFLH"]))

    for name, annual_hours in rows:
        print("\t".join([name, f"{annual_hours:.0f}"]))

day_map = {
    "sunday": 0,
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "": 0 # Default to Sunday
}

NORMAL_DAY_COUNT = 7
ALL_DAY_TYPE_COUNT = 12


def schedule_day_selector_indexes(selector: str) -> list[int]:
    selector = selector.strip().lower().replace(" ", "")

    if "alldays" in selector:
        return list(range(ALL_DAY_TYPE_COUNT))
    elif "weekdays" in selector:
        return [1, 2, 3, 4, 5]
    elif "weekends" in selector or "weekend" in selector:
        return [0, 6]
    elif "allotherdays" in selector:
        return []
    elif "holidays" in selector or "holiday" in selector:
        return [7]
    elif "summerdesignday" in selector:
        return [8]
    elif "winterdesignday" in selector:
        return [9]
    elif "sunday" in selector:
        return [0]
    elif "monday" in selector:
        return [1]
    elif "tuesday" in selector:
        return [2]
    elif "wednesday" in selector:
        return [3]
    elif "thursday" in selector:
        return [4]
    elif "friday" in selector:
        return [5]
    elif "saturday" in selector:
        return [6]
    elif "customday1" in selector:
        return [10]
    elif "customday2" in selector:
        return [11]
    else:
        raise ValueError(f"Unknown schedule day selector '{selector}'.")


def parse_schedule_time_to_minute(time_str: str) -> int:
    time_str = time_str.strip()
    if time_str.lower().startswith("until:"):
        time_str = time_str.split(":", 1)[1].strip()

    parts = time_str.split(":")
    if len(parts) != 2:
        raise ValueError(f"Schedule time '{time_str}' is not HH:MM.")

    hour = int(parts[0])
    minute = int(parts[1])
    if hour == 24 and minute == 0:
        return 1440
    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        raise ValueError(f"Schedule time '{time_str}' is outside the valid day.")
    return hour * 60 + minute


def date_to_leap_day_of_year(month: int, day: int) -> int:
    month_lengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        raise ValueError(f"Month {month} is outside 1..12.")
    if day < 1 or day > month_lengths[month - 1]:
        raise ValueError(f"Day {day} is outside the valid range for month {month}.")
    return sum(month_lengths[:month - 1]) + day


def schedule_timesteps_per_hour(idf_dict: dict[str, list[list[str]]]) -> int:
    timestep = idf_dict.get("timestep", [])
    if len(timestep) == 0 or len(timestep[0]) < 2 or timestep[0][1].strip() == "":
        return 6

    return int(float(timestep[0][1]))


def runperiod_start_day(idf_dict: dict[str, list[list[str]]]) -> int:
    run_periods = idf_dict.get("runperiod", [])
    if len(run_periods) == 0:
        return 0

    for field in run_periods[0][2:]:
        day = field.strip().lower()
        if day in day_map:
            return day_map[day]

    return 0


def expand_minute_values_to_timesteps(minute_values: list[float], interpolate: str, timesteps_per_hour: int) -> list[float]:
    if len(minute_values) != 1440:
        raise ValueError("Minute schedule must contain exactly 1440 values.")
    if 60 % timesteps_per_hour != 0:
        raise ValueError("Timesteps per hour must divide evenly into 60.")

    minutes_per_step = 60 // timesteps_per_hour
    timestep_values = []
    interpolate = interpolate.strip().lower()

    for start in range(0, 1440, minutes_per_step):
        end = start + minutes_per_step
        if interpolate == "average":
            timestep_values.append(sum(minute_values[start:end]) / minutes_per_step)
        else:
            timestep_values.append(minute_values[end - 1])

    return timestep_values


def minute_values_from_until_pairs(pairs: list[tuple[int, float]], interpolate: str) -> list[float]:
    minute_values: list[Optional[float]] = [None] * 1440
    previous_minute = 0
    previous_value: Optional[float] = None
    interpolate = interpolate.strip().lower()

    for until_minute, value in pairs:
        if until_minute <= previous_minute:
            raise ValueError("Schedule until times must be strictly increasing.")

        for minute in range(previous_minute, until_minute):
            if interpolate == "linear" and previous_value is not None:
                fraction = (minute - previous_minute + 1) / (until_minute - previous_minute)
                minute_values[minute] = previous_value + (value - previous_value) * fraction
            else:
                minute_values[minute] = value

        previous_minute = until_minute
        previous_value = value

    if previous_minute != 1440:
        raise ValueError("Schedule day does not extend through 24:00.")

    return [0 if value is None else value for value in minute_values]


def day_schedule_from_until_pairs(name: str, pairs: list[tuple[int, float]], interpolate: str, timesteps_per_hour: int) -> DayScheduleValues:
    minute_values = minute_values_from_until_pairs(pairs, interpolate)
    return DayScheduleValues(name, expand_minute_values_to_timesteps(minute_values, interpolate, timesteps_per_hour))


def build_day_schedules(idf_dict: dict[str, list[list[str]]], timesteps_per_hour: int) -> dict[str, DayScheduleValues]:
    day_schedules: dict[str, DayScheduleValues] = {}

    for schedule in idf_dict.get("schedule:day:hourly", []):
        if len(schedule) < 27:
            continue
        values: list[float] = []
        for value in schedule[3:27]:
            values.extend([float(value)] * timesteps_per_hour)
        day_schedules[schedule[1].strip().lower()] = DayScheduleValues(schedule[1], values)

    for schedule in idf_dict.get("schedule:day:interval", []):
        interpolate = schedule[3].strip() if len(schedule) > 3 and schedule[3].strip() != "" else "No"
        pairs = []
        for index in range(4, len(schedule), 2):
            if index + 1 >= len(schedule):
                break
            pairs.append((parse_schedule_time_to_minute(schedule[index]), float(schedule[index + 1])))
        day_schedules[schedule[1].strip().lower()] = day_schedule_from_until_pairs(schedule[1], pairs, interpolate, timesteps_per_hour)

    for schedule in idf_dict.get("schedule:day:list", []):
        if len(schedule) < 6:
            continue
        interpolate = schedule[3].strip() if schedule[3].strip() != "" else "No"
        minutes_per_item = int(float(schedule[4]))
        if minutes_per_item <= 0 or 60 % minutes_per_item != 0:
            raise ValueError(f"Schedule:Day:List '{schedule[1]}' has invalid Minutes per Item.")
        minute_values = []
        for value in schedule[5:]:
            minute_values.extend([float(value)] * minutes_per_item)
        if len(minute_values) != 1440:
            raise ValueError(f"Schedule:Day:List '{schedule[1]}' does not cover exactly 24 hours.")
        values = expand_minute_values_to_timesteps(minute_values, interpolate, timesteps_per_hour)
        day_schedules[schedule[1].strip().lower()] = DayScheduleValues(schedule[1], values)

    return day_schedules


def build_week_schedules(idf_dict: dict[str, list[list[str]]], day_schedules: dict[str, DayScheduleValues]) -> dict[str, list[Optional[DayScheduleValues]]]:
    week_schedules: dict[str, list[Optional[DayScheduleValues]]] = {}

    for schedule in idf_dict.get("schedule:week:daily", []):
        days: list[Optional[DayScheduleValues]] = []
        for day_name in schedule[2:14]:
            days.append(day_schedules.get(day_name.strip().lower()))
        while len(days) < ALL_DAY_TYPE_COUNT:
            days.append(None)
        week_schedules[schedule[1].strip().lower()] = days

    for schedule in idf_dict.get("schedule:week:compact", []):
        days: list[Optional[DayScheduleValues]] = [None] * ALL_DAY_TYPE_COUNT
        index = 2
        while index + 1 < len(schedule):
            selector = schedule[index]
            day_schedule = day_schedules.get(schedule[index + 1].strip().lower())
            indexes = schedule_day_selector_indexes(selector)
            if "allotherdays" in selector.strip().lower().replace(" ", ""):
                indexes = [i for i, value in enumerate(days) if value is None]
            for day_index in indexes:
                days[day_index] = day_schedule
            index += 2
        week_schedules[schedule[1].strip().lower()] = days

    return week_schedules


def assign_week_schedule_days(
    day_schedules_by_year_day: list[Optional[list[Optional[DayScheduleValues]]]],
    week: list[Optional[DayScheduleValues]],
    start_day: int,
    end_day: int,
):
    if end_day >= start_day:
        ranges = [(start_day, end_day)]
    else:
        ranges = [(start_day, 366), (1, end_day)]

    for start, end in ranges:
        for day in range(start, end + 1):
            day_schedules_by_year_day[day] = week


def finalize_leap_schedule_days(days: list[Optional[list[Optional[DayScheduleValues]]]]):
    if days[60] is None:
        days[60] = days[59]


def build_schedule_year(schedule: list[str], week_schedules: dict[str, list[Optional[DayScheduleValues]]]) -> Optional[list[Optional[list[Optional[DayScheduleValues]]]]]:
    days: list[Optional[list[Optional[DayScheduleValues]]]] = [None] * 367
    index = 3
    while index + 4 < len(schedule):
        week = week_schedules.get(schedule[index].strip().lower())
        if week is None:
            return None
        start_day = date_to_leap_day_of_year(int(schedule[index + 1]), int(schedule[index + 2]))
        end_day = date_to_leap_day_of_year(int(schedule[index + 3]), int(schedule[index + 4]))
        assign_week_schedule_days(days, week, start_day, end_day)
        index += 5

    finalize_leap_schedule_days(days)
    return [week[0:ALL_DAY_TYPE_COUNT] if week is not None else None for week in days]


def build_compact_annual_schedule(schedule: list[str], timesteps_per_hour: int) -> list[Optional[list[Optional[DayScheduleValues]]]]:
    zero_day = DayScheduleValues(f"{schedule[1]} Generated Missing Day", [0.0] * 24 * timesteps_per_hour)
    annual_days: list[Optional[list[Optional[DayScheduleValues]]]] = [None] * 367
    block_start_day = 1
    index = 3

    while index < len(schedule):
        field = schedule[index].strip()
        if not field.lower().startswith("through:"):
            raise ValueError(f"Expected Through field in Schedule:Compact '{schedule[1]}'.")

        through_text = field.split(":", 1)[1].strip()
        month_text, day_text = through_text.split("/")
        block_end_day = date_to_leap_day_of_year(int(month_text), int(day_text))
        week: list[Optional[DayScheduleValues]] = [zero_day] * ALL_DAY_TYPE_COUNT
        index += 1

        while index < len(schedule) and not schedule[index].strip().lower().startswith("through:"):
            for_field = schedule[index].strip()
            if not for_field.lower().startswith("for:"):
                raise ValueError(f"Expected For field in Schedule:Compact '{schedule[1]}'.")
            selector = for_field.split(":", 1)[1].strip()
            indexes = schedule_day_selector_indexes(selector)
            if "allotherdays" in selector.lower().replace(" ", ""):
                indexes = [i for i, value in enumerate(week) if value == zero_day]
            index += 1

            interpolate = "No"
            if index < len(schedule) and schedule[index].strip().lower().startswith("interpolate:"):
                interpolate = schedule[index].split(":", 1)[1].strip()
                index += 1

            pairs = []
            while index < len(schedule) and schedule[index].strip().lower().startswith("until:"):
                until_minute = parse_schedule_time_to_minute(schedule[index])
                if index + 1 >= len(schedule):
                    raise ValueError(f"Missing value after Until field in Schedule:Compact '{schedule[1]}'.")
                pairs.append((until_minute, float(schedule[index + 1])))
                index += 2

            day_name = f"{schedule[1]} Generated Day {block_end_day} {selector}"
            day_schedule = day_schedule_from_until_pairs(day_name, pairs, interpolate, timesteps_per_hour)
            for day_index in indexes:
                week[day_index] = day_schedule

        assign_week_schedule_days(annual_days, week, block_start_day, block_end_day)
        block_start_day = block_end_day + 1

    finalize_leap_schedule_days(annual_days)
    return [week[0:ALL_DAY_TYPE_COUNT] if week is not None else None for week in annual_days]


def annual_schedule_values_are_fractional(schedule: AnnualScheduleValues, start_day_of_week: int, days_in_year: int) -> bool:
    if schedule.constant_value is not None:
        return 0 <= schedule.constant_value <= 1

    day_type = start_day_of_week
    for day_of_year in range(1, days_in_year + 1):
        week = schedule.day_schedules[day_of_year]
        if week is None:
            return False
        day = week[day_type]
        if day is None:
            return False
        for value in day.values:
            if value < 0 or value > 1:
                return False
        day_type = (day_type + 1) % NORMAL_DAY_COUNT
    return True


def annual_schedule_full_load_hours(schedule: AnnualScheduleValues, start_day_of_week: int, days_in_year: int, timesteps_per_hour: int) -> float:
    if schedule.constant_value is not None:
        return days_in_year * 24 * schedule.constant_value

    total = 0.0
    day_type = start_day_of_week
    for day_of_year in range(1, days_in_year + 1):
        week = schedule.day_schedules[day_of_year]
        if week is None:
            raise ValueError(f"Schedule '{schedule.name}' is missing day {day_of_year}.")
        day_schedule = week[day_type]
        if day_schedule is None:
            raise ValueError(f"Schedule '{schedule.name}' is missing day type {day_type}.")
        total += day_schedule.full_load_hours(timesteps_per_hour)
        day_type = (day_type + 1) % NORMAL_DAY_COUNT
    return total


def read_schedule_file_values(schedule: list[str], base_dir: Optional[pathlib.Path], timesteps_per_hour: int) -> Optional[list[Optional[list[Optional[DayScheduleValues]]]]]:
    if base_dir is None or len(schedule) < 10:
        return None

    schedule_file = pathlib.Path(schedule[3])
    if not schedule_file.is_absolute():
        schedule_file = base_dir / schedule_file
    if not schedule_file.exists():
        print(f"Warning: Schedule:File '{schedule[1]}' file not found: {schedule_file}", file=sys.stderr)
        return None

    column_number = int(float(schedule[4]))
    rows_to_skip = int(float(schedule[5]))
    column_separator = schedule[7].strip().lower() if len(schedule) > 7 else "comma"
    interpolate = "Average" if len(schedule) > 8 and schedule[8].strip().lower() == "yes" else "No"
    minutes_per_item = int(float(schedule[9])) if len(schedule) > 9 and schedule[9].strip() != "" else 60

    if column_separator == "tab":
        separator = "\t"
    elif column_separator == "space":
        separator = None
    else:
        separator = ","

    values = []
    with open(schedule_file, "r") as f:
        for _ in range(rows_to_skip):
            next(f, None)
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(separator) if separator is not None else line.split()
            if column_number - 1 < len(parts):
                values.append(float(parts[column_number - 1]))

    items_per_day = 1440 // minutes_per_item
    annual_days: list[Optional[list[Optional[DayScheduleValues]]]] = [None] * 367
    file_day_count = min(366, len(values) // items_per_day)
    for file_day in range(1, file_day_count + 1):
        if file_day_count < 366 and file_day >= 60:
            day = file_day + 1
        else:
            day = file_day

        minute_values = []
        start = (file_day - 1) * items_per_day
        for value in values[start:start + items_per_day]:
            minute_values.extend([value] * minutes_per_item)
        day_schedule = DayScheduleValues(
            f"{schedule[1]} File Day {day}",
            expand_minute_values_to_timesteps(minute_values, interpolate, timesteps_per_hour),
        )
        annual_days[day] = [day_schedule] * ALL_DAY_TYPE_COUNT

    finalize_leap_schedule_days(annual_days)
    return annual_days


def annual_fractional_schedule_eflh(idf_dict: dict[str, list[list[str]]], base_dir: Optional[pathlib.Path] = None) -> list[tuple[str, float]]:
    timesteps_per_hour = schedule_timesteps_per_hour(idf_dict)
    start_day_of_week = runperiod_start_day(idf_dict)
    days_in_year = 365

    day_schedules = build_day_schedules(idf_dict, timesteps_per_hour)
    week_schedules = build_week_schedules(idf_dict, day_schedules)

    annual_schedules: list[AnnualScheduleValues] = []

    for schedule in idf_dict.get("schedule:constant", []):
        if len(schedule) > 3:
            annual_schedules.append(AnnualScheduleValues(schedule[1], schedule[0], [], float(schedule[3])))

    for schedule in idf_dict.get("schedule:year", []):
        days = build_schedule_year(schedule, week_schedules)
        if days is not None:
            annual_schedules.append(AnnualScheduleValues(schedule[1], schedule[0], days))

    for schedule in idf_dict.get("schedule:compact", []):
        days = build_compact_annual_schedule(schedule, timesteps_per_hour)
        annual_schedules.append(AnnualScheduleValues(schedule[1], schedule[0], days))

    for schedule in idf_dict.get("schedule:file", []):
        days = read_schedule_file_values(schedule, base_dir, timesteps_per_hour)
        if days is not None:
            annual_schedules.append(AnnualScheduleValues(schedule[1], schedule[0], days))

    for schedule in idf_dict.get("externalinterface:schedule", []):
        if len(schedule) > 3:
            annual_schedules.append(AnnualScheduleValues(schedule[1], schedule[0], [], float(schedule[3])))

    rows = []
    for schedule in annual_schedules:
        if annual_schedule_values_are_fractional(schedule, start_day_of_week, days_in_year):
            hours = annual_schedule_full_load_hours(schedule, start_day_of_week, days_in_year, timesteps_per_hour)
            rows.append((schedule.name, hours))

    version_sort_by_in_place(rows, lambda row: row[0])
    return rows


def day_of_year_from_month_day(month: int, day: int) -> int:
    if month < 1 or month > 12:
        print("Error: Month must be between 1 and 12.")
        sys.exit(1)

    if day < 1 or day > 31:
        print("Error: Day must be between 1 and 31.")
        sys.exit(1)

    if month == 1:
        return day
    elif month == 2:
        return 31 + day
    elif month == 3:
        return 59 + day
    elif month == 4:
        return 90 + day
    elif month == 5:
        return 120 + day
    elif month == 6:
        return 151 + day
    elif month == 7:
        return 181 + day
    elif month == 8:
        return 212 + day
    elif month == 9:
        return 243 + day
    elif month == 10:
        return 273 + day
    elif month == 11:
        return 304 + day
    else:
        return 334 + day

def month_from_day_of_year(day_of_year: int) -> int:
    if day_of_year < 1 or day_of_year > 365:
        print("Error: Day of year must be between 1 and 365.")
        sys.exit(1)

    if day_of_year <= 31:
        return 1
    elif day_of_year <= 59:
        return 2
    elif day_of_year <= 90:
        return 3
    elif day_of_year <= 120:
        return 4
    elif day_of_year <= 151:
        return 5
    elif day_of_year <= 181:
        return 6
    elif day_of_year <= 212:
        return 7
    elif day_of_year <= 243:
        return 8
    elif day_of_year <= 273:
        return 9
    elif day_of_year <= 304:
        return 10
    elif day_of_year <= 334:
        return 11
    else:
        return 12


def analyze_eflh_sch_year(file_dict, year_schedule: list[str], week_schedules: dict[str, list[float]]) -> Union[None, float]:
    # First determine day of week for first day of year
    run_periods = file_dict['runperiod'.lower()]
    if len(run_periods) == 0:
        print("Error: No RunPeriod object found.")
        sys.exit(1)

    run_period = run_periods[0]
    start_day = run_period[8].lower()
    start_dow_num = day_map[start_day.strip()]

    index = 3

    total_eflh = 0

    while index < len(year_schedule):
        week_sch_name = year_schedule[index]
        start_month = int(year_schedule[index + 1])
        start_day = int(year_schedule[index + 2])
        end_month = int(year_schedule[index + 3])
        end_day = int(year_schedule[index + 4])

        start_day_of_year = day_of_year_from_month_day(start_month, start_day)
        end_day_of_year = day_of_year_from_month_day(end_month, end_day)
        if week_sch_name not in week_schedules:
            return None

        week_sch_data = week_schedules[week_sch_name]

        for i in range(start_day_of_year, end_day_of_year + 1):
            dow = (start_dow_num + i - 1) % 7
            eflh = week_sch_data[dow]
            total_eflh += eflh

        index += 5

    return total_eflh


def def_parse_compact_week(fields: list[str], day_dict: dict[str, float]) -> list[float]:
    # 0, 1  are the type and name
    index = 2

    # initialize length 12 array with Nones
    days: list[Optional[str]] = [ None, None, None, None, None, None, None, None, None, None, None, None, ]
    # Sunday = 0 Monday = 1 Tuesday = 2 Wednesday = 3 Thursday = 4 Friday = 5 Saturday = 6 Holiday = 7 SummerDesignDay = 8 WinterDesignDay = 9 CustomDay1 = 10 CustomDay2 = 11

    while index + 1 < len(fields):
        day_type = fields[index].lower();
        value = fields[index + 1]

        if "alldays" in day_type:
            for i in range(len(days)):
                days[i] = value
        elif "weekdays" in day_type:
            for i in range(1, 6):
                days[i] = value
        elif "weekends" in day_type:
            days[0] = value
            days[6] = value
        elif "holidays" in day_type:
            days[7] = value
        elif "summerdesignday" in day_type:
            days[8] = value
        elif "winterdesignday" in day_type:
            days[9] = value
        elif "sunday" in day_type:
            days[0] = value
        elif "monday" in day_type:
            days[1] = value
        elif "tuesday" in day_type:
            days[2] = value
        elif "wednesday" in day_type:
            days[3] = value
        elif "thursday" in day_type:
            days[4] = value
        elif "friday" in day_type:
            days[5] = value
        elif "saturday" in day_type:
            days[6] = value
        elif "customday1" in day_type:
            days[10] = value
        elif "customday2" in day_type:
            days[11] = value
        elif "allotherdays" in day_type:
            for i in range(len(days)):
                if days[i] is None:
                    days[i] = value
        else:
            raise ValueError(f"Unknown day type '{day_type}' in compact week schedule at index {index}.")

        index += 2

    # Check for any Nones
    for i in range(len(days)):
        if days[i] is None:
            raise ValueError(f"Compact week schedule '{fields[1]}' has None value at index {i} {days}.")

    float_values: list[float] = []

    for d in days:
        if d is not None and d.lower() in day_dict:
            float_values.append(day_dict[d.lower()])
        else:
            raise ValueError(f"Compact week schedule '{fields[1]}' has unknown day '{d}'.")

    return float_values



def eflh_hours_weeks(file_dict: dict[str, list[list[str]]], day_analysis) -> dict[str, list[float]]:
    week_schedules = file_dict.get('schedule:week:daily'.lower(), [])

    week_schedule_dict: dict[str, list[float]] = {}

    for week_schedule in week_schedules:
        valid_fractional_sch = True
        name = week_schedule[1]
        # Just do normal days
        days = [d.lower() for d in week_schedule[2:9]]
        # Days go from Sun to Sat, Holiday, SummerDesignDay, WinterDesignDay, CustomDay1, CustomDay2
        day_items = []
        for day in days:
            if day in day_analysis:
                day_items.append(day_analysis[day])
            else:
                valid_fractional_sch = False
                day_items.append(None)

        if valid_fractional_sch:
            # print(name, f"{eflh_total:.1f}" if eflh_total is not None else "N/A")
            week_schedule_dict[name] = day_items

    compact_week_schedules = file_dict.get('schedule:week:compact'.lower(), [])
    for week_schedule in compact_week_schedules:
        values = def_parse_compact_week(week_schedule, day_analysis)
        name = week_schedule[1]
        week_schedule_dict[name] = values

    return week_schedule_dict


def eflh_days(file: list[list[str]]) -> dict[str, float]:
    d = tsv2dict(file)

    all_schedules = []

    day_schedule_dict = {}

    for sch in d.get('Schedule:Day:Interval'.lower(), []):
        index = 4
        eflh_total = 0
        previous_hour = 0

        valid_fractional_sch = True
        while index + 1 < len(sch):
            time_str = sch[index]
            value_until_time_str = float(sch[index + 1])

            if value_until_time_str < 0 or value_until_time_str > 1:
                valid_fractional_sch = False
                break

            # time_str is like HH:MM
            time_str = time_str.split(':')
            hour = int(time_str[0])
            minute = int(time_str[1])

            curr_hour = hour + minute / 60.0

            decimal_hours = (curr_hour) - previous_hour
            eflh_total += decimal_hours * float(sch[index + 1])

            previous_hour = curr_hour
            index += 2

        if valid_fractional_sch:
            day_schedule_dict[sch[1].lower()] = eflh_total
            fields = [sch[1], f"{eflh_total:.1f}"]
            all_schedules.append(fields)

    for sch in d.get('Schedule:Day:Hourly'.lower(), []):
        index = 3
        valid_fractional_sch = True
        eflh_total = 0
        while index < len(sch):
            value = float(sch[index])
            if value < 0 or value > 1:
                valid_fractional_sch = False
                break
            eflh_total += value
            index += 1

        if valid_fractional_sch:
            day_schedule_dict[sch[1].lower()] = eflh_total
            fields = [sch[1], f"{eflh_total:.1f}"]
            all_schedules.append(fields)

    all_schedules.sort(key=lambda x: x[0])
    for sch in all_schedules:
        print("\t".join([str(x) for x in sch]))

    return day_schedule_dict


def process_day_interval_schedule(schedule: list[str]):
    name = schedule[1]

    # First time index is at 4
    index = 4
    time_values = []

    while index < len(schedule):
        # Time is 'HH:MM'
        time = schedule[index]
        split_time = time.split(':')
        if len(split_time) != 2:
            print("Error: time '{}' is not in HH:MM format. Schedule '{}'".format(time, name))
            sys.exit(1)

        hour_str = split_time[0]
        minute_str = split_time[1]

        hour = int(hour_str)
        minute = int(minute_str)

        time_float = hour + minute / 60.0
        value = float(schedule[index + 1])

        time_values.append((time_float, value))

        index += 2

    return (name, time_values)

def process_day_hourly_schedule(schedule: list[str]):
    name = schedule[1]

    # First time index is at 4 (one based)
    index = 3
    time_values = []

    hour = 1
    while index < len(schedule):
        # Time is 'HH:MM'
        value = float(schedule[index])
        time_values.append((hour, value))
        index += 1
        hour += 1

    return (name, time_values)


def construction_summary(idf_dict: dict):
    # Get all constructions
    constructions = idf_dict.get('construction', [])
    material_dict = {}

    def add_materials(m_dict, materials):
        for material in materials:
            if material[1].lower() in m_dict:
                raise ValueError(f"Material '{material[1]}' already exists.")
            m_dict[material[1].strip().lower()] = material

    # Get all materials
    material_object_types = ['material', 'material:airgap', 'material:nomass', 'windowmaterial:gas', 'windowmaterial:simpleglazingsystem', 'windowmaterial:glazing']

    for obj_type in material_object_types:
        add_materials(material_dict, idf_dict.get(obj_type, []))

    # Get all constructions
    for construction in constructions:
        total_r_value = 0

        # Get all layers
        layers = construction[2:]

        for layer in layers:
            material = material_dict.get(layer.strip().lower())
            if material is None:
                print(f"Error: material '{layer}' not found.")
                print("Possible materials:")
                version_sort(material_dict.keys())
                sys.exit(1)

            if material[0].lower() == 'material':
                thickness_m = float(material[3])
                conductivity_W_per_mK = float(material[4])
                R_value_SI = thickness_m / conductivity_W_per_mK
            elif material[0].lower() == 'material:airgap':
                R_value_SI = float(material[2])
            elif material[0].lower() == 'material:nomass':
                R_value_SI = float(material[3])
            elif material[0].lower() == 'windowmaterial:simpleglazingsystem':
                U_value_SI = float(material[2])
                R_value_SI = 1 / U_value_SI
            elif material[0].lower() == 'windowmaterial:glazing':
                thickness_m = float(material[4])
                conductivity_W_per_mK = float(material[14])
                U_value_SI = 1 / (thickness_m / conductivity_W_per_mK)
                R_value_SI = 1 / U_value_SI
            elif material[0].lower() == 'windowmaterial:gas':
                gas_type = material[2].lower()
                if gas_type == "air":
                    thickness_m = float(material[3])
                    # Has some significant changes with temperature. Choosing something reasonable.
                    # https://www.engineeringtoolbox.com/air-properties-viscosity-conductivity-heat-capacity-d_1509.html
                    conductivity_W_per_mK = 0.0255
                else:
                    print("Error: gas type '{}' not recognized yet.".format(gas_type))
                    sys.exit(1)
                
                R_value_SI = thickness_m / conductivity_W_per_mK
            else:
                print("Error: material type '{}' not recognized.".format(material[0]))
                sys.exit(1)

            R_value_IP = R_value_SI * 5.678263337
            # Add to total
            total_r_value += R_value_IP

        u_value_IP = 1 / total_r_value
        fields = [construction[1], f"{total_r_value:.2f}", f"{u_value_IP:.3f}"]
        print("\t".join([str(x) for x in fields]))


def people_load(idf_dict: dict) -> list[list[str]]:
    # Get all people loads
    people_load_objs = idf_dict.get('people', [])

    all_rows = []

    for people_load in people_load_objs:
        space = people_load[2]
        schedule = people_load[3]

        people_type = people_load[4].strip().lower()

        if people_type == "people":
            people_load_str = f"{people_load[5]} people"
        elif people_type == "people/area":
            people_per_ft2 = float(people_load[6]) / 10.7639
            people_per_1000_ft2 = people_per_ft2 * 1000
            # Flip to ft²/people for consistency
            if people_per_ft2 > 0.000000001:
                ft2_per_person = 1 / people_per_ft2
                people_load_str = f"{ft2_per_person:.1f} ft²/person, {people_per_1000_ft2:.1f} people/1000 ft²"
            else:
                people_load_str = "0 persons"
        elif people_type == "area/person":
            ft2_per_person = 10.7639 * float(people_load[7])
            people_load_str = f"{ft2_per_person:,.0f} ft²/person"
        else:
            print("Error: people type '{}' not recognized.".format(people_type))
            sys.exit(1)

        fields = ["People", space, schedule, people_load_str]
        all_rows.append(fields)

    return all_rows


def lights_load(idf_dict: dict) -> list[list[str]]:
    # Get all light loads
    light_load_objs = idf_dict.get('lights', [])

    all_rows = []
    for light_load in light_load_objs:
        space = light_load[2]
        schedule = light_load[3]
        lighting_type = light_load[4].strip().lower()

        if lighting_type == "lightinglevel":
            light_load_str = f"{light_load[5]} people"
        elif lighting_type == "watts/area":
            watts_per_ft2 = float(light_load[6]) / 10.7639
            light_load_str = f"{watts_per_ft2:.2f} W/ft²"
        elif lighting_type == "watts/person":
            light_load_str = f"{light_load[7]:.2f} W/person"
        else:
            print("Error: people type '{}' not recognized.".format(lighting_type))
            sys.exit(1)

        fields = ["Lights", space, schedule, light_load_str]
        all_rows.append(fields)

    return all_rows

def plug_load(idf_dict: dict):
    # Get all plug loads
    plug_load_objs = idf_dict['electricequipment']

    all_rows = []
    for plug_load in plug_load_objs:
        space = plug_load[2]
        schedule = plug_load[3]
        plug_type = plug_load[4].strip().lower()

        if plug_type == "equipmentlevel":
            watts = float(plug_load[5])

            if watts < 1000:
                plug_load_str = f"{watts:.0f} W"
            elif watts < 1000000:
                plug_load_str = f"{watts / 1000:.1f} kW"
            else:
                plug_load_str = f"{watts / 1000000:.1f} MW"

        elif plug_type == "watts/area":
            watts_per_ft2 = float(plug_load[6]) / 10.7639
            plug_load_str = f"{watts_per_ft2:.2f} W/ft²"
        elif plug_type == "watts/person":
            plug_load_str = f"{float(plug_load[7]):.2f} W/person"
        else:
            print("Error: people type '{}' not recognized.".format(plug_type))
            sys.exit(1)

        fields = ["Plug", space, schedule, plug_load_str]
        all_rows.append(fields)

    return all_rows

def print_tsv_to_stdout(tsv: list[list[str]]):
    # If a tty, print nicely with padding, else to TSV standard
    if sys.stdout.isatty():
        max_col_widths = [0] * len(tsv[0])

        for line in tsv:
            for idx, field in enumerate(line):
                max_col_widths[idx] = max(max_col_widths[idx], len(field))

        for line in tsv:
            for idx, field in enumerate(line):
                print(field.ljust(max_col_widths[idx] + 1), end="")
            print()
    else:
        for line in tsv:
            print("\t".join(line))

def internal_load_summary(idf_dict: dict, header: bool = False):
    people = people_load(idf_dict)
    light = lights_load(idf_dict)
    plug = plug_load(idf_dict)

    all_rows = []
    if header:
        all_rows.append(["Type", "Space", "Schedule", "Load"])
    all_rows.extend(people)
    all_rows.extend(light)
    all_rows.extend(plug)

    print_tsv_to_stdout(all_rows)

def airloops(idf_dict: dict):
    airloops = idf_dict['airloophvac']
    for airloop in airloops:
        name = airloop[1]
        if airloop[4].lower() == "autosize":
            design_supply_air_flow_rate_cfm_str = "Autosize"
        else:
            design_supply_air_flow_rate_m3s = float(airloop[4])
            design_supply_air_flow_rate_cfm = design_supply_air_flow_rate_m3s * 2118.88
            design_supply_air_flow_rate_cfm_str = f"{design_supply_air_flow_rate_cfm:,.0f}"
        fields = [name, design_supply_air_flow_rate_cfm_str]
        print("\t".join([str(x) for x in fields]))


def chillers(idf_dict: dict):
    chillers_reformulated_eir = idf_dict.get('chiller:electric:reformulatedeir', [])
    for chiller in chillers_reformulated_eir:
        name = chiller[1]
        chiller_type = "Reformulated EIR"
        reference_capacity_tons = float(chiller[2]) / 3516.8528
        reference_cop = float(chiller[3])
        reference_kw_per_ton = 3.516 / reference_cop
        reference_chwst_degF = float(chiller[4]) * 1.8 + 32
        reference_cwrt_degF = float(chiller[5]) * 1.8 + 32
        reference_chw_flow_gpm = float(chiller[6]) * 15850.323
        reference_cw_flow_gpm = float(chiller[7]) * 15850.323

        fields = [name, chiller_type, f"{reference_capacity_tons:,.0f}", f"{reference_cop:.2f}", f"{reference_kw_per_ton:.2f}", f"{reference_chwst_degF:.1f}", f"{reference_cwrt_degF:.1f}", f"{reference_chw_flow_gpm:,.0f}", f"{reference_cw_flow_gpm:,.0f}"]
        print("\t".join([str(x) for x in fields]))

    chillers_eir = idf_dict.get('chiller:electric:eir', [])
    for chiller in chillers_eir:
        name = chiller[1]
        chiller_type = "EIR"
        reference_capacity_tons = float(chiller[2]) / 3516.8528
        reference_cop = float(chiller[3])
        reference_kw_per_ton = 3.516 / reference_cop
        reference_chwst_degF = float_str_or_autosize(lambda v: f"{float(v) * 1.8 + 32:.1f}", chiller[4])
        reference_cwst_degF =   float_str_or_autosize(lambda v: f"{float(v) * 1.8 + 32:.1f}", chiller[5])
        reference_chw_flow_gpm = float_str_or_autosize(lambda v: f"{float(v) * 15850.323:,.0f}", chiller[6])
        reference_cw_flow_gpm =  float_str_or_autosize(lambda v: f"{float(v) * 15850.323:,.0f}", chiller[7])

        fields = [name, chiller_type, f"{reference_capacity_tons:,.0f}", f"{reference_cop:.2f}", f"{reference_kw_per_ton:.2f}", f"{reference_chwst_degF}", f"{reference_cwst_degF}", f"{reference_chw_flow_gpm}", f"{reference_cw_flow_gpm}"]
        print("\t".join([str(x) for x in fields]))


def cooling_towers(idf_dict: dict):
    cooling_towers = idf_dict['coolingtower:variablespeed']
    for cooling_tower in cooling_towers:
        name = cooling_tower[1]
        model_type = cooling_tower[4]
        design_wet_bulb_degF = float_str_or_autosize(lambda v: f"{float(v) * 1.8 + 32:.1f}", cooling_tower[6])
        design_approach_degF = float_str_or_autosize(lambda v: f"{float(v) * 1.8:.1f}", cooling_tower[7])
        design_range_degF = float_str_or_autosize(lambda v: f"{float(v) * 1.8:.1f}", cooling_tower[8])
        design_water_flow_gpm = float_str_or_autosize(lambda v: f"{float(v) * 15850.323:,.0f}", cooling_tower[9])
        design_air_flow_cfm = float_str_or_autosize(lambda v: f"{float(v) * 2118.88:,.0f}", cooling_tower[10])
        design_fan_power_hp = float_str_or_autosize(lambda v: f"{float(v) / 745.7:,.0f}", cooling_tower[11])

        fields = [name, model_type, f"{design_wet_bulb_degF}", f"{design_approach_degF}", f"{design_range_degF}", f"{design_water_flow_gpm}", design_air_flow_cfm, design_fan_power_hp]

        print("\t".join([str(x) for x in fields]))


def get_sch_type(schedule_type_limit_name, type_limit_dict):
    type_limit = schedule_type_limit_name.lower()
    if type_limit in type_limit_dict:
        return type_limit_dict[type_limit][5].lower() if len(type_limit_dict[type_limit]) > 5 else "dimensionless"
    else:
        return "dimensionless"

def constant_schedules(idf_dict: dict):
    schedule_type_limits = { stl[1].lower(): stl for stl in idf_dict['scheduletypelimits'] }

    schedules = idf_dict['schedule:constant']

    rows = []
    for schedule in schedules:
        name = schedule[1]

        type_limit = schedule[2].lower()

        if type_limit in schedule_type_limits:
            sch_type = schedule_type_limits[type_limit][5] if len(schedule_type_limits[type_limit]) > 5 else "Unknown"
        else:
            sch_type = "Unknown"

        value = schedule[3]

        if sch_type.lower() == "temperature":
            float_value = float(value) * 1.8 + 32
            value = f"{float_value:.1f}°F"
        elif sch_type.lower() == "deltatemperature":
            float_value = float(value) * 1.8
            value = f"{float_value:.1f}°F"

        fields = [name, value]
        rows.append(fields)

    version_sort_by_in_place(rows, lambda x: x[0])

    for fields in rows:
        print("\t".join([str(x) for x in fields]))


def day_schedules(idf_dict: dict):
    schedule_type_limits = { stl[1].lower(): stl for stl in idf_dict['scheduletypelimits'] }

    out_dict = []

    day_interval_schedules = idf_dict.get('schedule:day:interval', [])
    for schedule in day_interval_schedules:
        name, data = process_day_interval_schedule(schedule)
        interpolate_type = schedule[3].strip().lower()

        if interpolate_type == "":
            interpolate_type = "No"
        out_dict.append({"name": name, "data": data, "interpolate": interpolate_type, "type": get_sch_type(schedule[2], schedule_type_limits)})

    day_hourly_schedules = idf_dict.get('schedule:day:hourly', [])
    for schedule in day_hourly_schedules:
        name, data = process_day_hourly_schedule(schedule)
        out_dict.append({"name": name, "data": data, "interpolate": "No", "type": get_sch_type(schedule[2], schedule_type_limits)})

    return out_dict


def process_schedules(schedule_list, dir_name):
    for schedule in schedule_list:
        name = schedule["name"]
        data = schedule["data"]
        interpolate = schedule["interpolate"]

        sch_type = schedule["type"]
        # TODO: Sanitize name
        mplot_file = f"{name}.mplot"

        dir_path = pathlib.Path(dir_name)

        # Crazy amount of escaping here.
        escaped_name = name.replace("_", "\\\\\\\\_")

        is_zero_to_one = all(0 <= value <= 1 for _, value in data)

        if sch_type == "temperature" or sch_type == "deltatemperature":
            ylabel = "°F"
        else:
            ylabel = "Value"

        with open(dir_path/ mplot_file, 'w') as f:
            f.write("START\n")

            first_val = data[0][1]
            if sch_type == "temperature":
                first_val = first_val * 1.8 + 32
            elif sch_type == "deltatemperature":
                first_val = first_val
            f.write(f"0,{first_val}\n")

            for time, value in data:
                if sch_type == "temperature":
                    value = value * 1.8 + 32
                elif sch_type == "deltatemperature":
                    value = value * 1.8
                f.write(f"{time},{value}\n")
            f.write("END\n")
            if interpolate == "Linear":
                f.write("line\n")
            else:
                f.write("fstep\n")
            f.write(f"g xr 0 24 xtics 0 2 24 xl \"Time of Day\" yl \"{ylabel}\" title \"{escaped_name}\" comma\n")
            if is_zero_to_one:
                f.write("yrange -5/100 1-5/100\n")

def sch_compact(idf_dict: dict):
    schedule_type_limits = { stl[1].lower(): stl for stl in idf_dict['scheduletypelimits'] }

    compact_schedules = idf_dict.get('schedule:compact', [])

    for schedule in compact_schedules:
        name = schedule[1]
        sch_type = get_sch_type(schedule[2], schedule_type_limits)

        print("**" + name + ":**\n")

        i = 3
        while i < len(schedule):
            if "through" in schedule[i].lower():
                print(schedule[i], end="")
                i += 1
            elif "for" in schedule[i].lower():
                print(" " + schedule[i] + "\n")
                i += 1
            elif "until" in schedule[i].lower():
                print("Until Time | Value")
                print("-----------|------")

                while i < len(schedule) and "until" in schedule[i].lower():
                    until = schedule[i]
                    until = until.lower().replace("until:", "").strip()

                    i += 1
                    value = schedule[i]
                    if sch_type == "temperature":
                        float_value = float(value) * 1.8 + 32
                        value = f"{float_value:.1f}°F"
                    elif sch_type == "deltatemperature":
                        float_value = float(value) * 1.8
                        value = f"{float_value:.1f}°F"
                    print(until + "|" + value)
                    i += 1
                print('\n')

            else:
                raise ValueError("Unknown compact schedule type: " + schedule[i])
        print()

def floor_area_from_surface(surface: list[str]) -> float:
    # Start at 12th element
    area = 0
    xy_pairs = []
    for i in range(12, len(surface), 3):
        xy_pairs.append((float(surface[i]), float(surface[i + 1])))

    for i in range(len(xy_pairs)):
        x1, y1 = xy_pairs[i]
        x2, y2 = xy_pairs[(i + 1) % len(xy_pairs)]
        area += x1 * y2 - x2 * y1

    return abs(area) / 2


def surface_area_from_vertices(surface: list[str], first_vertex_index: int) -> float:
    vertices = []
    for i in range(first_vertex_index, len(surface), 3):
        if i + 2 >= len(surface):
            break
        vertices.append((float(surface[i]), float(surface[i + 1]), float(surface[i + 2])))

    if len(vertices) < 3:
        return 0

    x_area = 0
    y_area = 0
    z_area = 0
    for i in range(len(vertices)):
        x1, y1, z1 = vertices[i]
        x2, y2, z2 = vertices[(i + 1) % len(vertices)]
        x_area += y1 * z2 - z1 * y2
        y_area += z1 * x2 - x1 * z2
        z_area += x1 * y2 - y1 * x2

    return math.sqrt(x_area * x_area + y_area * y_area + z_area * z_area) / 2


def surface_boundary_type(outside_boundary_condition: str) -> str:
    boundary_condition = outside_boundary_condition.strip().lower()
    if boundary_condition in ["surface", "zone", "adiabatic"]:
        return "Interior"
    elif boundary_condition.startswith("ground") or boundary_condition in ["outdoors", "othersidecoefficients", "othersideconditionsmodel"]:
        return "Exterior"
    elif boundary_condition == "":
        return "Unknown"
    else:
        return outside_boundary_condition


def surface_area_summary(idf_dict: dict) -> list[list[str]]:
    area_by_type_boundary: dict[tuple[str, str], float] = {}

    def add_area(surface_type: str, boundary_condition: str, area_m2: float):
        key = (surface_type, boundary_condition)
        if key not in area_by_type_boundary:
            area_by_type_boundary[key] = 0
        area_by_type_boundary[key] += area_m2 * 10.7639

    building_surface_by_name = {}
    for surface in idf_dict.get('buildingsurface:detailed', []):
        building_surface_by_name[surface[1].strip().lower()] = surface
        surface_type = surface[2]
        boundary_condition = surface_boundary_type(surface[6])
        add_area(surface_type, boundary_condition, surface_area_from_vertices(surface, 12))

    for surface in idf_dict.get('fenestrationsurface:detailed', []):
        surface_type = surface[2]
        parent_surface = building_surface_by_name.get(surface[4].strip().lower())
        if parent_surface is not None:
            boundary_condition = surface_boundary_type(parent_surface[6])
        else:
            boundary_condition = surface_boundary_type(surface[5])

        multiplier = 1
        if len(surface) > 8 and surface[8].strip() != "":
            multiplier = float(surface[8])
        add_area(surface_type, boundary_condition, surface_area_from_vertices(surface, 10) * multiplier)

    rows = [[surface_type, boundary_condition, area] for (surface_type, boundary_condition), area in area_by_type_boundary.items()]
    rows.sort(key=lambda x: (x[0].lower(), x[1].lower()))
    return rows
    

def analyze_zones(idf_dict: dict):
    idf_zones = idf_dict.get('zone', [])
    # spaces = idf_dict.get('space', [])
    floors = [o for o in idf_dict.get('buildingsurface:detailed', []) if o[2].lower() == "floor"]

    # print(len(floors), file=sys.stderr)
    
    floor_groups = {}
    for f in floors:
        z_name = f[4].lower()
        if z_name not in floor_groups:
            floor_groups[z_name] = []
        floor_groups[z_name].append(f)

    zones = []
    for zone in idf_zones:
        area = 0
        for floor in floor_groups.get(zone[1].lower(), []):
            area += floor_area_from_surface(floor)

        # m2 to ft2
        area = area * 10.7639
        zones.append([zone[1], area])

    zones.sort()
    return zones


def analyze_spaces(idf_dict: dict):
    idf_zones = idf_dict.get('zone', [])
    all_zone_names = {z[1].lower() for z in idf_zones}

    spaces = idf_dict.get('space', [])

    space_name_map = {s[1].lower().strip(): s[1] for s in spaces} # Just here to get back the original casing from the file instead of all lowercase

    space_dict = { s[1].lower().strip(): s for s in spaces }   
    floors = [o for o in idf_dict.get('buildingsurface:detailed', []) if o[2].lower() == "floor"]

    # print(len(floors), file=sys.stderr)
    # Mapping from floor surface to 
    floor_groups = {}
    for f in floors:
        z_name = f[4].lower()
        s_name = f[5].lower()
        if s_name.strip() == "":
            s_name = z_name

        if s_name not in floor_groups:
            floor_groups[s_name] = []
        floor_groups[s_name].append(f)

    spaces = []
    for s in floor_groups:
        area = 0
        for floor in floor_groups[s]:
            area += floor_area_from_surface(floor)

        # m2 to ft2
        area = area * 10.7639
        space_type = space_dict.get(s, "General")[6]
        spaces.append([space_name_map[s], area, space_type])

    spaces.sort()
    return spaces

def main():
    filename = None
    command = None
    idx = 1
    header = False

    dir_name = None

    while idx < len(sys.argv):
        if sys.argv[idx] == '-h' or sys.argv[idx] == '--help':
            print("Usage: idf.py COMMAND [filename]")
            print("Commands:")
            print("  eflh: Print the equivalent full load hours of fractional schedules.")
            print("  eflh_days: Print the equivalent full load hours of fractional day schedules.")
            print("  eflh_annual: Print the equivalent full load hours of all annual fractional schedules.")
            print("  eflh_all: Alias for eflh_annual.")
            print("  construction: Print the R-value and U-value of constructions.")
            print("  int_loads: Print internal loads.")
            print("  airloops: Print air loop design flow rates.")
            print("  chillers: Print chiller design data.")
            print("  cooling_towers: Print cooling tower design data.")
            print("  const_sch: Print constant schedules.")
            print("  day_sch: Print day schedules.")
            print("  sch_process: Process day schedules.")
            print("  sch_compact: Print compact schedules.")
            print("  surface_areas: Print gross surface area grouped by surface type and boundary condition.")
            print("  zones: Print zone details.")
            print("  spaces: Print space details.")
            print("Options:")
            print("  --header: Print a header row.")
            print("  --dir DIR: Directory for sch_process.")

            sys.exit(0)
        elif sys.argv[idx] == '--header':
            header = True
        elif sys.argv[idx] == 'eflh':
            command = "eflh"
        elif sys.argv[idx] == 'eflh_days':
            command = "eflh_days"
        elif sys.argv[idx] == 'eflh_annual':
            command = "eflh_annual"
        elif sys.argv[idx] == 'eflh_all':
            command = "eflh_annual"
        elif sys.argv[idx] == 'construction':
            command = "construction"
        elif sys.argv[idx] == 'int_loads':
            command = "int_loads"
        elif sys.argv[idx] == 'airloops':
            command = "airloops"
        elif sys.argv[idx] == 'chillers':
            command = "chillers"
        elif sys.argv[idx] == 'cooling_towers':
            command = "cooling_towers"
        elif sys.argv[idx] == 'const_sch':
            command = "const_sch"
        elif sys.argv[idx] == "day_sch":
            command = "day_sch"
        elif sys.argv[idx]  == "sch_process":
            command = "sch_process"
        elif sys.argv[idx] == "sch_compact":
            command = "sch_compact"
        elif sys.argv[idx] == "surface_areas":
            command = "surface_areas"
        elif sys.argv[idx] == "zones":
            command = "zones"
        elif sys.argv[idx] == "spaces":
            command = "spaces"
        elif sys.argv[idx] == "--dir":
            idx += 1
            try:
                dir_name = pathlib.Path(sys.argv[idx])
            except IndexError:
                print("Error: --dir requires an argument.")
                sys.exit(1)

        elif sys.argv[idx].startswith('--'):
            print("Error: unknown option '{}'.".format(sys.argv[idx]))
            sys.exit(1)
        else:
            if command is None:
                print(f"Unknown command `{sys.argv[idx]}`")
                sys.exit(1)

            filename = sys.argv[idx]
            if idx + 1 < len(sys.argv):
                print("Error: too many arguments.")
                sys.exit(1)

        idx += 1


    # If argument, use that as filename, otherwise read from stdin
    if filename is None or filename == '-':
        file = sys.stdin
    else:
        file = open(filename, 'r')

    if command == "eflh":
        contents = idf2tsv(file)
        eflh(contents)
    elif command == "eflh_days":
        contents = idf2tsv(file)
        eflh_days_command(contents, header)
    elif command == "eflh_annual":
        contents = idf2tsv(file)
        base_dir = pathlib.Path(filename).resolve().parent if filename is not None and filename != '-' else None
        eflh_annual(contents, header, base_dir)
    elif command == "construction":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        if header:
            print("\t".join(["Construction", "R-Value (ft²·°F·hr/Btu)", "U-Value (Btu/hr·ft²·°F)"]))
        construction_summary(idf_dict)
    elif command == "int_loads":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        internal_load_summary(idf_dict, header)
    elif command == "airloops":
        if header:
            print("\t".join(["Name", "Design Supply Air Flow Rate (CFM)"]))
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        airloops(idf_dict)
    elif command == "chillers":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        if header:
            if 'chiller:electric:reformulatedeir' in idf_dict and 'chiller:electric:eir' in idf_dict:
                print("Multiple chiller types not implemented yet.", file=sys.stderr)
                sys.exit(1)
            elif 'chiller:electric:reformulatedeir' in idf_dict:
                print("\t".join(["Name", "Type", "Design Capacity (Tons)", "Design COP", "Design kW/Ton", "Design CHWST (°F)", "Design CWRT (°F)", "Design CHW Flow (GPM)", "Design CW Flow (GPM)"]))
            elif 'chiller:electric:eir' in idf_dict:
                print("\t".join(["Name", "Type", "Design Capacity (Tons)", "Design COP", "Design kW/Ton", "Design CHWST (°F)", "Design CWST (°F)", "Design CHW Flow (GPM)", "Design CW Flow (GPM)"]))
            else:
                print("No chillers found of types implemented.", file=sys.stderr)
                sys.exit(1)

        chillers(idf_dict)
    elif command == "cooling_towers":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        if header:
            print("\t".join(["Name", "Model Type", "Design Wet Bulb (°F)", "Design Approach (°F)", "Design Range (°F)", "Design Water Flow (GPM)", "Design Air Flow (CFM)", "Design Fan Power (HP)"]))
        cooling_towers(idf_dict)
    elif command == "const_sch":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        if header:
            print("\t".join(["Schedule Name", "Value"]))
        constant_schedules(idf_dict)
    elif command == "day_sch":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        out_dict = day_schedules(idf_dict)
        print(json.dumps(out_dict, indent=2))

    elif command == "sch_process":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        if dir_name is None:
            print("Error: --dir is required for sch_process.")
            sys.exit(1)
        sch_list = day_schedules(idf_dict)
        process_schedules(sch_list, dir_name)

    elif command == "sch_compact":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        sch_compact(idf_dict)

    elif command == "surface_areas":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        rows = surface_area_summary(idf_dict)

        if header:
            print("\t".join(["Surface Type", "Boundary Condition", "Total Area (ft²)"]))

        for row in rows:
            print("\t".join([row[0], row[1], f"{row[2]:.0f}"]))

    elif command == "zones":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        zones = analyze_zones(idf_dict)

        if header:
            print("\t".join(["Zone", "Area (ft²)"]))

        for zone in zones:
            print("\t".join([str(x) for x in zone]))

    elif command == "spaces":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        spaces = analyze_spaces(idf_dict)

        if header:
            print("\t".join(["Space", "Area (ft²)", "Space Type"]))

        for space in spaces:
            fields = [space[0], f"{space[1]:.0f}", space[2]]
            print("\t".join(fields))

    elif command == "html":
        pass

    else:
        print("Command {} not recognized/implemented.".format(command))


if __name__ == "__main__":
    main()
