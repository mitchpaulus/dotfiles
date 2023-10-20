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

# Schedules

```
MON, TUE, WED, THU, FRI, SAT, SUN, HOL, ALL, WD, WEH, HDD, CDD
```

# Other utilities

<https://github.com/grammy-jiang/doe2-sim-parser>
