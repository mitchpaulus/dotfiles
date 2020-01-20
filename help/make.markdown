# Make

## Automatic Variables

`$^` | The names of all the prerequisites, with spaces between them. A
     target has only one prerequisite on each other file it depends on, no
     matter how many times each file is listed as a prerequisite.  So if you
     list a prerequisite more than once for a target, the value
     of $^ contains just  one copy of the name.

`$*` | The stem with which an implicit rule matches (see Section 10.5.4
     [How PatternsMatch], page 122).  If the target is dir/a.foo.b and the
     target pattern is a.%.b then the stem is dir/foo.  The stem is useful for
     constructing names of related files.In a static pattern rule, the stem is
     part of the file name that matched the ‘%’ in the target pattern.

All automatic variables have a 'D' and 'F' flavor that gets only the
'directory' or 'file within directory' part.
