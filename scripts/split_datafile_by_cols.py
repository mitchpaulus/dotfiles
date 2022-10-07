#!/usr/bin/env python3

# Once in a while, we get trend data files of the form:
# DateTime,Trend 1,DateTime,Trend 2,DateTime,Trend 3,...
# This script splits them into separate files, one for each trend.
# Assume the file we get has been converted to TSV.
import sys
import os
import mputils
from typing import Dict
import hashlib

if len(sys.argv) < 2:
    print("Usage: split_datafile_by_cols.py <datafile> <outputdir>")
    sys.exit(1)

datafile = sys.argv[1]

# If outputdir is not specified, use the current directory.
outputdir = os.getcwd()
if len(sys.argv) > 2:
    outputdir = sys.argv[2]

rows = mputils.read_tsv(datafile)

if len(rows) < 2:
    print(f"Data file '{datafile}' must have at least two lines")
    sys.exit(1)

header = rows[0]

# Check that we have even number of columns
if len(header) % 2 != 0:
    print(f"Data file '{datafile}' must have even number of columns")
    sys.exit(1)

trend_names = header[1::2]
unique_trend_names = set(trend_names)
# Build mapping from col index to trend name
col_to_trend = {}
for i in range(len(trend_names)):
    col_to_trend[i * 2 + 1] = trend_names[i]

all_data: Dict[str, Dict[str, str]] = {}
for trend_name in unique_trend_names:
    all_data[trend_name] = {}

for row in rows[1:]:
    for col in range(len(row)):
        if col % 2 == 0:
            continue
        if col not in col_to_trend:
            continue
        if row[col - 1].strip() == "":
            continue
        if row[col].strip() == "":
            continue

        trend_name = col_to_trend[col]
        all_data[trend_name][row[col - 1]] = row[col]

# Create a new file for each trend
for trend_name in unique_trend_names:
    trend_data = all_data[trend_name]
    sanitized_trend_name = mputils.sanitize_fn(trend_name)
    trend_file = os.path.join(outputdir, f"{sanitized_trend_name}.tsv")

    # create outputdir if it doesn't exist
    os.makedirs(outputdir, exist_ok=True)

    try:
        with open(trend_file, "x") as f:
            f.write(f"DateTime\t{trend_name}\n")
            for dt in mputils.version_sort(trend_data.keys()):
                f.write(f"{dt}\t{trend_data[dt]}\n")
    except FileExistsError:
        # Get SHA-256 of the data in the file, use that as the filename, then overwrite the file
        sha256 = hashlib.sha256()
        with open(trend_file, "rb") as f:
            sha256.update(f.read())
        sha256_hex = sha256.hexdigest()
        trend_file = os.path.join(outputdir, f"{sanitized_trend_name}-{sha256_hex}.tsv")
        with open(trend_file, "w") as f:
            f.write(f"DateTime\t{trend_name}\n")
            for dt in mputils.version_sort(trend_data.keys()):
                f.write(f"{dt}\t{trend_data[dt]}\n")
