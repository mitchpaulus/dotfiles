```python

def zero(a, b, macheps, t, f: Callable[[float], float)

# a = lower bound
# b = upper bound
# macheps = machine epsilon
# t = tolerance

fa = f(a)
fb = f(b)

#

c = a
fc = fa
d = b - a # x Difference
e = d # Current uncertainty size

# a is previous value of b
# b is best estimate of zero
# c is other end of interval, zero lies between b and c, a might be equal to c
# |f(b)| <= |f(c)|, meaning b is always closer to zero than c


```
