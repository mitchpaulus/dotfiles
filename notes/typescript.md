# Typescript


## Basic Types

- `string`, `number`, `boolean`, `any`
```
interface Point {
  x: number;
  y: number;
}
```

## Type Guards

- `typeof`: works for basic types.
- `instanceof`: works for more types
- Custom type guard. Return "type" is `arg is Type`. Should typically
  have a single function argument.

https://www.typescripttutorial.net/typescript-tutorial/typescript-type-guards/
```
function isCustomer(partner: any): partner is Customer {
    return partner instanceof Customer;
}
```

## Function typing

```
var myfunc: (parameter: Type) => ReturnType
```

Be careful with Union types and function types, best practice is to
parenthesize the function types or use a type alias.

```
var myvar = ((param) => Type) | OtherType
```


