#!/usr/bin/env python3

# This script accepts relative filepaths from the standard input,
# opens the default EDITOR to make changes, then makes a shell script to rename

import sys
import os
import re
import pathlib

def convert_to_int_if_possible(s: str):
    """
    Convert the given string to an int if possible. Otherwise, return the
    original string.
    """
    return int(s) if s.isdigit() else s

def version_sort_in_place(l):
    """ Sort the given list in the way that humans expect."""
    l.sort(key=alphanum_key)

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    #  return [convert_to_int_if_possible(c) for c in re.split('([0-9]+)', s) if convert_to_int_if_possible(c) != ""]
    return [convert_to_int_if_possible(c) for c in re.split('([0-9]+)', s.lower())]

def quote(s):
    return "'" + s.replace("'", "\"'\"'") + "'"

# Get the editor, if not provided crash
editor = os.environ.get('EDITOR')
if not editor:
    print('No editor set')
    sys.exit(1)

# Don't use stdin because it can be a pipe
current_tty = os.ttyname(sys.stdout.fileno())

# Check if the current tty is a terminal
if not os.isatty(sys.stdout.fileno()):
    print('stdout is not a terminal')
    sys.exit(1)

# Get the files from stdin if provided.
# Check that stdin is not a tty, so that we don't read from stdin if it's not provided
if not sys.stdin.isatty():
    files = sys.stdin.read().splitlines()
else:
    files = os.listdir('.')

version_sort_in_place(files)

# Put files to temp file
with open('/tmp/brename', 'w') as f:
    for file in files:
        f.write(file + '\n')

# Open editor
os.system(editor + ' /tmp/brename')

# Read temp file
with open('/tmp/brename', 'r') as f:
    new_names = f.read().splitlines()

    # Check that the number of files is the same
    if len(files) != len(new_names):
        print('Number of files and new names does not match')
        sys.exit(1)

    # Check that the files are being renamed, not moved, count number of '/' in each
    for i in range(len(files)):
        if files[i].count('/') != new_names[i].count('/'):
            print('Files are being moved, not renamed')
            sys.exit(1)

    # Print the shell script to the terminal and file. Quote the arguments to rename.
    # Use single quotes to avoid escaping. If the file name contains a single quote,
    # use backslash to escape them everywhere.
    # Ask user in terminal for confirmation, and then run
    #  print('#!/bin/sh')
    for i in range(len(files)):
        if files[i] != new_names[i]:
            print(" ".join(['mv', quote(files[i]), quote(new_names[i])]))
        else:
            print('#', files[i], 'is not being renamed')

    print('Do you want to run this? (y/n)')

    # Read from current_tty
    try:
        with open(current_tty, 'r') as tty:
            if tty.readline().strip() == 'y':
                for i in range(len(files)):
                    if files[i] != new_names[i]:
                        print('Renaming', files[i], 'to', new_names[i])

                        # First make sure new directory exists, create paths if necessary
                        path = pathlib.Path(new_names[i])

                        if path.parent != pathlib.Path('.'):
                            os.makedirs(path.parent, exist_ok=True)

                        os.rename(files[i], new_names[i])
    except KeyboardInterrupt:
        print('\nCancelled')
