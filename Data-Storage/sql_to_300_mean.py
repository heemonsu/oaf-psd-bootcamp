import sqlite3
import pandas as pd

# SQLite database file
sqlite_file = 'hourly_temperatures.db'

# Connect to SQLite database
conn = sqlite3.connect(sqlite_file)

# Query the database for entries at 3:00 pm
query_pm = "SELECT * FROM temperature_data WHERE strftime('%H:%M', date) = '15:00';"
result_pm = pd.read_sql_query(query_pm, conn)

# Query the database for entries at 3:00 am
query_am = "SELECT * FROM temperature_data WHERE strftime('%H:%M', date) = '03:00';"
result_am = pd.read_sql_query(query_am, conn)

# Close the database connection
conn.close()

# Calculate and print the average temperature for 3:00 pm
print(result_pm)
avg_temp_pm = result_pm['temperature_2m'].mean()
print(f"Average temperature at 3:00 pm: {avg_temp_pm:.2f} Celsius")


# Calculate and print the average temperature for 3:00 am
print(result_am)
avg_temp_am = result_am['temperature_2m'].mean()
print(f"Average temperature at 3:00 am: {avg_temp_am:.2f} Celsius")

