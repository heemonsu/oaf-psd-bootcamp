import pandas as pd
import sqlite3

# Load DataFrame from pickle file
pickle_file = 'hourly_temperatures.pkl'
df_hour_temp = pd.read_pickle(pickle_file)

# Print DataFrame to the screen
print("Data from the pickle file:")
print(df_hour_temp)

# SQLite database file
sqlite_file = 'hourly_temperatures.db'

# Connect to SQLite database
conn = sqlite3.connect(sqlite_file)

# Save DataFrame to SQLite database
df_hour_temp.to_sql('temperature_data', conn, index=False, if_exists='replace')

# Query the database and print the results
query = "SELECT * FROM temperature_data;"
result_df_hour_temp = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()
