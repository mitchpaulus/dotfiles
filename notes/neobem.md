Some useful functions:

```
concat = \ list_of_lists { if length(list_of_lists) == 0 then [] else head(list_of_lists) + concat(tail(list_of_lists)) }
flatMap = \ f list { concat(map(f, list)) }
enumerate = \ list start { if length(list) == 0 then [] else [{ 'item': head(list), 'index': start }] + enumerate(tail(list), start + 1) }
```
