# GenOpt

Text file based optimization.

3 files required:

1. Configuration File: Usually set up once per type of program, i.e. EnergyPlus, xlim, Transys
2. Initialization file:
  - Where the runtime optimization files are located
  - What files should be saved after finished
  - Additional strings to be passed to the command line invocation
  - Where the cost function is in the output file
  - Whether that cost function needs to be post-processed
  - What simulation program is being used.

3. Command file
  - optimization variables
  - stopping criteria
  - optimization algorithm


## Notes

If `WriteStepNumber` is true, the `%stepNumber%` placeholder must exist in the template file.


## Algorithms

```
// 1-D continuous
Algorithm { Main = GoldenSection | Fibonacci; }
```
