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
