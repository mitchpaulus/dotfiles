

[Source](https://download.schneider-electric.com/files?p_enDocType=Technical+leaflet&p_File_Name=03-00030-07-en.pdf&p_Doc_Ref=03-00030-07).
Also `03-00030-07-en SE TAC Menta.pdf` and `TAC Vista Menta Technical Manual.pdf` in PDF references.

From <https://www.se.com/ww/en/product-range/2312-tac-vista/?subNodeId=12146372280en_WW>
TAC Vista is a comprehensive software suite of building management tools that control and monitor your building management systems.
The TAC Vista software is modular and each function can be purchased separately.

- TAC Menta is a graphic application programming tool designed for the TAC Xenta 280/300/401/700 controllers.
  The three signal types are:
  •	 Integer – a signed 16 bit number
  •	 Real – a signed 32 bit number in IEEE format, precision of 7
  digits and
  •	 Binary – 0/1 = FALSE/TRUE


From `TAC Vista Menta Technical Manual.pdf`, available in `PDF References` folder.

SNVT = Standard Network Variable Type, which enables LonWorks™ network communication between nodes from different manufacturers.

`HFB` - Hierarchical Function Block

Simple blocks

- `DELAY` - Delayed On/Off
    - Inputs:
        - State (BINARY)
    - Parameters:
        - `DelayOn` (REAL)
        - `DelayOff` (REAL)
    - Output Type - Binary
    - Access: RO

This block delays the transitions of an input signal (state) by the time specified in seconds as defined by
the `DelayOn` (transition 0 to 1) and `DelayOff` (transition 1 to 0) parameters.
Note that the input signal must be true for a time interval longer than `DelayOn` in order to generate a pulse on the block output,
cf. the timing diagram below.
The input must also be false for a time interval longer than `DelayOff` in order to reset the output to false.


- `PIDP` - PID Controller - Analog Output

    - Inputs
        - MV (REAL) - Measured Value
        - SP (REAL) - Set Point
        - Mode (Integer) - Controller operating mode
        - G (REAL) - Proportional Gain
        - Ti (REAL) - Integral Time
        - Td (REAL) - Derivative Time
        - Dz (REAL) - Dead Zone
        - TSg (REAL) - Tracking Signal

    - Parameters
        - ControlInt (REAL) - Control interval (sec)
        - UMin (REAL) - Minimum permissible control signal
        - UMax (REAL) - Maximum permissible control signal
        - StrokeTime (REAL) - Actuator full stroke travel time (sec)
    - Output Type - Real
    - Access: R/W


Operating Mode

Mode | Description
-----|---------------------------------
0    | Off, controller stopped, output = TSg input
1    | Normal control
2    | Controller output forced to UMax
3    | Controller output forced to UMin
else | same as mode 0

- `PVR` - Real Value Parameter
    Basically a constant, or user changeable real value if it's made public.

- `SR` - Set-Reset Flip-Flop
    - Inputs
        - Set (s) (D) Binary
        - Reset (r) Binary
    - Parameters
        - InitValue Binary
    - Output Type - Binary

```
State table
State (t) Reset (t) Output (t + 1)
0   0  output(t)
0   1  0
1   0  1
1   1  invert(output(t))
```
