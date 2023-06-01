# General

Don't forget to end each line with ';' or '$'. ';' prints result, '$' hides result.

- `linel`: sets line length.
- `stardisp` controls whether spaces or \*'s are used to represent multiplication.

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

lratsubst (new, old, expr)
lratsubst (old = new, expr)
lratsubst ([ old_1 = new_1, …, old_n = new_n ], expr)

```
eq1: a =  b + c
eq2: b = d + e
result: lratsubst(eq2, eq1)
```

ratsubst (new, old, expr)

stringout (filename, expr_1, expr_2, expr_3, …)
stringout (filename, [m, n])
stringout (filename, input)
stringout (filename, functions)
stringout (filename, values)
From this [SO answer](https://stackoverflow.com/a/51256735/5932184), `ratsubst` might be better in most cases.

<http://www.hippasus.com/resources/symmath/index.html>
