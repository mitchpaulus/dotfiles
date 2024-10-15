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

To get intersecting area of polygons, can follow this up with a shoelace algorithm.

For [rectangles](https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other).

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

## Rounding

<https://en.wikipedia.org/wiki/Rounding>

```
round2Multiple(x, m) = round(x / m) * m
roundHalfUp(x) = floor(x + 0.5)
```

```awk
# Language with integer truncation - this doesn't take care of negatives.
value = int((value / 100000) + 0.5) * 100000

# With true floor function this works as is for both +/-
<https://www.youtube.com/watch?v=hTFTwWU_Arc>
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

See <https://github.com/mitchpaulus/MtpSharp/blob/main/MtpSharp/Extensions.cs> for C# implementation.

## String Comparison

1. [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance).
   - [Imlementations in various languages](https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance)
2. [Needleman-Wunsch or Smith-Waterman](https://stackoverflow.com/a/10445032/5932184)


## Batching List

```c#
public static List<List<T>> Batch<T>(this List<T> list, int groups)
{
    int groupSize = Math.DivRem(list.Count, groups, out int remainder);
    List<List<T>> batches = new();
    // Group into batches, the last batch gets the remaining items
    for (int i = 0; i < groups; i++)
    {
        batches.Add(list.GetRange(i * groupSize, i < groups - 1 ? groupSize : groupSize + remainder));
    }
    return batches;
}
```

## Greatest Common Divisor

<https://en.wikipedia.org/wiki/Greatest_common_divisor>

- Euclid's algorithm is simplest, but can be slow with numbers that are different magnitudes
- [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) is more efficient.
- [lehmer's GCD Algorithm](https://en.wikipedia.org/wiki/Lehmer%27s_GCD_algorithm) Even more efficient
- [Binary](https://en.wikipedia.org/wiki/Binary_GCD_algorithm)

## Generating all combinations

[Heap's algorithm](https://en.wikipedia.org/wiki/Heap%27s_algorithm)

## Integer Factorization

<https://cp-algorithms.com/algebra/factorization.html>

## Generalized Reduced Gradient/Simplex

Used to solve constrained non-linear optimization problems.

- *Slack Variable* - extra term added to inequality constraints to make the form an equality constraint.

Solving m linear equations with n unknowns (n\>m)

- Set (n - m) variables to 0 to eliminate them.
- Solve m x m system of equations

- *Non basic* variables are the ones that are set to 0
- *Basic* variables are the ones that remain.

- Can always rewrite inequality as less than or equal to.
  - Multiply both sides by -1 to switch sign direction.

## Recursion to Iteration

From ChatGPT:
One common method for converting recursion to iteration is to use a stack data structure to simulate the function call stack that is used in recursive function calls.

Here is a general outline of the process:

1. Create a stack data structure to store the state of the function at each recursive call.
2. Modify the recursive function to accept an additional parameter, which will be used to store the state of the function on the stack.
3. Instead of making a recursive function call, push the state of the function onto the stack and return to the beginning of the function.
4. At the beginning of the function, check if the stack is empty. If it is, return the final result. If it is not empty, pop the top element off the stack and use it to restore the state of the function.
5. Continue the function execution from the point where it left off, using the restored state.

## Value at Placeholder Any Base

Divide the number in base 10 by b^(m-1) and take the remainder when divided by b.

```
num // 4 % 2 # Gives 4's place in binary
```

## Clustering

Often interested in clustering sets. Like sets of strings of HVAC point types.
[Useful set similarity metrics](https://stats.stackexchange.com/questions/285367/most-well-known-set-similarity-measures):

 - [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index): len(intersection) / len(union)
 - [Sorensen-Dice coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient)
 - [Overlap coefficient](https://en.wikipedia.org/wiki/Overlap_coefficient)
 - [Tversky index](https://en.wikipedia.org/wiki/Tversky_index)


## Newton-Raphson

Root finding:

From Numerical Methods text,
pg. 157, pg. 259.

[Xi+1] = [Xi] - [J]^-1 [F(Xi)]

where [J]^-1 is the inverse Jacobian. Jacobian is the matrix of partial derivatives over the functions.

From <http://cosmos.phy.tufts.edu/~danilo/AST16/Material/RootFinding.pdf>.
Saved to G-drive PDF references, `RootFinding.pdf`

It only makes sense to use Halley’s method when it is easy to calculate f 00.xi/,
often from pieces of functions that are already being used in calculating f .xi/ and f 0 .xi/.
Otherwise, you might just as well do another step of ordinary Newton Raphson.
Halley’s method converges cubically; in the final convergence each iteration triples the number of significant digits.
But two steps of Newton-Raphson *quadruple* that number.

There is no reason to think that the basin of convergence of Halley’s method is
generally larger than Newton’s; more often it is probably smaller.
So don’t look to Halley’s method for better convergence in the large

From <https://www.cs.princeton.edu/courses/archive/fall12/cos323/notes/cos323_f12_lecture02_rootfinding.pdf>
- Can be fragile
  - Keep track of whether error is increasing or decreasing
  - If error is increasing, try taking a smaller step, some fraction of the J-1 F(Xi) term.
- Also: Can't really bracket and bisect, so there are few general methods to solve.

## Powell's Method

Multidimensional form of Brent's method, which apparently lots of people like.

## SLR Simple Linear Regression

```
slope = (n * sum(x*y) - sum(x) * sum(y)) / (n * sum(x^2) - sum(x)^2)
constant = (sum(y) - slope * sum(x)) / n
```

## Polynomial Regression order 2

```
[[a0 = -((sum_x2*sum_x4-sum_x3^2)*sum_y
           +sum_x*(sum_x2y*sum_x3-sum_x4*sum_xy)+sum_x2*sum_x3*sum_xy
           -sum_x2^2*sum_x2y)
           /(sum_x2*((-n*sum_x4)-2*sum_x*sum_x3)
            +sum_x^2*sum_x4+n*sum_x3^2+sum_x2^3),
a1 = -((sum_x2*sum_x3-sum_x*sum_x4)*sum_y
    +n*(sum_x4*sum_xy-sum_x2y*sum_x3)-sum_x2^2*sum_xy
    +sum_x*sum_x2*sum_x2y)
    /(sum_x2*((-n*sum_x4)-2*sum_x*sum_x3)
    +sum_x^2*sum_x4+n*sum_x3^2+sum_x2^3),
a2 = ((sum_x2^2-sum_x*sum_x3)*sum_y+sum_x2*((-sum_x*sum_xy)-n*sum_x2y)
                                    +n*sum_x3*sum_xy+sum_x^2*sum_x2y)
    /(sum_x2*((-n*sum_x4)-2*sum_x*sum_x3)
    +sum_x^2*sum_x4+n*sum_x3^2+sum_x2^3)]]
```


## ITP

An Enhancement of the Bisection Method Average Performance Preserving Minmax Optimality Oliveira and Takahashi

## Binning

```python
# Bin data
bins = dict()
for d in data:
    bin_num = int(d // binsize)
    if bin_num not in bins:
        bins[bin_num] = 0
    bins[bin_num] += 1

# Print data. Order by bin number, tab-separated. Bin value should be mid-point of bin
for bin_num in sorted(bins.keys()):
    line = f"{bin_num * binsize + binsize / 2}\t{bins[bin_num]}"
    print(line, end="\n")

```

## Interpolation

- Assume sorted data
- Track index of last value less than or equal to target
- Loop over gridded interpolation data

## To CSV Cell

```
public static string ToCsvCell(this string str)
{
    bool mustQuote = str.Contains(',') || str.Contains('\"') || str.Contains('\r') || str.Contains('\n');
    if (!mustQuote) return str;

    StringBuilder sb = new();
    sb.Append('\"');
    foreach (char nextChar in str)
    {
        sb.Append(nextChar);
        if (nextChar == '"') sb.Append('\"');
    }
    sb.Append('\"');
    return sb.ToString();
}

def to_csv_cell(text):
    must_quote = "," in text or '"' in text or '\r' in text or '\n' in text
    if not must_quote:
        return text

    chars = ['"']
    for char in text:
        if char == '"':
            chars.append('"')
        chars.append(char)
    chars.append('"')
    return ''.join(chars)

```

## Sorting Networks

Cool idea that came up when I was thinking about sorting in xlim.
<https://en.wikipedia.org/wiki/Sorting_network>

## NMBE/CVRMSE

```
sum_actual = 0
sum_diff = 0
sum_diff_squared = 0
for i in data:
    diff = model - actual
    sum_actual += actual
    sum_diff += diff
    sum_diff_squared += diff * diff

mean_actual = sum_actual / n
nmbe = sum_diff / n / mean_actual * 100
rmse = sqrt(sum_diff_squared / n)
cvrmse = rmse / mean_actual * 100

```

## Ear Clipping


<https://www.youtube.com/watch?v=QAdfkylpYwc>
<https://www.youtube.com/watch?v=hTJFcHutls8>

Cross Product exploration: <https://www.geogebra.org/m/psMTGDgc>

Can determine whether angle is convex or concave by looking at the cross product of the vectors, at the z component.

### Point in Triangle

Get directional vectors in order of triangle vertices.
For each one, get cross product of vector from triangle point to test point.
Make sure the 'z' component of the cross product is the same sign for all three vectors.

If counter-clockwise orientation, all these cross products should be positive. (outside_vec x vec_to_int_point)
If counter-clockwise orientation, the angle of vertex is < 180 degrees if cross product is positive, when using vectors v1->2 x v2->3.

To test


### Signed Area

Shoelace formula, or signed area of a polygon. Positive if counter-clockwise, negative if clockwise.

A = 1/2 * sum(all pairs of determinants of points, x y as column vectors, or the z component of the cross product of the vectors)

A = 1/2 * sum( | xi Xi+1 | + ..  | xn x0 |)
               | yi Yi+1 |       | yn y0 |

```
