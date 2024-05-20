#!/usr/bin/env python3

import sys

def parse_day_interval(split_line: list[str]):
    name = split_line[1]

    field = 5

    time_values = []

    while field <= len(split_line):
        # Time is 'HH:MM'
        time = split_line[field]
        split_time = time.split(':')
        hour_str = split_time[0]
        minute_str = split_time[1]

        hour = int(hour_str)
        minute = int(minute_str)

        time_int = hour * 60 + minute
        value = split_line[field + 1]

        time_values.append((time_int, value))

        field += 2

    return (name, time_values)


def interpolate(time_values, schedule_values):
    time_value_index = 0
    schedule_value_index = 0

    output_values = []

    while time_value_index < len(time_values):
        time_value = time_values[time_value_index]
        schedule_value = schedule_values[schedule_value_index]

        if time_value[0] <= schedule_value[0]:
            output_values.append(schedule_value[1])
            time_value_index += 1
        else:
            schedule_value_index += 1

    return output_values


schedules = []

for line in sys.stdin:
    split = line.split('\t')

    if split[0].lower() == "schedule:day:interval":
        schedule = parse_day_interval(split)
        schedules.append(schedule)


unique_times = set()
for schedule in schedules:
    for time_value in schedule[1]:
        unique_times.add(time_value[0])

unique_times.add(0)

sorted_times = sorted(unique_times)
sorted_names = sorted([schedule[0] for schedule in schedules])

print("Time", end="")
print("\t".join(sorted_names))

for schedule in schedules:
    time_values = schedule[1]
    interpolated_values = interpolate(sorted_times, time_values)
    schedule[1] = interpolated_values

name_map = { schedule[0]: schedule[1] for schedule in schedules }

for time in sorted_times:
    print(time, end="")
    for name in sorted_names:
        value = name_map[name]
        for time_value in value:
            if time_value[0] == time:
                print("\t" + time_value[1], end="")
