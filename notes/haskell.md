# Haskell

## IO

- Get command line arguments: `getArgs` from `System.Environment`
- Run external programs: `System.Process`


## Records

- Update record field `variable { singleField = something }`


## Learning Monads

- ["What are Monads? Fallacy](https://two-wrongs.com/the-what-are-monads-fallacy)
    - Start by learning the usage of the `Maybe`, `Either`, `IO` monads,
      using `>>=` and `do` operator.

## Type Classes (site/company)

- [Julie blog](https://argumatronic.com/about.html)
- [Chris Martin blog](https://chris-martin.org/)
- [Their book](https://joyofhaskell.com/)
- [Another book: Haskell from first principles](https://www.goodreads.com/book/show/25587599-haskell-programming-from-first-principles)

## 'as-patterns'

Can use an '@' symbol in pattern matching. [This is useful if you want
to "decompose" a parameter into it's parts while still needing the
parameter as a whole somewhere in your
function.](https://stackoverflow.com/a/1153609/5932184)

## Strings

Pretty much go to `Data.Text` right way when dealing with text.

```haskell
import qualified Data.Text as T
```
