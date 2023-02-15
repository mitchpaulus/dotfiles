# General

Don't forget to end each line with ';' or '$'. ';' prints result, '$' hides result.

# Solving

```maxima
eq: a + b = c + d
solve(eq, c)

subst(b = e * f, eq);

diff(eq_expr, var, <num>);

/* Simplifying */
eq1: a = b/c + 2;
eq1: ratsubst(d, b/c, eq1); /* a = d + 2 */
```


Solving n simultaneous equations:

```maxima
eq_effab: eff_ab = (Tai - Tao) / (Tai - Tasink);
eq_effhx: eff_hx = (Thxi - Thxo) / (Thxi - Thwr);
eq_mix: Thxi = Tao * X + (1 - X)*Tai;
eq_energy: Tai - Thxo = Qg / C;
solve([eq_effab, eq_effhx, eq_mix, eq_energy], [Tai, Tao, Thxi, Thxo]);
assume(var > 0, var2 < var3)

jacobian([expr1, expr2], [var1, var2])

(%i1) a: matrix ([3, 1], [2, 4]);
                            [ 3  1 ]
(%o1)                       [      ]
                            [ 2  4 ]

```


From this [SO answer](https://stackoverflow.com/a/51256735/5932184), `ratsubst` might be better in most cases.
