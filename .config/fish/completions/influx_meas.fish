complete -c influx_meas -f -a '(influx bucket ls --json | jq -r ".[] | .name")'
