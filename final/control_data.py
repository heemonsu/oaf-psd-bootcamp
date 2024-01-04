"""
Author: Steve Eckardt <seckardt@pacbell.net>
Project: oa professional software development bootcamp
Program Name: control_data.py
Revised: January 3rd 2024
License: MIT
"""

import sqlite3
import pandas as pd
import numpy as np

sqlite_file = 'Chicago_temp.db'
conn = sqlite3.connect(sqlite_file)

column_names = ['Year', 'Mean', 'Max', 'Min', 'Std']
annual_df = pd.DataFrame(columns=column_names)
annual_df.set_index('Year', inplace=True)

for year_index in range(1940, 2024):
    query = f"SELECT * FROM hourly_data WHERE strftime('%Y', date) = '{year_index}';"
    selected_year_df = pd.read_sql_query(query, conn)
    temp_array = selected_year_df['temperature_2m'].values

    mean_value = round(np.mean(temp_array),3)
    max_value = round(np.max(temp_array),3)
    min_value = round(np.min(temp_array),3)
    std_value = round(np.std(temp_array),3)

    new_row = {
        'Year': year_index,
        'Mean': mean_value,
        'Max': max_value,
        'Min': min_value,
        'Std': std_value
    }

    annual_df.loc[year_index] = new_row

annual_df['Mean+Std'] = annual_df['Mean'] + annual_df['Std']
annual_df['Mean-Std'] = annual_df['Mean'] - annual_df['Std']
new_order = ['Max', 'Mean+Std', 'Mean', 'Mean-Std', 'Min', 'Std']
annual_df = annual_df[new_order]

annual_df.to_sql('annual_data', conn, if_exists='replace')




column_names[0] = 'Decade'
decadal_df = pd.DataFrame(columns=column_names)
decadal_df.set_index('Decade', inplace=True)

for start_year in range(1940, 2011, 10):
    end_year = start_year + 9
    query = f"SELECT * FROM hourly_data WHERE strftime('%Y', date) >= '{start_year}' AND strftime('%Y', date) <= '{end_year}';"
    selected_decade_df = pd.read_sql_query(query, conn)
    temp_array = selected_decade_df['temperature_2m'].values

    mean_value = round(np.mean(temp_array),3)
    max_value = round(np.max(temp_array),3)
    min_value = round(np.min(temp_array),3)
    std_value = round(np.std(temp_array),3)

    new_row = {
        'Decade': start_year,
        'Mean': mean_value,
        'Max': max_value,
        'Min': min_value,
        'Std': std_value
    }

    decadal_df .loc[start_year] = new_row

decadal_df['Mean+Std'] = decadal_df['Mean'] + decadal_df['Std']
decadal_df['Mean-Std'] = decadal_df['Mean'] - decadal_df['Std']
decadal_df = decadal_df[new_order]

decadal_df.to_sql('decadal_data', conn, if_exists='replace')

conn.close()

print()
print(annual_df)
annual_df.to_csv('Chicago_annual_temp.csv', index=False)

print()
print(decadal_df)
decadal_df.to_csv('Chicago_decadal_temp.csv', index=False)

