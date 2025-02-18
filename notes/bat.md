# Adding a language

<https://github.com/sharkdp/bat>

Takes sublime text syntax files. <https://www.sublimetext.com/docs/syntax.html#contexts>

```
mkdir -p (bat --config-dir)/syntaxes
# Files must end with .sublime-syntax
bat cache --build
```

<https://www.sublimetext.com/docs/scope_naming.html>

```
comment.
constant.
entity.
invalid.
keyword.control
keyword.control.import
markup.
meta.
punctuation.
source.
storage.
string.
support.
text.
variable.
```
