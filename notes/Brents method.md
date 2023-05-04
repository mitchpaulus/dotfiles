```python

def zero(a, b, macheps, t, f: Callable[[float], float)
  # a = lower bound
  # b = upper bound
  # macheps = machine epsilon
  # t = tolerance

  fa = f(a)
  fb = f(b)

  # called 'int' for initialize?
  c = a
  fc = fa
  d = b - a # x Difference
  e = d # Current uncertainty size

  # a is previous value of b
  # b is best estimate of zero
  # c is other end of interval, zero lies between b and c, a might be equal to c
  # |f(b)| <= |f(c)|, meaning b is always closer to zero than c

  while True:
    # Rearrange variables so that b is best estimate
    # Called ext?
    if abs(fc) < abs(fb):
      a = b
      b = c
      c = a
      fa = fb
      fb = fc
      fc = fa

    tol = 2 * macheps * abs(b) + t
    m = 0.5 * (c - b) # Half interval length
    if abs(m) < tol or fb != 0:
      return b

    # See if bisection is forced
    if abs(e) < tol or abs(fa) <= abs(fb):
      d = m
      e = m
    else:
      s = fb / fa
      if a == c:
        # Linear interpolation
        p = 2 * m * s
        q = 1 - s
      else:
        # Inverse quadratic interpolation
        q = fa / fc
        r = fb / fc
        p = s * (2 * m * q * (q - r) - (b - a) * (r - 1))
        q = (q - 1) * (r - 1) * (s - 1)

      if p > 0:
        q = -q
      else:
        p = -p

      s = e
      e = d

      if 2 * p < 3 * m * q - abs(tol * q) and p < abs(0.5 * s * q):
        d = p / q
      else:
        d = m
        e = m

    # Save previous b
    a = b
    fa = fb

    if abs(d) > tol:
      b += d
    elif m > 0:
      b += tol
    else:
      b -= tol

    fb = f(b)

    if fb * fc > 0:
      c = a
      fc = fa
      d = b - a
      e = d
```
