"""
Author: Steve Eckardt <seckardt@pacbell.net>
Original code by Patrick Zippenfenig Source: https://github.com/open-meteo/sdk
Project: oa professional software development bootcamp
Program Name: model_builder.py
Revised: January 3rd 2024
License: MIT
"""

import openmeteo_requests
import requests_cache
import pandas as pd
import matplotlib.pyplot as plt
from retry_requests import retry
import sqlite3

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 41.85003,
	"longitude": -87.65005,  #Chicago, Illinois
	"start_date": "1940-01-01",
#    "start_date": "2023-12-30",
	"end_date": "2023-12-31",
	"hourly": "temperature_2m",
	"timezone": "America/Los_Angeles"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s"),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)

first_column_type = hourly_dataframe['date'].dtype
print(f"The data type of the first column is: {first_column_type}")

second_column_type = hourly_dataframe['temperature_2m'].dtype
print(f"The data type of the second column is: {second_column_type}")

# Save the DataFrame to a CSV file
hourly_dataframe.to_csv('Chicago_hourly_temp.csv', index=False)

# create SQLite database file
sqlite_file = 'Chicago_temp.db'
conn = sqlite3.connect(sqlite_file)
hourly_dataframe.to_sql('hourly_data', conn, index=False, if_exists='replace')
conn.close()
