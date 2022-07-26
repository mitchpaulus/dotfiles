# ASHRAE Guideline 36

## Economizer Sequences

Around pg ~113 - 5.16.2

Links:

- <https://www.ashrae.org/news/ashraejournal/guideline-36-2021-what-s-new-and-why-it-s-important>
- [Commissioning of Guideline 36](https://doi.org/10.6028/NIST.TN.2024)

Chilled and hot water plant sequences based on RP-1711, Advanced
Sequences of Operation for HVAC Systems - Phase II Central Plants and
Hydronic Systems

DOAS systems will likely be covered in next version in 2024, based on
RP-1865, Optimizing Supply Air Temperature Control for Dedicated Outdoor
Air Systems.


## Reference pages

T&R logic: pg. 44
Importance multipliers: pg. 44.
CWST Reset: 214

Variable	Value
SP0
SPmin
SPmax
Td
T
I
R
SPtrim
SPres
SPres-max

## PLR Chiller Staging

Centrifugal chiller efficiency varies significantly with lift. As lift increases for a given load, centrifugal compressors
must run faster to avoid surge. Capacity trimming under such conditions is accomplished using inlet guide vanes or
variable geometry diffusers, which reduces chiller efficiency. The above equation resets the centrifugal staging point
up when lift is high to minimize throttling of surge control devices and keep chillers operating near to their optimal
efficiency. Engineers should consult with the chiller manufacturer to obtain part load efficiency data and adjust the
optimal staging bounds for each application. See the ASHRAE Fundamentals of Design and Control of Central
Chilled-Water Plants Self-Directed Learning Course for how E and F can be optimally determined. The E and F
values above are the simplified coefficients from this SDL, Appendix A normalized for a plant with any number of
chillers.

## Plant DP vs. CHWST

The recommended logic first resets differential pressure setpoint to maximum before resetting chilled water supply
temperature setpoint down towards design. Parametric plant analysis performed in a variety of climate zones during
the development of ASHRAE’s “Fundamentals of Design and Control of Central Chilled-Water Plants” Self-Directed
Learning Course showed that the pump energy penalty incurred with this approach is more than offset by
chiller energy savings resulting from keeping the chilled water supply temperature setpoint as high as possible.
