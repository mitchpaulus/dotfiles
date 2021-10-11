# Algorithms

## Percentiles

Given sorted array:
    Calculate index

$$n = ⌈(P/100) * N⌉$$

Here $n$ is value 1 to N.

if index is 0-based, subtract 1 from this.


## Overlap of Polygons

Part of a subject area called polygon "clipping". Given a clipping
polygon and a subject polygon, can transform into clipped polygon.

- [Clipping (computer graphics)](https://en.wikipedia.org/wiki/Clipping_(computer_graphics))

Algorithms:

1. Greiner-Hormann
  - [Wikipedia](https://en.wikipedia.org/wiki/Greiner%E2%80%93Hormann_clipping_algorithm)

1. Sutherland-Hodgman
  - [Wikipedia](https://en.wikipedia.org/wiki/Sutherland%E2%80%93Hodgman_algorithm)
  - [GitHub](https://github.com/mdabdk/sutherland-hodgman)

2. Weiler–Atherton clipping algorithm

  - [Wikipedia](https://en.wikipedia.org/wiki/Weiler%E2%80%93Atherton_clipping_algorithm)

To get intersecting area of polygons, can follow this up with a shoelace
algorithm.


## Significant Figures

```C#
public static string ToSigFigs(this double value, int sigFigs)
{
    if (value == 0) return "0";
    int log = (int)Math.Floor(Math.Log10(Math.Abs(value)));
    var digits = Math.Max(0, sigFigs - 1 - log);
    var rounded = Math.Round(value, digits);

    if (digits == 0) return rounded.ToString("F0");
    // The 'G' format will take care of trailing zeros.
    return rounded.ToString($"G{sigFigs}");
}

```
