import requests
from datetime import datetime

def get_train_info(city):
    api_address = 'https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area%3ASNCF%3A87318964/departures'
    headers = {
        'Authorization': '4fad210a-e5fd-4440-bb18-fbeda2b6dd81',
    }
    response = requests.get(api_address, headers=headers)

    train_info_list = []

    if response.status_code == 200:
        json_data = response.json()
        departures = json_data.get('departures', [])

        for departure in departures:
            route = departure.get('route', {})
            stop_date_time = departure.get('stop_date_time', {})
            display_info = departure.get('display_informations', {})

            # Utiliser directement le champ stop_point pour obtenir le point de départ
            departure_location = display_info.get('direction', '')

            # Convertir la date dans le format demandé
            raw_departure_time = stop_date_time.get('departure_date_time', '')
            formatted_departure_time = datetime.strptime(raw_departure_time, '%Y%m%dT%H%M%S').strftime('%d %B à %Hh%M:%S')

            train_info = {
                "train_number": display_info.get('headsign', ''),
                "departure_from": departure_location,
                "destination": route.get('direction', '').get('name', ''),  # Modifier cette ligne si nécessaire
                "departure_time": formatted_departure_time,
            }
            train_info_list.append(train_info)

    return train_info_list
