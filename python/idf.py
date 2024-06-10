#!/usr/bin/python3
import sys
from typing import List, Iterable

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


def tsv2dict(file: list[list[str]]) -> dict:
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


def main():
    filename = None
    command = None
    idx = 1

    while idx < len(sys.argv):
        if sys.argv[idx] == '-h' or sys.argv[idx] == '--help':
            print("Usage: idf.py [filename]")
            sys.exit(0)
        elif sys.argv[idx] == 'elfh':
            command = "elfh"
        elif sys.argv[idx] == 'construction':
            command = "construction"
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
    else:
        print("Command {} not recognized.".format(command))


if __name__ == "__main__":
    main()
