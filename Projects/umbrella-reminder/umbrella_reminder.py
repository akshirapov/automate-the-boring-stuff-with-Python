# python3
# umbrella_reminder.py - Checks weather it's raining that day. If so,
# texts a reminder to pack an umbrella before leaving the house.

import requests
import json

from twilio.rest import Client

# Preset values
ACCOUNT_SID = "ACf0b15a2348daa30c348062c010f4ba54"
AUTH_TOKEN = "0dcd711b1dde2966890de12ef9a1b0bc"


def text_myself(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
        to="+79148773089",
        from_="+12566458080",
        body=message,
    )


# Download the JSON data from OpenWeatherMap.org's API.
location = 'Irkutsk'
app_id = '3f0a41ec4f54c4d5e0d8eea9ed868c5d'
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, app_id)

response = requests.get(url)
try:
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print('%s can’t be loaded!' % url)


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)


# Print weather descriptions.
weather_condition = weatherData['weather'][0]['main']
if weather_condition == 'Rain':
    text_myself('Today is raining. Pack an umbrella.')
