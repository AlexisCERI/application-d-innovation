from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from weather import Weather
from sncf_departures import get_train_info
from sncf_arrivals import get_train_info_arrivals
from vent import Vent

class ActionWeatherApi(Action):
    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #city = tracker.latest_message['text']
        city = tracker.get_slot('city')
        weather_data = Weather(city)
        weather_description_fr = weather_data['weather_description_fr']
        temp_min = int(weather_data['temp_min'])
        temp_max = int(weather_data['temp_max'])
        
        dispatcher.utter_message(
            text=f"La météo est {weather_description_fr}. La température minimale est {temp_min} degrés Celsius et la maximale est {temp_max} degrés Celsius."
        )
        return []

class ActionVentApi(Action):
    def name(self) -> Text:
        return "action_vent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot('city')
        #city = tracker.latest_message['text']
        vent_data = Vent(city)
        vitesse_vent = vent_data['vitesse_vent']
        humidite = vent_data['humidity']

        dispatcher.utter_message(
            text=f"La vitesse du vent est de {vitesse_vent} mètres par seconde. L'humidité est de {humidite}%"       
	    )
        return []


class ActionTrainInfo(Action):
    def name(self) -> Text:
        return "action_train_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.latest_message['text']
        train_info_list = get_train_info(city)
        if train_info_list:
            for train_info in train_info_list:
                dispatcher.utter_message(
                    f"Le train numéro {train_info['train_number']} au départ de {train_info['departure_from']} à destination de {train_info['destination']} partira le {train_info['departure_time']}"
                )
        else:
            dispatcher.utter_message("Désolé, je n'ai pas pu récupérer les informations sur les trains pour le moment.")
        return []

class ActionTrainInfoArrivals(Action):
    def name(self) -> Text:
        return "action_train_info_arrivals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.latest_message['text']
        train_info_list = get_train_info_arrivals(city)
        if train_info_list:
            for train_info in train_info_list:
                dispatcher.utter_message(
                    f"Le train numéro {train_info['train_number']} au départ de {train_info['departure_from']} arrivera le {train_info['arrival_time']}"
                )
        else:
            dispatcher.utter_message("Pas arrivées !")
        return []
