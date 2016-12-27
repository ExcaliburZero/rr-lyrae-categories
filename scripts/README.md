# Scripts
These are the scripts that we used for analyzing the OGLE III and IV RR Lyrae Data.

## mean-sd.R
Calculates the mean and standard deviation of the given data.

```
$ ./mean-sd.R ~/Documents/ogle/ogle3/smc/RRab-periods.dat
0.595879 
0.05925889
```

### Usage
Command structure:

```
./mean-sd.R DATA_FILE
```

Data file structure:

```
PERIOD_1
PERIOD_2
...
```

Example data file:

```
0.5588141
0.5947913
0.6506693
0.5652567
0.5471791
0.6328832
0.6947615
0.5530407
0.5957614
0.6256321
```

Output structure:

```
MEAN
STANDARD_DEVIATION
```

## scatter.py
Creates a scatter graph of all of the given period values.

```
$ python scatter.py "RRab Periods (SMC OGLE III)" "Number" "Period (days)" ../graphs/ogle3_smc_RRab_scatter.png < ~/Documents/ogle/ogle3/smc/RRab-periods.dat
```

![scatter.py example](../graphs/ogle3_smc_RRab_scatter.png)

### Usage
Command structure:

```
python scatter.py TITLE X_AXIS Y_AXIS OUTPUT_FILE < DATA_FILE
```

Data file structure:

```
PERIOD_1
PERIOD_2
...
```

Example data file:

```
0.5588141
0.5947913
0.6506693
0.5652567
0.5471791
0.6328832
0.6947615
0.5530407
0.5957614
0.6256321
```

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
