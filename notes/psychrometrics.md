# Psychrometrics

W = X Pv / (P - Pv)

or

Pv =  P W / (W + X)

X = 0.621945

- [Tetens equation](https://en.wikipedia.org/wiki/Tetens_equation)

```
P = 0.61078 * exp(17.27*T/(T+237.3))
P in kPa, T in °C

P = 0.088586 * exp((1727*T -55264) / (100 * T + 39514))
P in psi, T in F

# derivative
(ax + b) / (cx + d) -> (a*d - b*c) / (cx + d)^2

(a*d - b*c) = 1727 * 39514 - (-55264 * 100) = 73,767,078
```

## Online psychrometric chart

<https://drajmarsh.bitbucket.io/psychro-chart2d.html>

## Low Temperature Psychrometrics

The triple point of water is at 0.01°C.
For temperatures far below freezing, the water can typically be in one of two states: vapor or solid.
So instead of a dew-point temperature, you really have a ["frost-point" temperature](https://pdhonline.com/courses/m135/m135content.pdf).

Also from that source:

> Special care must be taken when using a wet-bulb thermometer in near freezing conditions.
> At temperatures below 32°F, touch the wick with a piece of clean ice or another cold object to induce freezing,
> because distilled water can be cooled below 32°F without freezing.
> The psychrometric chart must use frost-bulb, not wet-bulb temperatures, below 32°F to be accurate with this method.
