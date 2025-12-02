# Log-priors and Log-likelihoods

Turns products of probabilities into sums.
Needed in computation because otherwise the values can get really small.

# Calculating log-priors

For each parameter, get the y-value out of the PDF. Then take its logarithm and add them all together.
Remember that this value can often be negative if the y-value out of the PDF is < 1.
This is how a low probability prior will affect the sum, values close to 0 make the output go way negative.

# Calculating log-likelihoods

Get a log-likelihood for each data point, so for building energy modeling, this would be 8,760 data points if we had hourly data to compare to.
This can cause the total analysis to be biased way too much to the fitting of the hourly values.

Some options:
- Do log-likelihoods on the monthly data (n = 12 instead of 8760.)

# Triangular distribution

For min a, max b, mode c, peak always 2 * (b-a)  or .

PDF:

x < c: (2 * (x-a)) / ((b - a) * (c - a))
x > c: (2 * (b - x)) / ((b - a) * (b - c))

# Definitions

- "iid" = Independent and identically distributed.
- MLE: Maximum Likelihood Estimator (Maximizing just the likelihood part - only looking at comparison with measured data)
- MAP: Maximum A Posteriori. Maximizing the posterior (Using likelihood and priors)


# PDF for Normal Distribution

PDF(x) = 1 / sqrt(2 * pi * sigma²) exp( - ((x - mean)² / (2 * sigma²)))

# References

<https://en.wikipedia.org/wiki/Triangular_distribution>

Muehleisen, Ralph T and Bergerson, Joshua, "Bayesian Calibration - What, Why And How" (2016).
International High Performance Buildings Conference. Paper 167.
http://docs.lib.purdue.edu/ihpbc/167

Kennedy, M. C., & O'Hagan, A. (2001). Bayesian Calibration of Computer Models. Journal of the Royal Statistical
Society: Series B, 63(3), 425-464.

Heo, Y., Augenbroe, G. A., & Choudhary, R. (2011). Risk Analysis of Energy-Efficiency Projects Based on
Bayesian Calibration of Building Energy Model. Building Simulation 2011. Retrieved from
<http://www.ibpsa.org/proceedings/BS2011/P_1799.pdf>

Heo, Y. (2011). Bayesian calibration of building energy models for energy retrofit decision making under uncertainty.
Forthcoming, PhD Dissertation, Georgia Institute of Technology.
