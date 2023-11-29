from abc import ABC, abstractmethod
import requests
import random

# for testing, use a constant seed
random.seed(0)

SERVICE_REFERENCE = "api"

MIN_TEMP = 0.0
MAX_TEMP = 40.0

class AbstractWeatherService(ABC):
        @abstractmethod
        def get_weather(self, longitude: float, latitude: float):
            pass

class ApiService(AbstractWeatherService):
        url = 'https://api.open-meteo.com/v1/forecast'

        def get_weather(self, longitude: float, latitude: float):
            payload = {
                'latitude': latitude,
                'longitude': longitude,
                'hourly': 'temperature_2m'
            }
        
            try:
                response = requests.get(ApiService.url, params=payload)
            except Exception:
                print("failed to receive data from api")
                return []
 
            json_data = response.json()

            hourly_data = json_data.get("hourly", {})
            temperature = hourly_data.get("temperature_2m", [])
            return temperature

class MockService(AbstractWeatherService):
        def get_weather(self, longitude: float, latitude: float):
            return [random.uniform(MIN_TEMP, MAX_TEMP) for _ in range(20)]

class ServiceFactory():
        def buildService(name:str) -> AbstractWeatherService:
            if name == "mock":
                return MockService()
            elif name == "api":
                return ApiService()
            else:
                raise RuntimeError("Unspecified name:" + name)

class VisualizationHandler():
        def visualize_data(self, data: list):
            print(data)

class DataSourceHandler():
        def __init__(self, service: AbstractWeatherService, visualization_handler: VisualizationHandler) -> None:
            self.service = service
            self.visualization_handler = visualization_handler

    # could use mathplotlib to visualize data
        # def do_other_thing(self, recent_weather: list):
            # print(recent_weather)
            # forward to data storage handler
        
        def resolve_weather(self, longitude: float, latitude: float):
            resolved_recent_weather = self.service.get_weather(longitude, latitude)
            # self.do_other_thing(resolved_recent_weather)
            self.visualization_handler.visualize_data(resolved_recent_weather)

if __name__ == "__main__":
        # use a factory to build the service
        useable_service = ServiceFactory.buildService(SERVICE_REFERENCE)

        # data handler gets service injected like a dependency
        data_handler = DataSourceHandler(useable_service, VisualizationHandler())

        # use some data and call the program
        latitude = 37.7723281
        longitude = -122.4530167
        data_handler.resolve_weather(longitude, latitude)