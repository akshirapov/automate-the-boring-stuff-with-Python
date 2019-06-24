#! python3
# quickWeather.py - Prints the weather for a location from the command line.


import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 1:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

location = 'Irkutsk'


# Download the JSON data from OpenWeatherMap.org's API.
api_id = '3f0a41ec4f54c4d5e0d8eea9ed868c5d'
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, api_id)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % location)



