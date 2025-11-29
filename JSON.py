import json

def fetch_weather_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    location = data['location']['name']
    country = data['location']['country']
    temperature = data['current']['temperature']
    humidity = data['current']['humidity']
    wind_speed = data['current']['wind_speed']
    description = data['current']['weather_descriptions'][0]

    print("Weather Report for", location, country)
    print("Condition:", description)
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Wind Speed:", wind_speed)

fetch_weather_from_json("weather.json")
