"""Weather forecast app part 2:

In part 1, your app was able to get the current weather and temperature of a city.
Now we will extend this app to get the weather forecast for the next 7 days.


1. Expand your API call to get the weather forecast for the next 7 days.
You will have to add the following two parameters:
&daily=temperature_2m_max,temperature_2m_min
&timezone=Europe%2FBerlin

Print this data.
"""
import requests


def get_coordinates(city_name):
    """Returns the latitude, longitude and elevation of a city."""
    # Create the API call URL
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    # Send the request to the website and get the response
    response = requests.get(url)
    # Convert the response from JSON to a Python dictionary
    data = response.json()
    # Check if the city was found
    if "results" not in data:
        raise Exception("City not found.")
    # Get the latitude, longitude and elevation from the response
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    elevation = data["results"][0]["elevation"]
    return latitude, longitude, elevation


def get_weather_forecast(city_name):
    days = []
    temp_max = []
    temp_min = []
    
    # Error handling when the city is not found
    try:
        latitude, longitude, elevation = get_coordinates(city_name)
    except Exception as e:
        print(e)
        return days, temp_max, temp_min
    # Create the API call URL
    url = "https://api.open-meteo.com/v1/forecast?"
    url += "current_weather=true"  # Add current_weather to request URL
    url += f"&latitude={latitude:.2f}"  # Add latitude to request URL
    url += f"&longitude={longitude:.2f}"  # Add longitude to request URL
    url += f"&elevation={elevation:.2f}"  # Add elevation to request URL
    # TODO: Get the weather forecast for the next 7 days
    # 1. Add the daily and timezone parameters to the request URL
    # 2. Send the request to the API and get the response
    # 3. Convert the response from JSON to a Python dictionary
    # 4. Get the days, maximum and minimum temperature from the response
    # MY CODE (assignment 1)
    # 1. Add the daily and timezone parameters to the request URL
    url += f"&daily=temperature_2m_max,temperature_2m_min"
    url += f"&timezone=Europe%2FBerlin"

    # 2. Send the request to the API and get the response
    response = requests.get(url)

    # 3. Convert the response from JSON to a Python dictionary
    data = response.json()

    # 4. Get the days, maximum and minimum temperature from the response
    days = data["daily"]["time"]
    temp_max = data["daily"]["temperature_2m_max"]
    temp_min = data["daily"]["temperature_2m_min"]
    # MY CODE (assignment 1) END
    return days, temp_max, temp_min


if __name__ == "__main__":
    city_name = input("Please enter the name of a city: ")

    while city_name != "exit":
        days, temp_max, temp_min = get_weather_forecast(city_name)
        # TODO: Print the weather data for the next 7 days        
        # # MY CODE (assignment 2)
        # days is empty when the city was not found, so only print if we have data
        if len(days) > 0:
            print(f"Weather forecast for the next 7 days in {city_name}:")
            for i in range(len(days)):
                print(f"{days[i]}: min {temp_min[i]}°C, max {temp_max[i]}°C")
        # MY CODE (assignment 2) END

        city_name = input("Please enter the name of a city: ")