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

* : 0 or more
\+ : 1 or more (GNU extension)
\? : 0 or 1 (GNU extension)
\{i\} : exactly i
\{i,\} : i or more
\(regexp\) : group
. : any character
^ : start of line
$ : end of line
[abc] : a or b or c
[^abc] : not a or b or c
rgexp1\|regexp2 : or
\digit : backreference
```

The `-z` option causes `sed` to separate the lines by NULLs instead of newlines.

```
# Appending
sed '1a hello'
sed '/pattern/a hello'
```

[POSIX sed](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/sed.html)
