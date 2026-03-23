'''
User enters a postcode(Canada)
check online which city it is
and what's the weather
'''
import requests


def get_coordinates(city):
    url = 'https://geocoding-api.open-meteo.com/v1/search'
    params = {
        'name': city,
        'count': 1,
        'language': 'en',
        'format': 'json',
        'countryCode': 'CA',
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data:
        return None

    print(data['results'])
    result = data["results"][0]
    return result["latitude"], result["longitude"]

def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': True,
        'temperature_unit': 'celsius'
    }

    response = requests.get(url, params=params)
    data = response.json()

    current = data["current_weather"]
    print(current)
    return {
        'temperature': current['temperature']
    }

lat, lon = get_coordinates('Montreal')
print(get_weather(lat, lon))