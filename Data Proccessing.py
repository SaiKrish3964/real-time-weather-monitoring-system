import pandas as pd
from datetime import datetime

weather_records = []

def process_weather_data(data):
    global weather_records
    for city, details in data.items():
        temp = details['main']['temp']
        feels_like = details['main']['feels_like']
        condition = details['weather'][0]['main']
        timestamp = datetime.fromtimestamp(details['dt']).date()

        weather_records.append({
            'city': city,
            'temp': temp,
            'feels_like': feels_like,
            'condition': condition,
            'date': timestamp
        })

def summarize_weather():
    df = pd.DataFrame(weather_records)
    daily_summary = df.groupby(['city', 'date']).agg(
        avg_temp=('temp', 'mean'),
        max_temp=('temp', 'max'),
        min_temp=('temp', 'min'),
        dominant_condition=('condition', lambda x: x.mode()[0])
    ).reset_index()
    return daily_summary

if __name__ == "__main__":
    pass