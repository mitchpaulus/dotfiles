# DOE-2 Input

Rules:

1. One or more blanks must separate each element of an instruction
2. The equals sign between a U-name and a command is optional
3. A U-name may be required, optional, or not allowed, depending upon the particular command.
4. A valid command (or command abbreviation) must be the second item, or the first if no U-name is specified.
5. If a U-name is present, the U-name and the command must appear on the same line
6. Commands may not be misspelled or contain embedded blanks.
7. Every instruction must end with the instruction terminator, defined to be two successive periods preceded and followed by a blank character.


System is followed by zones


# Geometry

In IP, units of length are in feet. See `POLYGON` pg. 98 of `DOE22Vol2-Dictionary_48r`.

Each door is associated with the EXTERIOR-WALL before it.


# eQuest examples


```
"Ground Flr" = FLOOR
   AZIMUTH          = 360
   POLYGON          = "Floor Polygon"
   SHAPE            = POLYGON
   FLOOR-HEIGHT     = 13
   SPACE-HEIGHT     = 9
   C-DIAGRAM-DATA   = *Bldg Envelope & Loads 1 Diag Data*
   ..

"South Perim Spc (G.S1)" = SPACE
   SHAPE            = POLYGON
   ZONE-TYPE        = CONDITIONED
   PEOPLE-SCHEDULE  = "People-Schedule"
   LIGHTING-SCHEDUL = ( "GndPrm Ltg Sch" )
   TASK-LIGHT-SCH   = "GndCor Occ Sch"
   EQUIP-SCHEDULE   = ( "GndPrm Eqp Sch" )
   INF-SCHEDULE     = "GndCor Sys1 Infil Sch"
   INF-METHOD       = AIR-CHANGE
   INF-FLOW/AREA    = 0.0249137
   PEOPLE-HG-LAT    = 232.198
   PEOPLE-HG-SENS   = 250
   LIGHTING-W/AREA  = ( 1.22879 )
   TASK-LT-W/AREA   = 0
   EQUIPMENT-W/AREA = ( 0.856031 )
   AREA/PERSON      = 100
   POLYGON          = "Space Polygon 1"
   LOCATION         = FLOOR-V1
   C-ACTIVITY-DESC  = *Lobby (Reception/Waiting) (64%)*
   ..

"South Win (G.S1.E1.W1)" = WINDOW
   GLASS-TYPE       = "Window Type #2 GT"
   FRAME-WIDTH      = 0.108333
   X                = 1.10749
   Y                = 3.10833
   HEIGHT           = 5.00333
   WIDTH            = 82.4442
   FRAME-CONDUCT    = 2.781
   ..



```


# Chillers

Capacity in units of millions of BTU/hr
```
tons * 12000 / 1000000
```

# Circulation Loops

```
LOOP-NAME = CIRCULATION-LOOP
    TYPE = CHW
    LOOP-PUMP = CHW-PUMP
```

# Schedules

```
MON, TUE, WED, THU, FRI, SAT, SUN, HOL, ALL, WD, WEH, HDD, CDD
```

# Other utilities

<https://github.com/grammy-jiang/doe2-sim-parser>


# Weather

Dry bulb Temperature (°F)
Wet bulb Temperature (°F)
Atmospheric Pressure (inches of Hg times 100)
Wind Speed (knots)
Wind Direction (compass points 0-15, with 0 being north, 1 NNE, etc.)
Cloud Amount (0 - 10, with 0 clear and 10 totally cloudy)
Cloud Type (0, 1, or 2)
 0 is cirrus or cirrostratus, the least opaque;
 1 is stratus or stratus fractus, the most opaque; and
 2 is all other cloud types, of medium opacity
Humidity Ratio (pounds of water per pound of dry air)
Density of Air (lb/ft3)
Specific Enthalpy (Btu/lb)
Rain Flag (0 means it is not raining; 1 means it is)
Snow Flag (0 means it is not snowing; 1 means it is)


## DOE-2 fmt format

Header example:
```
<location> <year> <latitude> <longitude> <time zone> <solar flag 3 = no solar, 5 = solar>
<jan clearness num> <feb clearness num> <mar clearness num> <apr clearness num> . . .
<jan ground temp °R> <feb ground temp °R> <mar ground temp °R> <apr ground temp °R> . . .
Arlington-Reagan.Was 2008   38.85   77.04    5    5
  1.00  1.00  1.00  1.00  1.00  1.00  1.00  1.00  1.00  1.00  1.00  1.00
 527.7 527.7 527.7 527.7 527.7 527.7 527.7 527.7 527.7 527.7 527.7 527.7
```

1-2: Month (1-12)
3-4: Day (1-31)
5-6: Hour (1-24)
7-11: Wet Bulb Temperature (°F) (0 decimal places)
12-16: Dry Bulb Temperature (°F) (0 decimal places)
17-22: Atmospheric Pressure (in Hg) (0 decimal places)
23-27: Cloud Amount (0-10) (0 decimal places)
28-30: Snow indicator (0-1) (Int)
31-33: Rain indicator (0-1) (Int)
34-37: Wind Direction (0-15) (Int)
38-44: Humidity Ratio (4 decimal places)
45-50: Air Density (lb/ft3) (3 decimal places)
51-56: Specific Enthalpy (Btu/lb) (1 decimal places)
57-63: Total Horizontal Solar (BTU/hr-ft2) (1 decimal places)
64-70: Direct Normal Solar (BTU/hr-ft2) (1 decimal places)
71-73: Cloud Type (0-2) (Int)
74-78: Wind Speed (knots) (0 decimal places)

## OA Ventilation

If the `MIN-AIR-SCH` is specified, its hourly specified value will always be used (even if MIN-OA-METHOD is specified)
unless the hourly scheduled value is -999.

```
