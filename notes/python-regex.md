
<https://docs.python.org/3/library/re.html>

Metacharacters:

```
.
^
$
*
+
?
*?
+?
??
{m}
{m,n}
{m,n}?
[]
()
|
# There are some lookaheads
\A # Start of string
\b # word boundary
\B # not word boundary
\d # Unicode decimal
\D # Not Unicode decimal
\s # Unicode whitespace
\S # Not Unicode whitespace
\w # Word character
\W # Not word character
\Z # End of string
```

```python
import re

re.search(pattern, string, flags=0) -> re.Match | None # Pattern can match anywhere in string
re.match(pattern, string, flags=0) -> re.Match | None # Pattern can match only at beginning of string
re.split(pattern, string, maxsplit=0, flags=0)

# If replacement is a function, it's called with the match, and returns the desired replacement string
re.sub(pattern, replacement: str | Callable[Match, str], string, count=0, flags=0) -> str

# Match objects

Match.start([group])
Match.end([group])
Match.span([group])  # Tuple of Match.start/Match.end
# Can get the text from the total match with match.group()
Match.group([group1,...]) -> str | Tuple[str, ...] # Return string of group. Group 0 is entire match.

```
