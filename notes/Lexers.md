Standard lexer structure based on Crafting Interpreters that I've liked:

```go
type Lexer struct {
	start   int
	current int
	col     int
	line    int // One-based line number.
	input   []rune
}

type Token struct {
	// One-based line number.
	Line   int
	Column int
	Start  int
	Lexeme string
	Type   TokenType
}
```
