# Usage: idf.py COMMAND [filename]
# Commands:
# eflh: Print the equivalent full load hours of fractional schedules.
# construction: Print the R-value and U-value of constructions.
# int_loads: Print internal loads.
# airloops: Print air loop design flow rates.
# chillers: Print chiller design data.
# cooling_towers: Print cooling tower design data.
# const_sch: Print constant schedules.
# day_sch: Print day schedules.
# sch_process: Process day schedules.
# sch_compact: Print compact schedules.
# Options:
# --header: Print a header row.
# --dir DIR: Directory for sch_process.

complete -c idf.py -n '__fish_use_subcommand' -a eflh -d 'Print the equivalent full load hours of fractional schedules.'
complete -c idf.py -n '__fish_use_subcommand' -a construction -d 'Print the R-value and U-value of constructions.'
complete -c idf.py -n '__fish_use_subcommand' -a int_loads -d 'Print the internal loads of the model.'
complete -c idf.py -n '__fish_use_subcommand' -a airloops -d 'Print air loop design flow rates.'
complete -c idf.py -n '__fish_use_subcommand' -a chillers -d 'Print zone design loads.'
complete -c idf.py -n '__fish_use_subcommand' -a cooling_towers -d 'Print cooling tower design data.'
complete -c idf.py -n '__fish_use_subcommand' -a const_sch -d 'Print constant schedules.'
complete -c idf.py -n '__fish_use_subcommand' -a day_sch -d 'Print day schedules.'
complete -c idf.py -n '__fish_use_subcommand' -a sch_process -d 'Process day schedules.'
complete -c idf.py -n '__fish_use_subcommand' -a sch_compact -d 'Print compact schedules.'
