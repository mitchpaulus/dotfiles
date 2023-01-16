# Heat Exchangers

- [NTU method Wikipedia](https://en.wikipedia.org/wiki/NTU_method)
- [LMTD](https://en.wikipedia.org/wiki/Logarithmic_mean_temperature_difference)

- Typically start with the LMTD, move to NTU if you can't use LMTD.

- $C$ is heat capacity rate (mass flow * specific heat) in units of W / °F or BTU/hr °F (coming from BTU/hr ft2 °F * ft2)
- UA is in same units.

$$
\textrm{NTU} = \frac{UA}{C_{min}}
$$


Counter Flow

$$

ε = (1 - exp(-NTU * (1 + Cmin/Cmax))) /
    (1 - (Cmin/Cmax)*exp(-NTU * (1 - Cmin/Cmax)))

ε = (1 - exp(-NTU * (1 + R)) /
    (1 - (R)*exp(-NTU * (1 - R)))

at R = 1

ε = (1 - exp(-NTU * (1 + R)) /
    (1 - (R)*exp(-NTU * (1 - R)))


ε, R, NTU

$$

Solving for NTU / UA in the counterflow case (multiply by Cmin for UA):

$$
NTU = (ln( 1 - R ε / 1 - ε )) / (1 - R)
$$

Solving for NTU/UA in the single stream case:

$$
ε = 1 - exp(-NTU)

N = ln(1 / 1 - ε)
$$


# Log Mean Temperature Difference

LMTD = (ΔTa - ΔTb)
      ------------
      ln(ΔTa / ΔTb)

q = UA (LMTD)

q, UA, ΔTa, ΔTb

q, UA, Ta1, Ta2, Tb1, Tb2
