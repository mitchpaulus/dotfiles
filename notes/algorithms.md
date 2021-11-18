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

4. Vatti algorithm

  - Bala R. Vatti. "A generic solution to polygon clipping", Communications of the ACM, Vol 35, Issue 7 (July 1992) pp. 56–63.

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

## Is Point in Polygon?

Great algorithm, first saw at: https://web.cs.ucdavis.edu/~okreylos/TAship/Spring2000/PointInPolygon.html

Determine whether point $P$ is in polygon $Q$

1. Initialize intersectionCount to 0.
2. For each edge $e$ of $Q$, defined by $p_1$ and $p2$, check the
   following:
   1. If $p_{1y}$ < $P_y$ and $p_{2y}$ < $P_y$, do nothing, both points
      are below ray.
   2. If $p_{1y}$ >= $P_y$ and $p_{2y}$ >= $P_y$, do nothing, both points
      are above ray.
   3. Otherwise, calculate the intersection point $S$ of the edge $e$
      and the horizontal line $y=P_y$. If $S_x >= P_x$, increment
      intersectionCount.
3. After all edges have been checked, $P$ is inside $Q$, if and only
   if intersectionCount is *odd*.


## Rational Approximations

[From here.](https://www.maa.org/sites/default/files/321917011764.pdf.bannered.pdf)

Given real number X:

algorithm:
 - Take floor of X, or nearest integer <= X, save as [X]
 - Get remainder {X} by X - [X]
 - {X} < 1, so take 1 / {X} to get Y

