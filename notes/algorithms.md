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

- [Clipping (computer graphics)](<https://en.wikipedia.org/wiki/Clipping_(computer_graphics)>)

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
   1. If $p\_{1y}$ \< $P_y$ and $p\_{2y}$ \< $P_y$, do nothing, both points
      are below ray.
   2. If $p\_{1y}$ >= $P_y$ and $p\_{2y}$ >= $P_y$, do nothing, both points
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

- Take floor of X, or nearest integer \<= X, save as \[X\]
- Get remainder {X} by X - \[X\]
- {X} \< 1, so take 1 / {X} to get Y

## Version Sorting

[From gnu.org ](https://www.gnu.org/software/coreutils/manual/html_node/Version_002dsort-ordering-rules.html)

The version sort ordering rules are:

1. The strings are compared from left to right.
2. First the initial part of each string consisting entirely of non-digit characters is determined.
   1. These two parts (one of which may be empty) are compared
      lexically. If a difference is found it is returned.
   2. The lexical comparison is a comparison of ASCII values modified so that:
      - all the letters sort earlier than all the non-letters and
      - so that a tilde sorts before anything, even the end of a part.
3. Then the initial part of the remainder of each string which consists
   entirely of digit characters is determined. The numerical values of
   these two parts are compared, and any difference found is returned as
   the result of the comparison.
   1. For these purposes an empty string (which can only occur at the
      end of one or both version strings being compared) counts as zero.
4. These two steps (comparing and removing initial non-digit strings and
   initial digit strings) are repeated until a difference is found or
   both strings are exhausted.

## String Compraison

1. [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance).
   - [Imlementations in various languages](https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance)
2. [Needleman-Wunsch or Smith-Waterman](https://stackoverflow.com/a/10445032/5932184)
