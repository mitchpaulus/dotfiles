# Type Theory

## Algebraic Types

1. Product Types == Tuples, Records.           data Type = Type { field1 :: Type2, field2 :: Type2 }
2. Sum Types == Coproduct == Disjoint Unions.  data Type = Either | Or

Typically denote things as

Term: Type

Types are typically thought of as set of values that a term might evaluate to.

## Covariant, Contravariant, Invariant Generic Types

Sources:
 - <https://mypy.readthedocs.io/en/stable/generics.html#variance-of-generic-types>
 - [Why are Arrays invariant, but Lists covariant](https://stackoverflow.com/q/6684493/5932184)
 - [Covariance, Invariance and Contravariance explained in plain English](https://stackoverflow.com/q/8481301/5932184)
 - [Covariance and contravariance in C#, part 1](https://ericlippert.com/2007/10/16/covariance-and-contravariance-in-c-part-1/)


When dealing with generic types we come up across different
situations for dealing with derived types.

**Covariant**:

A generic class MyCovGen[T, ...] is called covariant in type variable T if MyCovGen[B, ...] is always a subtype of MyCovGen[A, ...].

**Contravariant**:

A generic class MyContraGen[T, ...] is called contravariant in type variable T if MyContraGen[A, ...] is always a subtype of MyContraGen[B, ...].

**Invariant**:

If neither of the above is true.

Good comment [here](https://stackoverflow.com/a/42720468/5932184):

> The real answer has to do with the way function types interact with
> subtyping. The short story is if a type parameter is used as a return
> type, it is covariant. On the other hand, if a type parameter is used as
> an argument type, it is contravariant. If it is used both as a return
> type and as an argument type, it is invariant.

## Dependent Types

Dependent types allow you to parameterize a type from a value. For
example (<https://stackoverflow.com/a/9374698/5932184>):

```
type BoundedInt(n) = { i:Int | i <= n }
```

## Hindley/Milner type system

Widely accepted approach for "parametric polymorphism", which is when a
function is defined over multiple types, acting in the *same way* for
each type.

This is in contrast to "ad hoc polymorphism", in which functions can act
*differently* for each type. See '[Ad hoc polymorphism](https://doi.org/10.1145/75277.75283)'.
