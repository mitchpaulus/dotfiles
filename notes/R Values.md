# R Values

(ASHRAE Fundamentals 2021 Chapter 26, Table 10)
Outdoors
  - 15 mph wind (for winter) = 0.17
  - 7.5 mph wind (for summer) = 0.25

Indoors

Values are R-values
Position   | Direction  | ε=0.90 | ε=0.20 | ε=0.05
-----------|------------|--------|--------|-------
Horizontal | Upward     | 0.61   | 1.10   | 1.32
45°        | Upward     | 0.62   | 1.14   | 1.37
Vertical   | Horizontal | 0.68   | 1.35   | 1.70
45°        | Downward   | 0.76   | 1.67   | 2.22
Horizontal | Downward   | 0.92   | 2.70   | 4.55


(ASHRAE Fundamentals 2021 Chapter 26, Table 1)

Carpet and rubber pad (one-piece) 3/8" 20 lb/ft³: R-0.68



## Air Gap

Pg. 4:10, Table 4-4

## Insulating Materials

Fiberglass Blanket and Batt

Approx 3.5" 0.4-2.0 lb/ft^3, R-13
Approx 3.5" 1.2-1.6 lb/ft^3  R-15


Item                          | Density (lb/ft²) | R    | Source
------------------------------|------------------|------|----------------
0.5" Gypsum                   | 45               | 0.32 | A:3
4" Heavyweight concrete block | 61               | 0.71 | 8:9 (Table 8-5)


# Glass

Thermal conductivity: 1.05 W/mK or 0.6066 Btu/hr ft °F <https://material-properties.org/glass-density-heat-capacity-thermal-conductivity/>

DOE-2 default is 0.52 Btu/hr ft °F <https://www.osti.gov/servlets/purl/10180705>

# ASHRAE 90.1-2010 Table A9.4D

0.5" Gypsum: R-value: 0.45
0.625" Gypsum: R-value: 0.56
Concrete at R-0.0625/in
Carpet and rubber pad: R-value: 1.23

# ASHRAE Table A9.4E (Thermal Conductivity of Concrete Block Material)

Density (lb/ft3) | Thermal Conductivity (Btu in/hr ft2 °F)
-----------------|----------------------------------------
80               | 3.7
85               | 4.2
90               | 4.7
95               | 5.1
100              | 5.5
105              | 6.1
110              | 6.7
115              | 7.2
120              | 7.8
125              | 8.9
130              | 10
135              | 11.8
140              | 13.5

# Brick

From (ASHRAE Fundamentals 2021 Chapter 26, Table 1)

Specific Heat: 0.19 Btu/lb °F
Conductivity from 2.5 to 10.2 Btu in/hr ft² °F

# EnergyPlus

Thickness, conductivity, density, and specific heat
