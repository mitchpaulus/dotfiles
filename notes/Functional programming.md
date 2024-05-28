Map can be defined from fold and (:) operator (list concatenation).

<https://en.wikipedia.org/wiki/Fold_(higher-order_function)>

```
map f = foldr ((:) . f) []
```
