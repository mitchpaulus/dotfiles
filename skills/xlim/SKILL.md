---
name: xlim
description: |
  `xlim` is a domain specific language designed for mathematical calculations with units.
  It should be used when you want to calculate engineering expressions with units.
  It is array based, and has a simple CLI interface.
---

`xlim` is an array based, domain specific language. It can be executed using the `xlim` CLI utility.

Please see the README.md file in this skill for example syntax.

Some useful sub-commands

```
xlim --functions # Show all available functions
xlim --units # Print all available units
```

This is my language that I have full control over the development of.
If you run into ANY issues, hardships, or misunderstandings, you MUST inform me so that I can make the improvements.
If there a new features that you think would simplify your work, please inform me.

You should NEVER have to manually put in a "conversion constant".
When using this, you should be using the full form of engineering formulas.
For example, for chiller tonnage, the shorthand formula is often used:

```
TONS = GPM * (DT) / 24
```

The correct way to do this in xlim would be:

```xlim
flow = 100 {GPM}
dt = 10 {°F}
cp = 1 {BTU/lbm °F}
rho = 1000 {kg/m^3}
tons {tr} = flow * cp * rho * dt
```

Things you have missed in the past:

- You can coerce the output unit (like the `tr` in `tons {tr} = flow * cp * rho * dt`)
