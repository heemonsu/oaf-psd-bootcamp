import pandas as pd

# Read CSV file into a DataFrame
csv_file = 'hourly_temperatures.csv'
df_hour_temp = pd.read_csv(csv_file)

# Print DataFrame to the screen
print("Data from the CVS file:")
print(df_hour_temp)

# Save DataFrame to pickle file
pickle_file = 'hourly_temperatures.pkl'
df_hour_temp.to_pickle(pickle_file)

