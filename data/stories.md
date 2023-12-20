## ask_weather
* greet
  - utter_greet
* weather
  - utter_city
* vent
  - action_vent

## specify_city
* greet
  - utter_greet
* city
  - action_weather_api

## ask_vent
* greet
  - utter_greet
* vent
  - utter_vent

## specify_vent
* greet
  - utter_greet
* vent
  - action_vent

## train_departures
* greet
  - utter_greet
* ask_train_departures
  - action_train_info

## train_arrivals
* greet
  - utter_greet
* ask_train_arrivals
  - action_train_info_arrivals

