# Markdown

## Editors

[Typora](https://typora.io) is an interesting one.

## Spell Checking

[source](https://manuel-strehl.de/check_markdown_spelling_with_aspell)

```sh
for file in *.md
do
    aspell check --mode=markdown --lang=en "$file"
done
```

## Named links

[Link text][Link id]

[Link id]: http://link.com "Optional"

## Linting

- <https://earthly.dev/blog/markdown-lint/>
