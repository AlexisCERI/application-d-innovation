# sncf_arrivals.py

import requests
from datetime import datetime

def get_train_info_arrivals(city):
    api_address = 'https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area%3ASNCF%3A87318964/arrivals'
    headers = {
        'Authorization': '4fad210a-e5fd-4440-bb18-fbeda2b6dd81',
    }
    response = requests.get(api_address, headers=headers)

    train_info_list = []

    if response.status_code == 200:
        json_data = response.json()
        arrivals = json_data.get('arrivals', [])

        for arrival in arrivals:
            route = arrival.get('route', {})
            stop_date_time = arrival.get('stop_date_time', {})
            display_info = arrival.get('display_informations', {})

            # Utiliser directement le champ stop_point pour obtenir le point d'arrivée
            arrival_location = route.get('direction', {}).get('name', '')

            # Convertir la date dans le format demandé
            raw_arrival_time = stop_date_time.get('arrival_date_time', '')
            formatted_arrival_time = datetime.strptime(raw_arrival_time, '%Y%m%dT%H%M%S').strftime('%d %B à %Hh%M:%S')

            train_info = {
                "train_number": display_info.get('headsign', ''),
                "departure_from": route.get('direction', {}).get('name', ''),
                "arrival_at": arrival_location,
                "arrival_time": formatted_arrival_time,
            }
            train_info_list.append(train_info)

    return train_info_list
