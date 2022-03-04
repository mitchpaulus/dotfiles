# Alerton Visual Logic



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
