# HVAC

## Cooling Towers

- In the context of cooling towers, PWL usually stands for "Sound Power
  Level" and the units are decibels. Equations usually have a form like:

$$
PWL = 56 + 30 \log \frac{TipSpeed}{1000} + \log (HP)
$$

- Tip speed is often `TS`.

- L/G stands for Liquid/Gas ratio and is the ratio of the mass flow
  rates for the water to the air.

- Another important cooling tower characteristic is the $\frac{KaV}{L}$
  value, where

  - $K$: overall heat enthalpy transfer coefficient, lb/h-ft²
  - $a$: Surface area per unit tower volume, ft²/ft^3
  - $V$: Effective tower volume, ft^3
  - $L$: Water mass flowrate, lb/h

## Min CW Flow over Cooling Towers

- From 'Variable Flow over Multiple Cooling Towers for Energy Savings',
  by Gray Stauffer, Wednesday 2021-03-10:
  - Easier for cross flow towers
    - 30% turn down for cross flow
    - only 70% for counter flow.

## York Chillers

From [link here](https://docs.johnsoncontrols.com/chillers/v/u/YK/YK-Style-H-Centrifugal-Liquid-Chiller-250-300-tons),
they provide a formula for minimum CWST.

$$\textrm{CWST_{min}} = \textrm{CHWST} - \textrm{CW Range} + 5°F + 12 (PLR)$$

Page 38. See `GoogleDrive\hvac\160.76-EG1.pdf`

Model Number Nomenclature:

Positions - Meaning

1-2: Unit Type
3-4: Evaporator Code
5-6: Condenser Code
7-8: Compressor Code
9: Power Supply (- for 60 Hz, 5 for 50 Hz, M for 50 Hz Supply / 60 Hz motor)
10-11: Motor Code
12: Design Level
13: Special

## IPLV

Updates the EER or kW/ton value by the weighted average of efficiencies
at different part load ratios. Heavily weighted to the PLR at 75% and
50% load.

IPLV (or NPLV) = 0.01A+0.42B+0.45C+0.12D

Where:

A = COP or EER @ 100% Load
B = COP or EER @ 75% Load
C = COP or EER @ 50% Load
D = COP or EER @ 25% Load


## Andover/TAC History

Interesting resources:

Andover controls started in 1975

TAC was bought out by Schneider Electric in 2003/2004 - Migrated into
the SE brand in 2009.

TAC was a Swedish company, then underwent a series of acquisitions and
mergers.

- Tour Agenturer (1925)
- Tour & Andersson (1977)
- TA Hydronics and TA Control (aka TAC) (1994/1995)
- Merged with CSI from Dallas, TX (2000)
- Schneider Electric (2003)

[link](http://www.bmsengineers.co.uk/andover-controls)
[TAC History](https://www.se.com/ww/en/about-us/company-profile/history/tac.jsp?contentId=document/30869)
[TAC Wikipedia](https://en.wikipedia.org/wiki/TAC_(building_automation))


PaaS: Platform as a service [MS Azure](https://en.wikipedia.org/wiki/Microsoft_Azure)

## CO2 measurement

Most HVAC sensors are going to be based on IR sensors. [source](https://jlcinternational.com/co2-measurement-theory-basics/).

## Cascaded Control

Notes from: [source](Ryan_Miles_Feb2021_14-21_Understanding_Cascade_Control_and_Its_applications_for_HVAC.pdf)
Miles ASHRAE Journal, Feb 2021, Pg. 14.

- Instead of single PID loop to have actuator control to desired process
  variable, you have actuator control to *manipulated variable* setpoint
  instead, where the *manipulated variable* setpoint resets from a
  second PID loop.

- Examples:
    - Box Reheat Coils: Reheat coils control to Discharge Temp.
      Discharge temp resets based on space temp. This prevents
      stratification. (ASHRAE Standard 90.1 requires < 20°F and Guideline
      62 has tighter restrictions, and Guideline 36 explicitly states the
      control should be this way).

    - AHU Cooling Coils: PID loop from CHWV to flow instead of SAT
      directly. This way you prevent pulling more flow than needed and
      avoiding the "saturation region" in which more flow results in
      little additional heat transfer.

## COP to kW/ton

COP = 3.516 / (kW/ton)


## 2-pipe vs. 4-pipe

2 pipe means there is single supply and return piping for both heating
and cooling. The system can only be in one mode at a time.

4 pipe means there is a supply/return for both heating and cooling.
Systems can be in either heating or cooling at any time.

## Silicon Controlled Rectifiers (SCRs)

Solid state switching device which can provide fast, infinitely variable
proportional control of electric power
<https://www.avatarinstruments.com/guide-to-scr-power-controls/>.

## Acronyms

XFMR - shortened version of 'transformer'
SCR - Silicon controlled rectifier
FTR - Floor Telecommunications Room
PTR - Primary Telecommunications Room
IDF - Intermediate Distribution Frame
MDF - Main Distribution Frame

SLR - SuperLAN Room

FTR/PTR is analogous to IDF/MDF in the IT world.

<https://www.imss.caltech.edu/services/wired-wireless-remote-access/construction-requirements/Voice-and-Data-Network-Terminology>


## CFM per Ton Rule of Thumb

Based on quick internet search, ~400 CFM/ton
 - Sources
  - <https://www.reference.com/world-view/cfm-per-ton-air-conditioning-vary-afe5e016234707f1>
  - <https://hvac-blog.acca.org/400-cfm-per-ton-or-is-it/>
  - <https://climesense.com/how-many-cfm-per-ton/>
  - <https://inspectapedia.com/aircond/Air_Flow_Rates.php>
  - <https://www.eng-tips.com/viewthread.cfm?qid=305846>


## Trim and Respond logic

ASHRAE Guideline 36 is all in on Trim and Respond logic. The context
behind this is that there was an ASHRAE research project RP-1455.

Advantages:

1. Easier to tune
2. Can "respond" more quickly than "trim".
3. Less polling
4. Allows for easier ignoring, weighting of specific zones.

[link](https://tayloreng.egnyte.com/dl/e1DzRUmHTl/ASHRAE_Journal_-_Trim_and_Respond.pdf_)


## End of line resistors (ELR, EOLR, DEOLR)

Basically they allow some supervisory control to verify whether the wiring has been broken resulting in an open or short circuit.

- <https://www.alarmgrid.com/blog/ever-wonder-why-they-re-called-end-of-line-resistors>
- <http://www.controlandinstrumentation.com/systems/endoflineresistors.html>

## Direct Drive vs Belt Driven

Refs:
 - <https://eldridgeusa.com/blog/which-are-better-direct-or-belt-drive-fans/>
 - <https://www.industrialfansdirect.com/blogs/info-center/85154244-belt-driven-vs-direct-drive-fans>

Efficiency: Direct drive more efficient, no belt losses.
Maintenance: Direct drive doesn't need belt replacements, tightening.
Reliability: Direct drives can handle high heat when in the air stream.
Noise: related to propeller speed. Belt drives can spin at whatever rate you can make the pulleys.
Cost: Depends.
Overall: Direct drive for most.

## Wet Bulb Empirical Regression Formula

From:
Wet-Bulb Temperature from Relative Humidity and Air Temperature
Roland Stull
November 2011
DOI: 10.1175/JAMC-D-11-0143.1
American Meteorological Society

T in Celsius, RH% (0-100), atan taking radians.

Tw = T * atan[ 0.151977 * ( (RH% + 8.313659)^1/2  ) ] + atan(T + RH%) - atan(RH% - 1.676331) +  0.00391838(RH%)^3/2 * atan(0.023101 * RH%) - 4.686035

## Spark Spread

<https://www.eia.gov/todayinenergy/detail.php?id=9911>

Spark spread ($/MWh) = power price ($/MWh) – [natural gas price ($/mmBtu) * heat rate (mmBtu/MWh)]

Benchmark value for heat rate is often 7,000 BTU/kWH ~ 50% conversion efficiency.

## GCV vs NCV

 - Came across the acronym NCV in a boiler flue gas analysis.
   NCV stands for net calorific value. Equates to LHV.

- From <https://adgefficiency.com/energy-basics-hhv-versus-lhv/>

  higher heating value (HHV) aka gross calorific value (GCV)
  lower heating value (LHV) aka net calorific value (NCV)

## SEER

EER is output BTUs / input Wh. EER = 3.41214 * COP, COP = EER / 3.41214.
EER = 12 * kW/ton, kW/ton = EER / 12.

## WWR - Window to Wall Ratio, Window percentage

WWR = 1 / (1 - Window Percentage)
Window Percentage = 1 - 1 / WWR
