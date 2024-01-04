"""
Author: Steve Eckardt <seckardt@pacbell.net>
Project: oa professional software development bootcamp
Program Name: view_data.py
Revised: January 3rd 2024
License: MIT
"""
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

sqlite_file = 'Chicago_temp.db'
conn = sqlite3.connect(sqlite_file)
query = "SELECT * FROM annual_data"
annual_df = pd.read_sql_query(query, conn)
query = "SELECT * FROM decadal_data"
decadal_df = pd.read_sql_query(query, conn)
conn.close()



annual_df = annual_df.drop('Std', axis=1)
x = annual_df['Year']
for column in annual_df.columns[1:]:
    plt.plot(x, annual_df[column], linestyle='-', label=column)
plt.xlabel('Year')
plt.ylabel('Temperatures in Celsius')
plt.title('Chicago\'s Annual Temperatures')
plt.legend(loc='lower left', bbox_to_anchor=(1, 0))
plt.show()


x = decadal_df['Decade']
decadal_df = decadal_df.drop('Std', axis=1)
for column in decadal_df.columns[1:]:
    plt.plot(x, decadal_df[column], linestyle='-', label=column)
plt.xlabel('Decade')
plt.ylabel('Temperatures in Celsius')
plt.title('Chicago\'s Decadal Temperatures')
plt.legend(loc='lower left', bbox_to_anchor=(1, 0))
plt.show()