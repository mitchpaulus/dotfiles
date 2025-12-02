# GenOpt

<https://simulationresearch.lbl.gov/GO/download/manual-3-1-1.pdf>

Text file based optimization.

3 files required:

1. Configuration File (`.cfg` extension): Usually set up once per type of program, i.e. EnergyPlus, xlim, Transys

```
// vim: ft=genoptcfg

SimulationError { ErrorMessage = "Error"; }
IO { NumberFormat = Double; }
SimulationStart
{
    Command = "./runxlim.sh";
    WriteInputFileExtension = true;
}
```

2. Initialization file (`.ini`):
  - Where the runtime optimization files are located
  - What files should be saved after finished
  - Additional strings to be passed to the command line invocation
  - Where the cost function is in the output file
  - Whether that cost function needs to be post-processed
  - What simulation program is being used.


```
Simulation {
    Files {
        Template {
            File1 = "./gen_hx_fit.xlim";
        }
        Input {
            File1 = "./in.xlim";
        }
        Log {
            File1 = "./log.txt";
        }
        Output {
            File1 = "./out.txt";
        }
        Configuration {
            File1 = "./xlim.cfg";
        }
    }
    ObjectiveFunctionLocation {
        Name1  = "objective";
        Delimiter1 = "=";
    }
}
Optimization {
    Files {
        Command {
            File1 = "./command.txt";
        }
    }
}
```


3. Command file (`command.txt`)
  - optimization variables
  - stopping criteria
  - optimization algorithm


## Notes

If `WriteStepNumber` is true, the `%stepNumber%` placeholder must exist in the template file.


## Algorithms

```
// 1-D continuous
Algorithm { Main = GoldenSection | Fibonacci; }

GoldenSection needs either:
AbsDiffFunction
IntervalReduction
```

## Running

```sh
# With GUI
java -jar genopt.jar file.ini
# I have genopt script that looks for installed version
genopt file.ini
# Without GUI
java -classpath genopt.jar genopt.GenOpt file.ini
```

## Continuous Parameters

```
// Settings for a continuous parameter
Parameter {
    Name = String ;
    Ini = Double ;
    Step = Double ;
    [ Min = Double | SMALL; ]
    [ Max = Double | BIG ; ]
    [ Type = CONTINUOUS; ]
}
```

## Paths

`Command` in `.cfg` file is run from within the temp working directory, a directory below the `.ini` file.

However, a leading '.' in the `Command` path will be replaced with the directory of the `.ini` file.

Example:

```
SimulationStart
{
    Command = "./run.sh %Simulation.Files.Input.File1%";
    WriteInputFileExtension = true;
}
```

This is then run as:

```sh
# PWD: /abs/dir/to/ini/file/tmp_subdir
/abs/dir/to/ini/file/run.sh input_file.ext
```
