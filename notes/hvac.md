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

## York Chillers

From [link
here](https://docs.johnsoncontrols.com/chillers/v/u/YK/YK-Style-H-Centrifugal-Liquid-Chiller-250-300-tons),
they provide a formula for minimum CWST.

$$\textrm{CWST_{min}} = \textrm{CHWST} - \textrm{CW Range} + 5°F + 12 (PLR)$$


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

