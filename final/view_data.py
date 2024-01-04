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

plt.xlabel('Year')
plt.ylabel('Temperatures in Celsius')
plt.title('Chicago\'s Annual Temperatures')
plt.plot(x, annual_df['Max'], color='#FF0000', label='Max') # Hot Red
plt.plot(x, annual_df['Mean+Std'], color='#FFA500', label='Mean+Std') # Warm Orange
plt.plot(x, annual_df['Mean'], color='#FFFF00', label='Mean') # Neutral Yellow
plt.plot(x, annual_df['Mean-Std'], color='#0000FF', label='Mean-Std') # Cool Blue
plt.plot(x, annual_df['Min'], color='#800080', label='Min') # Cold Purple
plt.legend( loc='lower left', bbox_to_anchor=(1, 0))
plt.subplots_adjust(right=0.8)
plt.show()


x = decadal_df['Decade']
decadal_df = decadal_df.drop('Std', axis=1)
plt.plot(x, decadal_df['Max'], color='#FF0000', label='Max') # Hot Red
plt.plot(x, decadal_df['Mean+Std'], color='#FFA500', label='Mean+Std') # Warm Orange
plt.plot(x, decadal_df['Mean'], color='#FFFF00', label='Mean') # Neutral Yellow
plt.plot(x, decadal_df['Mean-Std'], color='#0000FF', label='Mean-Std') # Cool Blue
plt.plot(x, decadal_df['Min'], color='#800080', label='Min') # Cold Purple
plt.xlabel('Decade')
plt.ylabel('Temperatures in Celsius')
plt.title('Chicago\'s Decadal Temperatures')
plt.legend(loc='lower left', bbox_to_anchor=(1, 0))
plt.subplots_adjust(right=0.8)
plt.show()