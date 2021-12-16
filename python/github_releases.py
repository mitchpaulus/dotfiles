#!/usr/bin/python3

# The purpose of this script is to parse the JSON output from the GitHub API related to the latest release.
# The script prints out the URL to the asset and the file name of the asset.

import sys
import json
import re

# Read in standard input as JSON and parse it
def read_json():
    return json.loads(sys.stdin.read())

def usage():
    print("github_releases.py")
    print("USAGE:")
    print(" latest_release owner repo | python3 github_releases.py regex")

if __name__ == "__main__":
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-h" or sys.argv[i] == "--help":
            usage()
            sys.exit(0)
        i += 1

    release = read_json()
    assets = release["assets"]

    # First argument is the regex to match against the asset name
    regex = sys.argv[1]

    for asset in assets:
        if re.search(regex, asset["name"]):
            print(asset["browser_download_url"])
            print(asset["name"])
            sys.exit(0)
