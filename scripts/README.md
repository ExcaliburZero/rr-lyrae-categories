# Scripts
These are the scripts that we used for analyzing the OGLE III and IV RR Lyrae Data.

## function.py
Creates a graph of a probability function using provided mean and standard deviation values.

```
$ python function.py "RRab Period Probability (SMC OGLE III)" "Period (days)" "Probability" ../graphs/ogle3_smc_RRab_probability.png < ~/Documents/ogle/ogle3/smc/RRab-stats.dat
```

![function.py example](../graphs/ogle3_smc_RRab_probability.png)

### Usage
Command structure:

```
python function.py TITLE X_AXIS Y_AXIS OUTPUT_FILE < DATA_FILE
```

Data file structure:

```
MEAN
STANDARD_DEVIATION
```

Example data file:

```
0.595879
0.05925889
```
