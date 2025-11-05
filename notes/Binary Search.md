<https://en.wikipedia.org/wiki/Binary_search>
```
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := L + floor((R - L) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m − 1
        else:
            return m
    return unsuccessful
```
