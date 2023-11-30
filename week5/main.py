#I don't really have progress on main.py yet I don't know how to tie this structure of the program all together yet it's getting to be a lot of pieces to put together for a beginner like me.
#I will try though.


import argparse

from database import WeatherDatabase
from service import WeatherService

#Global constants
DB_FILE = "data/weather_database.db"
API_KEY = "todogetanAPIkey"

def login():
    return "login"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="City to get the weather data for")
    parser.add_argument("--reset", action="store_true", help="Reset the database")
    args = parser.parse_args()


    #Create a database object
    db = WeatherDatabase(DB_FILE)
    service = WeatherService(API_KEY)

    #Reset the database if --reset is provided
    if args.reset:
        db.reset_database()

    # and print weather data for the provided city
    city_weather_data = db.get_weather_data(service, args.city)
    print(f"Weather data for {args.city}:", city_weather_data)

    if __name__ == "__main__":
        main()

