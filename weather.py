# perpose of this code is 👉 This code is written to fetch live weather information of 
# a city from the OpenWeatherMap API and return it in a clean, usable Python object.
# 🧩 Why do we even need this code?
# Problem:

# Computers cannot understand city names directly for weather.

# The weather API needs:

# latitude

# longitude

# But users give:

# city

# state

# country

# So this code acts as a translator.

import os
import requests
from dataclasses import dataclass

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int

def get_lat_lon(city_name, state_code, country_code, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}"
    resp = requests.get(url).json()

    if not resp:
        return None, None

    data = resp[0]
    return data.get("lat"), data.get("lon")

def get_current_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    resp = requests.get(url).json()

    return WeatherData(
        main=resp.get("weather", [{}])[0].get("main", ""),
        description=resp.get("weather", [{}])[0].get("description", ""),
        icon=resp.get("weather", [{}])[0].get("icon", ""),
        temperature=int(resp.get("main", {}).get("temp", 0))
    )

def main(city_name, state_name, country_name):
    api_key = os.getenv("API_KEY")   # ✅ must match Render exactly

    if not api_key:
        raise RuntimeError("API_KEY environment variable not set")

    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)

    if lat is None or lon is None:
        return None

    return get_current_weather(lat, lon, api_key)
