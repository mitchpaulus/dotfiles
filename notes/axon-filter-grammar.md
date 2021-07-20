## Filters

grammar: https://skyfoundry.com/doc/docHaystack/Filters

```
<filter>     :=  <condOr>
<condOr>     :=  <condAnd> ("or" <condAnd>)\*
<condAnd>    :=  <term> ("and" <term>)\*
<term>       :=  <parens> | <has> | <missing> | <cmp>
<parens>     :=  "(" <filter> ")"
<has>        :=  <path>
<missing>    :=  "not" <path>
<cmp>        :=  <path> <cmpOp> <val>
<cmpOp>      :=  "==" | "!=" | "<" | "<=" | ">" | ">="
<path>       :=  <name> ("->" <name>)\*

<val>        :=  <bool> | <ref> | <str> | <uri> |
                 <number> | <date> | <time>
<bool>       := "true" or "false"
<number>     := same as Zinc (keywords not supported INF, -INF, NaN)
<ref>        := same as Zinc
<symbol>     := same as Zinc
<str>        := same as Zinc
<uri>        := same as Zinc
<date>       := same as Zinc
<time>       := same as Zinc
<name>       := same as Zinc <id>
```

