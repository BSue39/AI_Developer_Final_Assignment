import requests

# Define the coordinates and the data we want
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 40.71,
    "longitude": -74.01,
    "current": "temperature_2m",
}

# Make the request
response = requests.get(url, params=params)
data = response.json()

# Print the current temperature
current_temp = data['current']['temperature_2m']
unit = data['current_units']['temperature_2m']

print(f"The current temperature in NYC is {current_temp}{unit}")