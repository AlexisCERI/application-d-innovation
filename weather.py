# Weather.py

import requests

def Weather(city):
    api_address = 'http://api.openweathermap.org/data/2.5/weather?lang=fr&appid=78c66689b8926082321cdfff9d4dc9e2&q='
    url = api_address + city
    json_data = requests.get(url).json()

    weather_description_fr = json_data['weather'][0]['description']
    temperature_info = json_data['main']
    
    temp_min = int(temperature_info['temp_min'] - 273)
    temp_max = int(temperature_info['temp_max'] - 273)

    return {
        'weather_description_fr': weather_description_fr,
        'temp_min': temp_min,
        'temp_max': temp_max
    }
