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

