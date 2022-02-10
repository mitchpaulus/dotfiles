# Wang Chiller Model

From paper "Optimization of Condenser Water Loop Control in Hot and Humid Climates"

Used biquadratic fit with PLR and *Chiller Lift Ratio*, $(CWRT - CHWST)/Design Lift$

$$
\frac{P_{output}}{P_{design}} = C + A (PLR) + B (PLR)² + D (LR) + E LR² + PLR LR
$$
