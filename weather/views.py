from django.shortcuts import render
from weather.service.weather_service import getDataForCity

def index(request:str):
  weatherData = {}
  if 'city' in request.GET:
    city = request.GET['city']
    weatherData = getDataForCity(city)
  return render(request, 'weather/index.html', {'data': weatherData})
