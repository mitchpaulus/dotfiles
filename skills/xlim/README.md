# `xlim`

Basic syntax:

```xlim
-- This is a comment

-- A file is a list of definitions. Order does not matter.
definition3 = definition1 + definition2
definition1 = 1
definition2 = 2

-- Very loose restrictions on names, can start with numbers or use other Unicode characters
ρ_water = 997 {kg/m^3} -- Density of water
1_array = [1]
this_statement_is_true? = false
😊 = 123 -- even emojis are allowed

-- list definitions
a_list = [1, 2, 3]

-- true/false keywords
-- if ... then ... else
-- equality: ==
-- not equal: !=
-- normal comparison operators: <, <=, >, >=
if_statement = if 2 > 1 then true else false

-- compound logic, 'and' and 'or' are keywords. No 'not' for now, use '== false' instead
compound_logic = if 2 > 1 and 1 > 0 then true else false

exponentiate = 2^3

range = 60 to 80 by 2 in {degF}

-- array programming, all operations are element by element
element_sum = [1, 2, 3] + [4, 5, 6] -- [5, 7, 9]

-- any operation with a scalar is applied across entire array
var = 2 * [1, 2, 3] -- [2, 4, 6]

-- functions
-- function_name: args, .. ;
list = [1, 2, 3] {}
sum_over_array = sum: list; -- 6
min_val = min2: 1, 2; -- 1
max_val = max2: 1, 2; -- 2

-- You can define your own functions!
add2kilograms: inputMass {kg} = inputMass + 2 {kg}
new_mass = add2kilograms: 1 {lbm}; --  1 lbm + 2 kg (~4.4 lbm) = 5.4 lbm
-- These are type checked, so this will fail
-- result = add2kilograms: 3 { W };

-- units
-- simple unit on numeric value
var_with_unit = 2 {kW}

-- compound units are created using unit names, '/', '^' followed by integers, '(', and ')'.
-- Can also use Unicode superscripts up to power of 5 (ex: s^2 can be s²)
compound_unit = 2 {kg m/s^2} -- or 2 { kg m/s² }
-- implicit multiplication has higher precedence than division
division = 2 {kg W/m s} -- This is parsed like: 2 { (kg W) / (m s) }

-- units and conversions are handled automatically.
-- if units have same base units, operation will convert to the "left hand" side.
unit_magic = 1 {tr} + 12000 {btu/h} -- 2 { tr }

-- If you want a different unit for the final definition, specify next to the identifier
unit_magic_2 {kW} = 1 {hp} + 550 {ft lbf/s} -- 2 hp = 1.491 kW

-- You're not allowed to add unlike units
-- not_allowed = 1 { hp } + 1 { btu } -- Results in error

-- Sometimes you need to repeat *sets* of calcuations.
-- You can define a template of definitions and then apply it with different parameters
template my_template param1 {kW} param2 {kW}
  def_1 = param1 + param2
  def_2 = param1 - param2
end

template_application_1 is my_template: 1 {kW}, 2 {kW};
template_application_2 is my_template: 3 {kW}, 4 {kW};
-- This is equivalent to:
-- template_application_1.def_1 = 1 {kW} + 2 {kW}
-- template_application_1.def_2 = 1 {kW} - 2 {kW}
-- template_application_2.def_1 = 3 {kW} + 4 {kW}
-- template_application_2.def_2 = 3 {kW} - 4 {kW}

-- Loading data from a file is as simple as wrapping the relative file path in back ticks
-- Assumes the file is tab separated and looks something like:
-- Spaces allowed, will become underscores
-- variable1 ( m )	variable2 ( kg )
-- 1	2
-- 3	4
`data.tsv`
```

# Available Syntax Highlighting

Syntax highlighting is available for the following editors:

- [VS Code](https://code.visualstudio.com/) (install the [`xlim` extension](https://marketplace.visualstudio.com/items?itemName=MitchellPaulus.xlim))
- [Notepad++](https://notepad-plus-plus.org/) (Use file [`notepad++/xlim.xml`](notepad++/xlim.xml))
- [Vim](https://www.vim.org/)/[Neovim](https://neovim.io/) (See the [`xlim-vim` GitHub repository](https://github.com/mitchpaulus/xlim-vim))
- [Kate](https://kate-editor.org/) (Use file [`kde-syntax/xlim.xml`](kde-syntax/xlim.xml)).
  This can also be used as a syntax definition for [Pandoc](https://pandoc.org/).
- \<Your favorite editor here\>: I'm open to adding support for more editors. Please open an issue.

# Temperature

Temperature units are unfortunate exception to linear units.
They are *affine*, which can be described in several ways.
One way is that "zero" is not special.

# Related Software

- [Pint](https://pint.readthedocs.io/en/stable/): Python library for handling quantities with units.
- [Frink](https://frinklang.org/): Object-orientated language with units, interval arithmetic, arbitrary precision math.

## Prior Art

Frink requires the use of functions for Fahrenheit and Celsius (<https://frinklang.org/#TemperatureScales>).

```
Fahrenheit[451]
:: 505.9277777777778 K (temperature)
```

- [physmod Matlab](https://www.mathworks.com/help/physmod/simscape/ug/thermal-unit-conversions.html)

Axon has the units of `Δ°F`

## Desired Outcomes

- Can still use normal temperature units for differences
  - `50 {°F} - 30 {°F}`
  - Resulting unit should be `Δ°F`
- Specific heat units therefore are:
  - `BTU / lb Δ°F`
- Composite units with an affine component cannot be added, only be subtracted if exactly equal

## TODO

- LSP
  - [ ] Rename
- [ ] Syntax for array of copies
- [ ] Seamless rational/floating number arithmetic
- [ ] Syntax for loading from more file types
- [ ] Distributions/Monte Carlo runs
- [ ] More units
- [ ] Add Date data type
- [ ] Excel configuration options
- [ ] Add corresponding dynamic array formulas for Excel
  - [ ] `FILTER`
  - [ ] `SORT`
  - [ ] `SORTBY`
  - [ ] `UNIQUE`

## Additional References

- [How can you measure the doubling of a temperature?](https://www.reddit.com/r/askscience/comments/9p6xoo/how_can_you_measure_the_doubling_of_a_temperature/)
- [New Excel dynamic arrays](https://support.microsoft.com/en-us/office/dynamic-array-formulas-and-spilled-array-behavior-205c6b06-03ba-4151-89a1-87a7eb36e531)
