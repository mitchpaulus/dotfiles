# Alerton Visual Logic

`BR` stands for branch point - used for points that link blocks within the diagram.

[Reference](https://hvac-talk.com/vbb/threads/2051121-Alerton-BacTalk-Visuallogic-PI-Function)

## Analog Input Comparator

Plus Input >= Minus input + TDB  == ON
Plus Input <= Minus input - RDB  == OFF
Else: No change

## PI loops

Output = P + I + 50

Error = FB - SP

P = Kp (E)

I = Iprev + Iinc, Absolute value limited to Ilim

Iinc = E (Ki / 60), Absolute value limited to Imax / 60

Iprev = STUP on startup

If Ki = 0, I = STUP - This can be used to reset the integral gain when a setpoint changes or something (pg 62 first paragraph of Integral startup).

The absolute output is limited between 0 and 100 (pg. 58 of manual).

## One Shot

Description: Sets the output ON for one pass of DDC whenever the input *transitions* from OFF to ON.
Remarks:     The *output* remains ON only for a single pass of DDC, even if the input stays ON for a longer or period.

## Flip Flop

Any time the reset is On, the output goes to Off.

The output then goes to On anytime the set input goes On, and stays on until a reset.

Output previous  | Set Current   | Reset Current   | Output
-----------------|---------------|-----------------|-------
0                | 0             | 0               | 0
0                | 0             | 1               | 0
0                | 1             | 0               | 1
0                | 1             | 1               | 0
1                | 0             | 0               | 1
1                | 0             | 1               | 0
1                | 1             | 0               | 1
1                | 1             | 1               | 0

## Velocity Pressure to FPM Converter

Looks like gauge - has 'Zero' 'Out' and 'K' on the meter.

Output = k √ (vp_input - zero)

## Delay on Break/Make

Delay on break -> delay going from On to Off
Delay on make -> delay going from Off to On

Opposite transitions for each have no delay. Delays are in seconds.

## Sample and Hold

When the CTRL input is ON, the output and the stored value are set equal to the input.
When the CTRL input is OFF, the output is set to the last stored value.
