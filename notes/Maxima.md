# General

Don't forget to end each line with ';' or '$'. ';' prints result, '$' hides result.

# Solving

```maxima
eq: a + b = c + d
solve(eq, c)

subst(b = e * f, eq);

diff(eq_expr, var, <num>);
```


From this [SO answer](https://stackoverflow.com/a/51256735/5932184), `ratsubst` might be better in most cases.
