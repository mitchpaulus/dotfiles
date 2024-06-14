#!/usr/bin/python3
import sys
from typing import List, Iterable
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

    for sch in d['Schedule:Year'.lower()]:
        if sch[2].lower() == 'fractional':
            print(sch[1])


def eflh_days(file: list[list[str]]):
    d = tsv2dict(file)

    all_schedules = []
    for sch in d['Schedule:Day:Interval'.lower()]:
        if sch[2].lower() == 'fractional':
            index = 4
            eflh_total = 0
            previous_hour = 0

            while index + 1 < len(sch):
                time_str = sch[index]
                # time_str is like HH:MM
                time_str = time_str.split(':')
                hour = int(time_str[0])
                minute = int(time_str[1])

                curr_hour = hour + minute / 60.0

                decimal_hours = (curr_hour) - previous_hour
                eflh_total += decimal_hours * float(sch[index + 1])

                previous_hour = curr_hour
                index += 2

            fields = [sch[1], eflh_total]
            all_schedules.append(fields)

    all_schedules.sort(key=lambda x: x[0])
    for sch in all_schedules:
        print("\t".join([str(x) for x in sch]))


def process_day_interval_schedule(schedule: list[str]):
    name = schedule[1]

    # First time index is at 4
    index = 4
    time_values = []

    while index < len(schedule):
        # Time is 'HH:MM'
        time = schedule[index]
        split_time = time.split(':')
        hour_str = split_time[1]
        minute_str = split_time[2]

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
    constructions = idf_dict['construction']

    # Get all materials
    materials = idf_dict['material']

    air_gaps = idf_dict['material:airgap']
    no_mass = idf_dict['material:nomass']

    window_simple_glazing_systems = idf_dict['windowmaterial:simpleglazingsystem']

    # Get all constructions
    for construction in constructions:
        total_r_value = 0

        # Get all layers
        layers = construction[2:]

        for layer in layers:
            # Get the material
            for m in materials:
                if m[1].lower() == layer.strip().lower():
                    material = m
                    break
            else:
                for m in air_gaps:
                    if m[1].lower() == layer.strip().lower():
                        material = m
                        break
                else:
                    for m in no_mass:
                        if m[1].lower() == layer.strip().lower():
                            material = m
                            break
                    else:
                        for m in window_simple_glazing_systems:
                            if m[1].lower() == layer.strip().lower():
                                material = m
                                break
                        else:
                            print("Error: material '{}' not found.".format(layer))
                            print("Possible materials:")
                            version_sort(materials)

                            for m in materials:
                                print("\t{}".format(m[1]))

                            sys.exit(1)

            # material = materials[layer[0].lower()]

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
            else:
                print("Error: material type '{}' not recognized.".format(material[0]))
                sys.exit(1)

            R_value_IP = R_value_SI * 5.678263337
            # Add to total
            total_r_value += R_value_IP

        u_value_IP = 1 / total_r_value
        fields = [construction[1], f"{total_r_value:.2f}", f"{u_value_IP:.2f}"]
        print("\t".join([str(x) for x in fields]))


def people_load(idf_dict: dict):
    # Get all people loads
    people_load_objs = idf_dict['people']

    for people_load in people_load_objs:
        space = people_load[2]
        schedule = people_load[3]

        people_type = people_load[4].strip().lower()

        if people_type == "people":
            people_load_str = f"{people_load[5]:,.0f} people"
        elif people_type == "people/area":
            people_per_ft2 = float(people_load[6]) / 10.7639
            people_load_str = f"{people_per_ft2:.1f} people/ft²"
        elif people_type == "area/person":
            ft2_per_person = 10.7639 * float(people_load[7])
            people_load_str = f"{ft2_per_person:,.0f} ft²/person"
        else:
            print("Error: people type '{}' not recognized.".format(people_type))
            sys.exit(1)

        fields = ["People", space, schedule, people_load_str]

        print("\t".join([str(x) for x in fields]))


def lights_load(idf_dict: dict):
    # Get all light loads
    light_load_objs = idf_dict['lights']

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

        print("\t".join([str(x) for x in fields]))

def plug_load(idf_dict: dict):
    # Get all plug loads
    plug_load_objs = idf_dict['electricequipment']

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

        print("\t".join([str(x) for x in fields]))

def internal_load_summary(idf_dict: dict):
    people_load(idf_dict)
    lights_load(idf_dict)
    plug_load(idf_dict)

def airloops(idf_dict: dict):
    airloops = idf_dict['airloophvac']
    for airloop in airloops:
        name = airloop[1]
        design_supply_air_flow_rate_m3s = float(airloop[4])
        design_supply_air_flow_rate_cfm = design_supply_air_flow_rate_m3s * 2118.88
        fields = [name, f"{design_supply_air_flow_rate_cfm:,.0f}"]
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
            f.write(f"0,{data[0][1]}\n")
            for time, value in data:
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


def main():
    filename = None
    command = None
    idx = 1
    header = False

    dir_name = None

    while idx < len(sys.argv):
        if sys.argv[idx] == '-h' or sys.argv[idx] == '--help':
            print("Usage: idf.py [filename]")
            sys.exit(0)
        elif sys.argv[idx] == '--header':
            header = True
        elif sys.argv[idx] == 'elfh':
            command = "elfh"
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

    if command == "elfh":
        contents = idf2tsv(file)
        eflh(contents)
    elif command == "construction":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        construction_summary(idf_dict)
    elif command == "int_loads":
        contents = idf2tsv(file)
        idf_dict = tsv2dict(contents)
        if header:
            print("\t".join(["Type", "Space", "Schedule", "Load"]))
        internal_load_summary(idf_dict)
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

    else:
        print("Command {} not recognized/implemented.".format(command))


if __name__ == "__main__":
    main()
