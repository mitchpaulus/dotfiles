#!/bin/sh

# Purpose of this script is to update weather for status blocks, but have it at a much longer
# interval than most of the other items.
weather_file=~/.local/share/weather/weather.txt
mkdir -p ~/.local/share/weather

[ -e "$weather_file" ] || date +%s > $weather_file

# 300 s = 5 mins
if [ "$(awk 'BEGIN { FS=OFS="\t" } NR == 1 { printf $1 + 300 }' $weather_file)" -lt "$(date +%s)" ]; then
    printf "%s\t%s" "$(date +%s)" "$(curl -s 'wttr.in/Dallas?format=%t+%C')" > $weather_file
fi

awk 'BEGIN { FS=OFS="\t" } { print $2 }' $weather_file

