import requests
import os

key = os.ENV_KEY

MY_LONG = "77.4126"
MY_LAT = "23.2599"

parameters = {

    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": key,
    "cnt": 3

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

data_id = data["list"]

will_rain = True

for hours in data_id:
    code = hours["weather"][0]["id"]
    if code < 700:
        will_rain = False

if will_rain == False:
    print("Bring an Umbrella")




