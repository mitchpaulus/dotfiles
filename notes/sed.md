# `sed`

Grammar

```
<expression> : <address> <command>

<address> : <address-range> | <single-address>
<address range> : <single address> ',' <single address>
<single address> : <line number> | '$' | <step-address> | <regex>
<step address> : <integer> '~' <integer>   # first~step
```

Regex

```
\+
\.
```

The `-z` option causes `sed` to separate the lines by NULLs instead of newlines.
