import requests
import urllib.parse
from django.conf import settings

def getDataForCity(city:str):
  weatherData = {}
  endpoint = f'{settings.VISUAL_CROSSING_WEATHER_URL}/{urllib.parse.quote(city)}/next7days?unitGroup=metric&key={settings.VISUAL_CROSSING_WEATHER_API_KEY}'  
  try:
    response = requests.get(endpoint)
    weatherData = response.json()
  except requests.exceptions.RequestException:
    weatherData = 'Sorry, we cannot provide you a weather information for {location}'.format(location=city)
  return weatherData