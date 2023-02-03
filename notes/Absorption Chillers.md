# Absorption Chillers

Generator - main portion that accepts the heat input

## Modeling

Zero-order model:

6 Eqs, 12 unknowns - 3 Qs, 3 external Ts, 3 internal Ts, 3 UAs

Energy Balance: Qh + Ql = Qi

Entropy Balance: Qh / Thi + Ql/Tli = Qi/Tii

3 Heat transfer equations:

Qh = UAh (Th - Thi)
Ql = UAl (Th - Tli)
Qi = UAi (Tii - Ti)

Final equation somewhat arbitrary, but useful assumption:

Thc - Tic = Tic - Tlc
