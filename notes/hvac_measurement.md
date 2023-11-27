# HVAC Measurement

## CO2

- Telaire 7001 CO2 (from Onset)
    - <60s to 90% of step input.
    - Therefore <120s (2 min) to 99% of step input.
    - +/- 50 ppm or 5% of reading (CO2 > 1,000 ppm), whichever is greater.
    - +/- 20 ppm repeatability


## Temperature

From discussion with work colleague:

- RTDs: Typically used with water temperature. Little more fragile
- Thermisters: Typically used with thermostats. Tighter range for
  temperature within range of spaces.

- Thermocouples - least accurate of 3, Most AHU measurements.

MAT - multiple thermocouples welded

  - Types:
    - K: Good for fluke
    - J
    - T: Tighter range


## 4-20 mA vs. 0-10 V

[Veris](https://blog.veris.com/choosing-analog-signal-types-for-industrial-sensors-0-10v-or-4-20ma) says prefer 4-20 mA:

- Current is much less vulnerable to noise, interference, or voltage drop.
- Only two wires are required. Since there will always be at least 4 mA flowing through the loop, your instrument can be “loop-powered” (using the same two wires that transmit signals).
- A long cable run will not affect the accuracy of a current signal.
- Faults are easily detected. A reading of 0 mA indicates no signal, whereas 4 mA represents a zero value measurement.
