---
name: 'Understand EnergyPlus IDF file'
description: 'This skill describes a CLI utility to get short summaries of key inputs and assumptions from EnergyPlus .idf files'
---

I have a CLI utility, `idf.py` that you can use to get useful summarirized information from EnergyPlus IDF files.
You should be using this skill when you are required to audit or check certain parts of an EnergyPlus IDF file.

It is invoked with `idf.py`.
This is the output of the current help. You can always use `idf.py --help` to see the latest.

```
Usage: idf.py COMMAND [filename]
Commands:
  eflh: Print the equivalent full load hours of fractional schedules.
  construction: Print the R-value and U-value of constructions.
  int_loads: Print internal loads.
  airloops: Print air loop design flow rates.
  chillers: Print chiller design data.
  cooling_towers: Print cooling tower design data.
  const_sch: Print constant schedules.
  day_sch: Print day schedules.
  sch_process: Process day schedules.
  sch_compact: Print compact schedules.
  zones: Print zone details.
  spaces: Print space details.
Options:
  --header: Print a header row.
  --dir DIR: Directory for sch_process.
```

Example usage:

```sh
$ idf.py --header construction 'envelope,lights,hvac.idf'
Construction    R-Value (ft²·°F·hr/Btu) U-Value (Btu/hr·ft²·°F)
Barracks Roof   25.45   0.039
Barracks Exterior Wall  16.79   0.060
Interior Wall   0.45    2.219
Barracks Ceiling Floor  0.25    4.004
Construction_Barracks_Window    2.22    0.450
```
