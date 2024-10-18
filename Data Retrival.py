import requests
import time

API_KEY = 'YOUR_API_KEY'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None

def get_weather_data():
    weather_data = {}
    for city in CITIES:
        data = fetch_weather_data(city)
        if data:
            weather_data[city] = data
    return weather_data

if __name__ == "__main__":
    while True:
        print(get_weather_data())
        time.sleep(300)  # Wait for 5 minutes