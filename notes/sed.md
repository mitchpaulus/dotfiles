# `sed`

Grammar

```
<expression> : <address> <command>

<address> : <address-range> | <single-address>
<address range> : <single address> ',' <single address>
<single address> : <line number> | '$' | <step-address> | <regex>
<step address> : <integer> '~' <integer>   # first~step
<regex> : '/' <pattern> '/' | \% <pattern> %
```

Regex

```
\+
\.
```

The `-z` option causes `sed` to separate the lines by NULLs instead of newlines.

```
# Appending
sed '1a hello'
sed '/pattern/a hello'
```

[POSIX sed](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/sed.html)
