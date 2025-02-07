# Compilers

[Cool graph showing what compiles to what:](https://github.com/mohd-akram/languages)
[Textbook on Compiler design](http://cs.rowan.edu/~bergmann/books/Compiler_Design/java/CompilerDesignBook.pdf)

[Slides from Graydon Hoare, creator of Rust](http://venge.net/graydon/talks/CompilerTalk-2019.pdf?utm_source=thenewstack&utm_medium=website&utm_campaign=platform)

## Predictive Parsing / Recursive Descent

- One procedure called `Match`

  ```
  procedure match(t: token) {
    if lookahead = t then
      lookahead := nexttoken
    else
      error
    end
  }
  ```

- One procedure for each non-terminal

  ```
  procedure type() {

    if lookahead is in { integer, char, num } then
      simple
    else if lookahead = '|' then
      match('|'); match(id);

    else error

   end

  }
  ```


# Pratt Parsing

- <https://www.oilshell.org/blog/2017/03/31.html#original-series>
- <https://www.engr.mun.ca/%7Etheo/Misc/exp_parsing.htm>
- [The top-down parsing of expressions](http://antlr.org/papers/Clarke-expr-parsing-1986.pdf)
- <http://javascript.crockford.com/tdop/tdop.HTML>
- <http://effbot.org/zone/simple-top-down-parsing.htm>
- <http://eli.thegreenplace.net/2010/01/02/top-down-operator-precedence-parsing>
- <http://journal.stuffwithstuff.com/2011/03/19/pratt-parsers-expression-parsing-made-easy/>
- <https://matklad.github.io/2020/04/13/simple-but-powerful-pratt-parsing.HTML>

# References

[Peephole optimization](https://en.wikipedia.org/wiki/Peephole_optimization)
[How Compilers Work - Walter Bright](https://accu.org/conf-docs/PDFs_2010/CompilerConstruction_WalterBright.pdf)
[Parser in Rust](https://www.nhatcher.com/post/a-rustic-invitation-to-parsing/)
[Subroutine calls in the ancient world, before computers had stacks or heaps](https://devblogs.microsoft.com/oldnewthing/20240401-00/?p=109599)
