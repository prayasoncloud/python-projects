import requests

key = "79149cb0a31f63994c7b3af97c4692be"

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

print(data)