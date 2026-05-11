I found **two distinct Vertiv/Liebert “XDH” families** in source material:

1. **Liebert XDH Horizontal Row Cooler** — the classic Liebert XD pumped-refrigerant, in-row module sold around **XDH20** and **XDH32**.
2. **Vertiv Liebert XDH High Heat Density Precision Air Conditioner** — a newer/global “XDH030…” style terminal unit whose model number encodes capacity, apparently used with XDC multi-connected systems.

## Main XDH in-row model lines and capacities

| Product family / model                             |               Model variants found |                                                          Nominal cooling capacity |                                                 Maximum cooling capacity | Rating notes / source confidence                                                                                                                                                                 |
| -------------------------------------------------- | ---------------------------------: | --------------------------------------------------------------------------------: | -----------------------------------------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Liebert XDH20 Horizontal Row Cooler**            | XDH20BK, XDH20SK, XDH20BS, XDH20SS | **22 kW / 6.3 tons at 60 Hz**; **21.6 kW / 6.1 tons at 50 Hz** in the user manual |                                 **25.3 kW / 7.2 tons** at 60 Hz or 50 Hz | User manual table rates capacity at **55°F / 13°C entering fluid temperature** and **50°F / 10°C or lower dew point**. ([Vertiv][1])                                                             |
| **Liebert XDH32 Horizontal Row Cooler**            | XDH32BK, XDH32SK, XDH32BS, XDH32SS |                                           **30 kW / 8.5 tons** at 60 Hz and 50 Hz |                                                     **34 kW / 9.7 tons** | Same user-manual rating basis: **55°F / 13°C entering fluid temperature** and **50°F / 10°C or lower dew point**. ([Vertiv][1])                                                                  |
| **Guide-spec version: XDH20**                      |                         XDH20 line |                **22 kW / 75,000 BTUH** at 60 Hz; **22 kW / 75,000 BTUH** at 50 Hz |                                    Not in the excerpted guide-spec table | Vertiv guide specification rates at **55°F entering fluid**, **98°F entering air**, and **50°F or lower dew point**; airflow listed as 2,500 CFM at 60 Hz and 2,428 CFM at 50 Hz.                |
| **Guide-spec version: XDH32**                      |                         XDH32 line |              **30 kW / 102,000 BTUH** at 60 Hz; **30 kW / 102,000 BTUH** at 50 Hz |                                    Not in the excerpted guide-spec table | Same guide-spec conditions; airflow listed as 4,000 CFM at 60 Hz and 3,850 CFM at 50 Hz.                                                                                                         |
| **Older XDH datasheet: XDH20**                     |                              XDH20 |                      **22 kW / 6.3 tons at 60 Hz**; **19 kW / 5.4 tons at 50 Hz** |                  **25.5 kW** under stated higher entering-air conditions | This older 2009/2016-style datasheet conflicts with the later user manual/guide-spec on 50 Hz nominal capacity. I’d treat it as older or condition-specific unless matching a unit submittal.    |
| **Older XDH datasheet: XDH32**                     |                              XDH32 |                      **30 kW / 8.5 tons at 60 Hz**; **27 kW / 7.7 tons at 50 Hz** |                  **34.5 kW** under stated higher entering-air conditions | Same caveat: the newer guide spec/user manual show 30 kW at 50 Hz, while this older datasheet shows 27 kW.                                                                                       |
| **Liebert XDH030… High Heat Density Precision AC** |    Example shown: **XDH030CS1LRC** |                              **30 kW**, encoded in digits 4–6 of the model number | I did not find a separate maximum capacity table in the available manual | This is a different-looking/global manual: model nomenclature says digit 3 “H” = horizontal cabinet in-row installation and digits 4–6 = cooling capacity in kW; example model is XDH030CS1LRC.  |

## What the XDH is, according to Vertiv

The current Vertiv product page describes the **Liebert XDH Cooling Module** as a **horizontal row cooler** placed in line with rack enclosures; it draws air from the hot aisle through the rear, cools it, and discharges into the cold aisle. ([Vertiv][2]) The older XDH datasheet says the unit is part of the Liebert XD high-density cooling family using **pumped refrigerant technology**, with refrigerant supplied by either an **XDP pumped refrigerant unit** or an **XDC refrigerant chiller**.

## Source material I’d keep

The strongest primary sources I found are:

| Source                                                                         | Why it matters                                                                                                                  |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| **Vertiv product page — “Vertiv™ Liebert® XDH Cooling Module”**                | Confirms the current product positioning as an in-row horizontal row cooler and links to brochure/manual. ([Vertiv][2])         |
| **Vertiv guide specifications — “Liebert XD Horizontal Row Cooler (XDH)”**     | Best concise source for spec-writing and nominal capacities: XDH20 = 22 kW, XDH32 = 30 kW, with airflow and rating conditions.  |
| **Vertiv Liebert XDH 50/60 Hz User Manual**                                    | Best detailed source for exact model variants and both nominal and maximum capacities for XDH20/XDH32. ([Vertiv][1])            |
| **Vertiv XDH datasheet PDF**                                                   | Useful older brochure/datasheet, but note its 50 Hz nominal capacities differ from the later manual/guide spec.                 |
| **Vertiv Liebert XDH High Heat Density Precision Air Conditioner User Manual** | Relevant if you are looking at newer/global XDH030-style nomenclature; it confirms XDH030 capacity coding as 30 kW.             |

## Bottom line

For the classic **Liebert/Vertiv XDH in-row cooling modules**, the core model lines I found are:

* **XDH20**: roughly **22 kW nominal**, **25.3 kW max** in the later user manual.
* **XDH32**: roughly **30 kW nominal**, **34 kW max** in the later user manual.

There is also a newer/global **XDH030…** model-code family where **030 = 30 kW**, but I’d treat that separately from the older **XDH20/XDH32 pumped-refrigerant Horizontal Row Cooler** line unless you have a region-specific submittal tying them together.

[1]: https://www.vertiv.com/48ec77/globalassets/shared/liebert-xdh-50-60hz-user-manual_00.pdf "Liebert® XDH™ User Manual"
[2]: https://www.vertiv.com/en-us/products-catalog/thermal-management/high-density-solutions/vertiv-liebert-xdh-cooling-module/ "
        Vertiv™ Liebert® XDH Cooling Module | High Density Solutions
    "
