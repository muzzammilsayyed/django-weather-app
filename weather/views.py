from django.shortcuts import render
import requests
from decouple import config

def weather(request):
    data = {}
    if request.method == 'POST':
        city = request.POST['city']
        api_key = config('API_KEY')
        source = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}'
        list_of_data = requests.get(source).json()
        if list_of_data.get('cod') == 200:
            data = {
                "country_code": str(list_of_data['sys']['country']),
                'coordinate': str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
                'temp': round((list_of_data['main']['temp'] - 32) * 5.0/9.0, 2),
                'humidity': str(list_of_data['main']['humidity']),
                'city': city
            }
        else:
            data['error'] = 'City not found or API request failed.'
    return render(request, "weather.html", data)
