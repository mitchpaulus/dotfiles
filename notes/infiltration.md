Chapter 16 - ASHRAE Fundamentals

Table 13 Summary of Building Airtightness Data
Air Leakage, cfm/ft2 at 0.30 in. of water
Standard or Code                  Material Assembly             Whole Building*
ASHRAE 90.1                       0.004    0.04                 0.39
ASHRAE/ICC/USGBC/IES 189.1-2023   0.004*   0.04*                0.20
IECC                              0.004    0.04                 0.39
IgCC                  Same as ASHRAE 189.1 Same as ASHRAE 189.1 0.25
USACE ECB 2009-29                 0.004    —                    0.25
GSA P100-2021                     0.004    0.04                 2.25


0.3 in. of water is a common "Blower door test" pressure, not an actual design pressure for infiltration.

ASHRAE 90.1 uses a conversion of 0.112 to convert between the blower door and something that should be input into EnergyPlus.

The 0.112 comes from the PNNL report, dividing their example.

0.4 CFM/ft2 * 0.112 = 0.0448 CFM/ft2 = 0.000227584 (m3/s)/(m2)
