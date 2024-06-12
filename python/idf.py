#!/usr/bin/python3
import sys
from typing import List, Iterable
import math

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


def main():
    filename = None
    command = None
    idx = 1
    header = False

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
    else:
        print("Command {} not recognized.".format(command))


if __name__ == "__main__":
    main()
