class WeatherDataRepository:
    def __init__(self, database):
        self.database = database

    def get_weather_data(self, city):
        return self.database.get_weather_data(city)

    def insert_weather_data(self, city, temperature, conditions):
        self.database.insert_data(city, temperature, conditions)

  #this file could be like a interface to talk between the database and other classes
