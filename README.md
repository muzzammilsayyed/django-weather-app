# django-weather-app
Django Weather App
A simple web application built with Django that allows users to get current weather information for any city using the OpenWeatherMap API.

Features
User-friendly interface for entering city names.
Displays current temperature, humidity, country code, and coordinates.
Uses OpenWeatherMap API to fetch real-time weather data.
Securely manages API key using environment variables.
Prerequisites
Python 3.x
Django 3.x or later
OpenWeatherMap API Key
Installation
Clone the Repository



Usage
Enter the name of the city you want to get the weather information for in the input field.
Click on the "Get Weather" button.
The app will display the current weather details, including temperature, humidity, country code, and coordinates.

Code Overview
views.py
The views.py file contains the main logic for fetching and displaying the weather data.

weather.html
The weather.html template file provides the frontend for the app.

Acknowledgements
Django
OpenWeatherMap
python-decouple
