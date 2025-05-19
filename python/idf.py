#!/usr/bin/python3
import sys
from typing import List, Iterable, Union, Optional
import math
import json
import pathlib

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
            tokens.append(s[start:idx])

    return tokens

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


def eflh(file: list[list[str]]):
    d = tsv2dict(file)

    print("Day Schedules EFLH")
    day_dict = eflh_days(file)
    print()

    week_dict = eflh_hours_weeks(d, day_dict)

    print("Annual Schedules EFLH")
    for sch in d['Schedule:Year'.lower()]:
        eflh = analyze_eflh_sch_year(d, sch, week_dict)
        if eflh is not None:
            print(f"{sch[1]}: {eflh:.0f}")

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
    week_schedules = file_dict['schedule:week:daily'.lower()]

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

    compact_week_schedules = file_dict['schedule:week:compact'.lower()]
    for week_schedule in compact_week_schedules:
        values = def_parse_compact_week(week_schedule, day_analysis)
        name = week_schedule[1]
        week_schedule_dict[name] = values

    return week_schedule_dict


def eflh_days(file: list[list[str]]) -> dict[str, float]:
    d = tsv2dict(file)

    all_schedules = []

    day_schedule_dict = {}

    for sch in d['Schedule:Day:Interval'.lower()]:
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

    # First time index is at 4
    index = 4
    time_values = []

    hour = 1
    while index < len(schedule):
        # Time is 'HH:MM'
        value = float(schedule[index])
        time_values.append((hour, value))
        index += 1

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
            print("  construction: Print the R-value and U-value of constructions.")
            print("  int_loads: Print internal loads.")
            print("  airloops: Print air loop design flow rates.")
            print("  chillers: Print chiller design data.")
            print("  cooling_towers: Print cooling tower design data.")
            print("  const_sch: Print constant schedules.")
            print("  day_sch: Print day schedules.")
            print("  sch_process: Process day schedules.")
            print("  sch_compact: Print compact schedules.")
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
                print("Error: no command specified.")
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
