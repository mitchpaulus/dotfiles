# fzf

If installing fzf from the git repository, it adds the location to the path using the universal `$fish_user_paths`.
This is a list of directories that are prepended to the path.

FIELD INDEX EXPRESSION
       A field index expression can be a non-zero integer or a range expression ([BEGIN]..[END]). --nth and --with-nth take a comma-separated  list  of
       field index expressions.

   Examples
       1      The 1st field
       2      The 2nd field
       -1     The last field
       -2     The 2nd to last field
       3..5   From the 3rd field to the 5th field
       2..    From the 2nd field to the last field
       ..-3   From the 1st field to the 3rd to the last field
       ..     All the fields


You cannot control the output of the selected line, you have to select out whatever fields using awk or something afterwards.

```
-n --nth # These make the search only work in certain fields
--with-nth # Only display the selected fields in the input
-d --delimiter # Use a different delimiter than whitespace (awk-style, so "\t" works for tab)
```
