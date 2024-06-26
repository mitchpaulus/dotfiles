More powerful alternative to markdown

For math, uses asciimath

<https://asciimath.org/>
<https://www1.chapman.edu/%7Ejipsen/>

```fish
docker run --rm -u (id -u):(id -g) -v .:/documents/ asciidoctor/docker-asciidoctor:latest asciidoctor-pdf test.adoc
```
