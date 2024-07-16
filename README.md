# django-weather-app
<h1>Django Weather App</h1>
<br>
A simple web application built with Django that allows users to get current weather information for any city using the OpenWeatherMap API.
<br>
Features:
<br>
User-friendly interface for entering city names.
<br>
Displays current temperature, humidity, country code, and coordinates.
<br>
Uses OpenWeatherMap API to fetch real-time weather data.
<br>
Securely manages API key using environment variables.
<br>
Prerequisites
<br>
Python 3.x
Django 3.x or later
OpenWeatherMap API Key
Installation
Clone the Repository

<br>

Usage
Enter the name of the city you want to get the weather information for in the input field.
Click on the "Get Weather" button.
The app will display the current weather details, including temperature, humidity, country code, and coordinates.
<br>

Code Overview
<br>
views.py
The views.py file contains the main logic for fetching and displaying the weather data.
<br>
weather.html
The weather.html template file provides the frontend for the app.
<br>

Acknowledgements
Django
OpenWeatherMap
python-decouple
