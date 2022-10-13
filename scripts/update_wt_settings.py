#!/usr/bin/env python3

import json
import os.path
from typing import Union, List
import sys

# Look for locations of the settings files
username = "mpaulus"

# Terminal stable
# %LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
# Terminal preview
# %LOCALAPPDATA%\Packages\Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe\LocalState\settings.json

# Get the settings file. We are running this file through WSL
# so we need to use the Unix path
settings_file = "/mnt/c/Users/" + username + "/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json"
preview_settings_file = "/mnt/c/Users/" + username + "/AppData/Local/Packages/Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe/LocalState/settings.json"

# print whether the files exist:
print("Settings file exists: " + str(os.path.exists(settings_file)))
print("Preview settings file exists: " + str(os.path.exists(preview_settings_file)))

def current_key_set(action):
    if "keys" in action:
        keys = action["keys"]
        if isinstance(keys, str):
            keys = set([keys])
        return set(keys)
    else:
        return set([])

def update_file(s):
    s["copyOnSelect"] = False
    s["copyFormatting"] = False
    s["trimBlockSelection"] = True
    s["trimPaste"] = True

    # Wipe the existing actions, put my own
    s["actions"] = [
        { "command": "unbound", "keys": "ctrl+shift+w" },
        { "command": "unbound", "keys":  "alt+down" },
        { "command": "unbound", "keys":  "alt+left" },
        { "command": "unbound", "keys":   "alt+right" },
        { "command": "unbound", "keys":    "alt+up" },
        { "command": "newTab", "keys": "alt+enter" },
        { "command": { "action": "splitPane", "split": "auto", "splitMode": "duplicate" }, "keys": "alt+;" },
        { "command": { "action": "splitPane", "split": "horizontal", "splitMode": "duplicate" }, "keys": "alt+-" },
        { "command": { "action": "moveFocus", "direction": "down" }, "keys": "alt+j" },
        { "command": { "action": "moveFocus", "direction": "left" }, "keys": "alt+h" },
        { "command": { "action": "moveFocus", "direction": "right" }, "keys": "alt+l" },
        { "command": { "action": "moveFocus", "direction": "up" }, "keys": "alt+k" },
        { "command": { "action": "moveFocus", "direction": "previous" }, "keys": "ctrl+alt+left" },
        { "command": "nextTab", "keys": "alt+n" },
        { "command": "prevTab", "keys": "alt+p" },
        { "command": "closePane", "keys": "alt+o" },
    ]

    color_schemes = [
        {
            "background" : "#2E3440",
            "black" : "#2E3440",
            "blue" : "#D8DEE9",
            "brightBlack" : "#88C0D0",
            "brightBlue" : "#D08770",
            "brightCyan" : "#A3BE8C",
            "brightGreen" : "#5E81AC",
            "brightPurple" : "#EBCB8B",
            "brightRed" : "#81A1C1",
            "brightWhite" : "#B48EAD",
            "brightYellow" : "#BF616A",
            "cyan" : "#ECEFF4",
            "foreground" : "#D8DEE9",
            "green" : "#434C5E",
            "name" : "Nord",
            "purple" : "#E5E9F0",
            "red" : "#3B4252",
            "white" : "#8FBCBB",
            "yellow" : "#4C566A"
        },
        {
            "background": "#222222",
            "black": "#0C0C0C",
            "blue": "#0090FF",
            "brightBlack": "#767676",
            "brightBlue": "#3B78FF",
            "brightCyan": "#61D6D6",
            "brightGreen": "#16C60C",
            "brightPurple": "#B4009E",
            "brightRed": "#E74856",
            "brightWhite": "#F2F2F2",
            "brightYellow": "#F9F1A5",
            "cyan": "#3A96DD",
            "foreground": "#F2F2F2",
            "green": "#13A10E",
            "name": "Mitch",
            "purple": "#FDAADC",
            "red": "#ff7f7f",
            "white": "#CCCCCC",
            "yellow": "#e0e022"
        },
        {
            "name": "Chalk",
            "black": "#7d8b8f",
            "red": "#b23a52",
            "green": "#789b6a",
            "yellow": "#b9ac4a",
            "blue": "#2a7fac",
            "purple": "#bd4f5a",
            "cyan": "#44a799",
            "white": "#d2d8d9",
            "brightBlack": "#888888",
            "brightRed": "#f24840",
            "brightGreen": "#80c470",
            "brightYellow": "#ffeb62",
            "brightBlue": "#4196ff",
            "brightPurple": "#fc5275",
            "brightCyan": "#53cdbd",
            "brightWhite": "#d2d8d9",
            "background": "#2b2d2e",
            "foreground": "#d2d8d9"
        }
    ]

    # Merge the existing color schemes with my own, overwriting any duplicates on property 'name'
    s["schemes"] = {**{x["name"]: x for x in s["schemes"]}, **{x["name"]: x for x in color_schemes}}
    s["schemes"] = list(s["schemes"].values())


# Read standard input to json
s = json.load(sys.stdin)

# Update the settings
update_file(s)

# Write the settings back to standard output
json.dump(s, sys.stdout, indent=4)

#  # If file exists try to read it
#  try:
    #  with open(settings_file, 'r') as f:
        #  settings = json.load(f)
        #  print("Settings file loaded")

        #  actions = settings["actions"]
        #  for action in actions:
            #  print(action["command"])

#  except:
    #  print(f'Could not read settings file: {settings_file}')

#  try:
    #  with open(preview_settings_file, 'r') as f:
        #  preview_settings = json.load(f)
        #  print("Preview settings file loaded")
#  except:
    #  print(f'Could not read settings file: {preview_settings_file}')
