#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Purpose of this script is to add in 'Binning' tabular data.
# Common options for configuraiton are:

# 1. Bin size (default 1)
# 2. Include all rows (default True)
# 3. Fill value for blank
# 4. Count or Frequency for bin (default Count)
# 5. Delim for data (default smart)
# 6. Column selection (default 1)
# 7. X style (center of bin, left/right edge of bin)

import sys
import csv

def main():
    idx = 1
    bin_size = 1
    blank_text = ""
    remove_blank = False
    filename = None
    column_one_based = 1
    trend_name = None

    while idx < len(sys.argv):
        if sys.argv[idx] == '--bin' or sys.argv[idx] == '-b':
            idx += 1
            try:
                bin_size = float(sys.argv[idx])
            except ValueError:
                print(f"Invalid bin size '{sys.argv[idx]}'")
                return
            except IndexError:
                print("Missing bin size")
                return
            idx += 1
        elif sys.argv[idx] == '-h' or sys.argv[idx] == '--help':
            print("Usage: bindata.py OPTIONS <filename>")
            print("Options:")
            print("  -b, --bin <size>   Size of bin (default 1)")
            print("  -h, --help         Display this help message")
            return
        elif sys.argv[idx] == "-m" or sys.argv[idx] == "--missing":
            idx += 1
            if idx >= len(sys.argv):
                print("Missing missing value text")
                return
            blank_text = sys.argv[idx]
            idx += 1
        elif sys.argv[idx] == "-r" or sys.argv[idx] == "--remove":
            remove_blank = True
            idx += 1
        elif sys.argv[idx] == "-c" or sys.argv[idx] == "--column":
            idx += 1
            try:
                column_one_based = int(sys.argv[idx])
            except ValueError:
                print(f"Invalid column number '{sys.argv[idx]}'")
                return
            except IndexError:
                print("Missing column number")
                return
            idx += 1
            if column_one_based < 1:
                print("Column number must be greater than 0")
                return
        elif sys.argv[idx] == "-n" or sys.argv[idx] == "--name":
            idx += 1
            if idx >= len(sys.argv):
                print("Missing trend name")
                return
            trend_name = sys.argv[idx]
            idx += 1

        elif sys.argv[idx].startswith('-'):
            print(f"Unknown option '{sys.argv[idx]}'")
            return
        else:
            filename = sys.argv[idx]
            idx += 1
            if idx < len(sys.argv):
                print(f"Unknown option '{sys.argv[idx]}'")
                return

    bin_data(filename, bin_size, blank_text, remove_blank, column_one_based, trend_name)


def bin_data(data_file, bin_size, blank_text, keep_blank, column_one_based, trend_name):
    if data_file is None:
        # Read from stdin
        file = sys.stdin
    else:
        try:
            file = open(data_file, 'r')
        except FileNotFoundError:
            print(f"File '{data_file}' not found")
            return

    # Read first line to figure out file type.
    contents = file.read().splitlines()

    if "\t" in contents[0]:
        delim = "\t"
    elif "," in contents[0]:
        delim = ","
    else:
        delim = "\t"

    bin_counts = {}

    if delim == ",":
        reader = csv.reader(contents)

        if trend_name is not None:
            first_row = next(reader)
            # Try to find the trend name in the first row
            for idx, col in enumerate(first_row):
                if col == trend_name:
                    column_one_based = idx + 1
                    break
            else:
                print(f"Trend name '{trend_name}' not found in first row")
                return

        for row_num, row in enumerate(reader):
            try:
                data = float(row[column_one_based - 1])
            except ValueError:
                continue
            except IndexError:
                raise ValueError(f"Column {column_one_based} not found in row {row_num + 1}")

            bin_num = data // bin_size
            if bin_num not in bin_counts:
                bin_counts[bin_num] = 0
            bin_counts[bin_num] += 1
    else:

        if trend_name is not None:
            first_row = contents[0].split(delim)
            # Try to find the trend name in the first row
            for idx, col in enumerate(first_row):
                if col == trend_name:
                    column_one_based = idx + 1
                    break
            else:
                print(f"Trend name '{trend_name}' not found in first row")
                return

        for row_num, row in enumerate(contents):
            try:
                data = float(row.split(delim)[column_one_based - 1])
            except ValueError:
                continue
            except IndexError:
                raise ValueError(f"Column {column_one_based} not found in row {row_num + 1}")

            bin_num = data // bin_size
            if bin_num not in bin_counts:
                bin_counts[bin_num] = 0
            bin_counts[bin_num] += 1


    bin_nums = sorted(bin_counts.keys())
    min_bin = min(bin_nums)
    max_bin = max(bin_nums)
    curr_bin = min_bin
    while curr_bin <= max_bin:
        center_of_bin = curr_bin * bin_size + bin_size / 2
        bin_count = bin_counts.get(curr_bin, 0)
        print(f"{center_of_bin}\t{bin_count}")
        curr_bin += 1


if __name__ == "__main__":
    main()
