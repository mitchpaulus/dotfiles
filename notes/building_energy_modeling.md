# Building Energy Modeling

## Default PLR curves

For AHUs with constant setpoint:

$$ FFLP = 0.00153 + 0.005208 PLR + 1.108624 PLR² + -0.11636 PLR³ $$


## EnergyPlus

- Plant only model, use `LoadProfile:Plant` to simulate the measured
  loads.

