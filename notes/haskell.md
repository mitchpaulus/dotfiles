# Haskell

[Learn X in Y for Haskell](https://learnxinyminutes.com/docs/haskell/)

## IO

- Get command line arguments: `getArgs` from `System.Environment`
- Run external programs: `System.Process`

## Records

- data Record = Record { field :: Type, field2 :: Type }

- Update record field `variable { singleField = something }`


## Learning Monads

- ["What are Monads? Fallacy](https://two-wrongs.com/the-what-are-monads-fallacy)
    - Start by learning the usage of the `Maybe`, `Either`, `IO` monads,
      using `>>=` and `do` operator.

- [Monads Demystified](https://blog.reverberate.org/2015/08/monads-demystified.html)

## Type Classes (site/company)

- [Julie blog](https://argumatronic.com/about.html)
- [Chris Martin blog](https://chris-martin.org/)
- [Their book](https://joyofhaskell.com/)
- [Another book: Haskell from first principles](https://www.goodreads.com/book/show/25587599-haskell-programming-from-first-principles)
- [Type Classes](https://typeclasses.com/): Haskell and Nix training. $30/month

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

## Useful links

[Reddit post](https://www.reddit.com/r/haskell/comments/npxfba/ive_tried_to_learn_haskell_several_times_but_keep/)
[Applicative Functors original paper](https://www.staff.city.ac.uk/~ross/papers/Applicative.pdf)

## Type Classes

Type classes are defined by specifying a set of function or constant names,
together with their respective types, that must exist for every type that belongs to the class.

```haskell
class Monad m where
  return :: a -> m a
  (>>=)  :: m a -> (a -> m b) -> m b
```

## Setup with Nix

<https://github.com/aveltras/setting-up-a-haskell-development-environment-with-nix>


## Cabal

Puts packages and binaries at `~/.cabal/`

## Stream Fusion

- Streams are what I think they are: linear access to a potentially unbounded list of data.
- General term for eliminating intermediate data structures that grow with stream processing is *deforestation*.
- In the context of stream processing, it's typically called *stream fusion*.

References:

P. L. Wadler. Deforestation: Transforming programs to eliminate trees. Theoretical Computer Science, 73(2):231–248, June 1990.
[URL:](http://homepages.inf.ed.ac.uk/wadler/topics/deforestation.html).

Kiselyov, Biboudis, Palladinos, Smaragdakis: Stream Fusion, to Completeness

[Functors, applicatives, and monads in pictures](https://www.adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html)
