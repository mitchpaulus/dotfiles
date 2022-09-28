%[parameter][flags][width][.precision][length]type


- parameter `n$`
- flags (0 or more):
  - `-` Left align output
  - `+` Prepend plus for positive values
  - ` ` Prepend space for positive values
  - `0` With `width` specified, prepend 0's
  - `'` Thousands grouping separator
  - `#` Alternate form
- width: Minimum width
- precision:
- length: Don't really care about
- type (required)
  - d or i: signed integer
  - u: unsigned integer
  - f or F: fixed point
  - e or E: (`d.ddde+dd`). Exponent has at least two digits.
  - g or G: normal or exponential notation, removes insignificant zeros. Decimal point not included on whole numbers.
  - s: string
  - x or X: unsigned int as hexadecimal number
