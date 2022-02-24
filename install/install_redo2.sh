#!/bin/sh
set -e

if test -z "$LOCALBIN"; then
    printf "Variable LOCALBIN must be set.\n"
    exit 1
fi

latest_release="$(latest_release zombiezen redo-rs)"
download="$(printf "%s" "$latest_release" | github_releases.py 'redo_v[0-9]\.[0-9]\.[0-9]_linux_x86-64.zip')"
asset="$(printf "%s" "$download" | awk 'NR == 1')"
name="$(printf "%s" "$download" | awk 'NR == 2')"
# Need to follow redirects with '-L' to get the actual file.
# Curling to
printf "Curling to '%s'\n" /tmp/"$name" >&2
curl --output /tmp/"$name" -L "$asset"

# Make temporary directory in /tmp.
# This is where we'll extract the zip file.
# We'll delete it when we're done.
tmpdir="$(mktemp -d)"
unzip /tmp/"$name" -d "$tmpdir"

# Search for all files under a 'bin' directory.
# This is where the binaries are.
# We'll copy them to the local bin directory.
# We'll delete the original files.
for file in "$tmpdir"/*/bin/*; do
    cp "$file" "$LOCALBIN"
done
