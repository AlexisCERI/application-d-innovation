import requests

def Vent(city):
    api_key = '78c66689b8926082321cdfff9d4dc9e2'
    api_address = f'http://api.openweathermap.org/data/2.5/weather?lang=fr&appid={api_key}&q='
    url = api_address + city
    json_data = requests.get(url).json()

    vitesse_vent = json_data['wind']['speed']
    temperature_info = json_data['main']

    temp_min = int(temperature_info['temp_min'] - 273)
    temp_max = int(temperature_info['temp_max'] - 273)

    humidity = json_data.get('main', {}).get('humidity', None)

    return {
        'vitesse_vent': vitesse_vent,
        'temp_min': temp_min,
        'temp_max': temp_max,
        'humidity': humidity
    }
