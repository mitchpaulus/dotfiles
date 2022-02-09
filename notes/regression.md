# Regression

## Issue with R2 for models with no constant term

My MLR code was returning a different R2 value from Excel when using models without
a constant term. Eventually found a answer from [Stats Stack Exchange](https://stats.stackexchange.com/questions/26176/),
basically the normal formula doesn't necessarily make sense, so it is quietly changed to be:

$
R² = 1 - \frac{\sum_{i}  \left( y_i - \hat{y}_i \right)^2  }{\sum_i y_i^2 }
$

[Additional Reference](https://stats.stackexchange.com/questions/7357/manually-calculated-r2-doesnt-match-up-with-randomforest-r2-for-testing)
