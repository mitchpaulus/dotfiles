---
name: 'Neobem (`nbem`)'
description: |
  Neobem is a domain specific language for generating EnergyPlus idf files.
  It is a simple epxression based language that is a superset of the `idf` file format.
  It should be used when you want to generate idf files with paramaterization and abstraction.
---

Neobem (`nbem` CLI compiler), is a domain specific language for generating EnergyPlus idf files.

At a high level the `nbem` file is a list of the following constructs:

- `idf` object declaration
- variable declaration
- import statement
- export statement
- print statement
- log statement

Any time a `idf` object declaration is encountered, it is printed to standard output.
There is also a substitution that occurs during the printing.

The most important and common operations is mapping a template over a list of data:

```neobem
zones = [
    {
        'name': 'Bedroom',
        'x_origin': 0,
        'y_origin': 0
    },
    {
        'name': 'Living Room',
        'x_origin': 10,
        'y_origin': 20
    },
    {
        'name': 'Kitchen',
        'x_origin': 5,
        'y_origin': 12
    }
]

zone_template = λ zone {
Zone,
  <zone.'name'>,     ! Name
  0,                 ! Direction of Relative North {deg}
  <zone.'x_origin'>, ! X Origin {m}
  <zone.'y_origin'>, ! Y Origin {m}
  0,                 ! Z Origin {m}
  1,                 ! Type
  1,                 ! Multiplier
  autocalculate,     ! Ceiling Height {m}
  autocalculate,     ! Volume {m3}
  autocalculate,     ! Floor Area {m2}
  ,                  ! Zone Inside Convection Algorithm
  ,                  ! Zone Outside Convection Algorithm
  Yes;               ! Part of Total Floor Area
}

print zones |= zone_template
```

You can find the complete documentation at: `neobem.html` in this skill directory.

## Running different model versions with flags

You often want to run several different models with different tweaks based on binary flags.
For example, running a baseline and then a design model.
`nbem` supports this with the following workflow.

The CLI has a `--flag` option that lets you specify a comma separated list of flags.

```sh
nbem --flags envelope,lights in.nbem
```

and in the nbem file:

```neobem
uvalue = if exists('envelope') then 0.08 else 0.124

print if exists('lights') then my_design_light_template() else baseline_light_template()
```
