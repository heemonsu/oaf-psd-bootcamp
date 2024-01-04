"""
Author: Steve Eckardt <seckardt@pacbell.net>
Project: oa professional software development bootcamp
Program Name: main.py
Revised: January 3rd 2024
License: MIT

The goal of this project is to observe temperature changes in Chicago, Illinois, over the last 80 years.

Steps:
Model builder:
1. Download the hourly measurements from the Open-Metro API site.
2. Create a Chicago_temp.db database and save the temperature data into a table.
3. Save the temperature data into a CSV file and print temperature data to the screen.
Control Data:
4. Calculate the data set's annual min, max, mean, and standard deviation.
5. Calculate the decade min max medium and standard deviation of the data set.
6. Save the calculations to a new table in the database, a CSV file, and print to the screen.
View Data:
6. Plot a line graph of the annual data and the decade data.

The two graphs and a screen capture of the program run are attached.

Observations and Conclusions:
Decade     Max  Mean+Std    Mean  Mean-Std     Min     Std
  1940  35.541    20.813   9.215    -2.383 -27.009  11.598
  1950  36.126    21.429   9.958    -1.513 -26.374  11.471
  1960  36.176    21.195   9.404    -2.387 -28.774  11.791
  1970  35.376    21.292   9.466    -2.360 -26.474  11.826
  1980  36.976    21.546   9.834    -1.878 -31.824  11.712
  1990  37.426    21.302  10.291    -0.720 -32.524  11.011
  2000  36.726    21.645  10.375    -0.895 -28.024  11.270
  2010  36.876    21.541  10.246    -1.049 -32.437  11.295
Over the past 80 years, the data shows that average and maximum temperatures have increased by 1° Celsius or about 2° Fahrenheit.
Interestingly, the minimum temperature decreased by 5° C or about 10° f.
"""
import subprocess
try:
    subprocess.run(["python", 'model_builder.py'], check=True)
    subprocess.run(["python", 'control_data.py'], check=True)
    subprocess.run(["python", 'view_data.py'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running the script: {e}")