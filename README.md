# Trapping Rain Water

Author: Michael Trossbach

Contact: mptrossbach@gmail.com

## Problem Description

Given *n* non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

## Solutions
1. Row by row (i.e. axis 0). This solution can be parallelized.

2. Column by column (i.e. axis 1). This solution cannot be parallelized (as far as I can tell).

## Usage
Two options:
- Jupyter Notebook (see `trapping_rain_water.ipynb`)
- Command line


> Command-line arguments
> - `-e` **elevation map**: space-separated list of integer values
> - `-a` **axis**: axis to use when applying the function
> - `-p` **plot**: whether to visualize the trapped water

## Examples

Get the total count of the water units using axis 0 (**no visualization**).

```
$ python trapped_rain_water.py -e 1 0 2 3 1 2 -a 0
Number of Water Units: 2
```
Generate the image of the elevation map and the water units (which will also tell you the total count of water units).

```
$ python trapped_rain_water.py -e 1 0 2 3 1 2 -p
```

**Output**
![alt text](https://raw.githubusercontent.com/michotross257/trapped-rain-water/master/images/readme_trapped_water.jpg)
