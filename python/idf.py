#!/usr/bin/python3

import sys

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


def main():
    # If argument, use that as filename, otherwise read from stdin
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        file = open(filename, 'r')
    else:
        file = sys.stdin

    contents = idf2tsv(file)
    eflh_days(contents)


if __name__ == "__main__":
    main()
