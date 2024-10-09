
Can see the nesting for HFB blocks.


Line likes

```
#11                     "CALIBRATE\SA1_T_OFS" [6,14,0,7] '0x10002','Temperature Sensor Offset Value','B4CAC315-5C71-47a5-B383-A96EF2874327' = PVR (1)
```

In the square brackets is [x-coord, y-coord, ?, ?] and the `= PVR (1)` is the block type with the parameter.

>1:0 = {{133,23.}}
>2:0 = {{1,0}}
>3:0 = {{2,1}}
>4:0 = {{5,0}}
>5:0 = {{133,45.}}
>6:0 = {{53,17;53,22;9,0}}
>7:0 = {{6,1}}
>8:0 = {{6,2}}
>9:0 = {{71,22.}}
>10:0 = {{92,9{92,19{2,0}{92,41;4,0}}{15,0}}}
>11:0 = {{21,20;12,1}}
>12:0 = {{28,9{28,13;6,0}{10,0}}}
>13:0 = {{95,34{95,27;2,2}{95,49;4,2}}}
>14:0 = {{12,0}}
>16:0 = {{4,1}}

These '>' are the connections. Each block has a number and this defines where it goes to next.
It can be a list of connections, everything but the last is coordinates, sometimes of bends and such.
The last item is the {block ref, port}. Port is 0 based. 0 is at top of the block.

AUT grammar

```
[AUT]


```

The coordinates are about 327.91667 = 11 inches. 29.810606 / inch

792 pts = 11 inches, so it doesn't equal some multiple of points. Also not mm, so not sure what it is.
