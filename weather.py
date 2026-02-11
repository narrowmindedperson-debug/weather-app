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

import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass


load_dotenv()
api_key = os.getenv('API_key')

@dataclass
class weatherdata:
    main: str 
    description: str
    icon: str
    temperature: int

def get_lan_lon(city_name,state_code,country_code,API_key):
    resp = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}") .json()
    # 👉 resp is a Python variable that stores the JSON response returned by the OpenWeatherMap API.
    data = resp[0]
    # 👉 data becomes the first dictionary inside the list resp
    lat,lon = data.get('lat'), data.get('lon')
    return lat,lon
 

def get_current_weather(lat,lon,API_key):

    resp=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = weatherdata(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=int(resp.get('main').get('temp'))
    )
    return data 

def main(city_name,state_name,country_name):
    lat,lon=get_lan_lon(city_name,state_name,country_name,api_key)
    weather_data=(get_current_weather(lat,lon,api_key))
    return weather_data


if __name__ == "__main__":
    lat,lon=get_lan_lon('toronto','ON','canada',api_key)
    print (get_current_weather(lat,lon,api_key))