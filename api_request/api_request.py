import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("api_key")
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"


def fetch_data():
    print("Fetching weather data from weatherstack API....")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully")
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred in retrieving data: {e}")
        raise


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-10-12 11:18', 'localtime_epoch': 1760267880, 'utc_offset': '-4.0'}, 'current': {'observation_time': '03:18 PM', 'temperature': 15, 'weather_code': 122, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Overcast '], 'astro': {'sunrise': '07:04 AM', 'sunset': '06:20 PM', 'moonrise': '10:34 PM', 'moonset': '01:49 PM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 69}, 'air_quality': {'co': '197.85', 'no2': '15.15', 'o3': '69', 'so2': '5.05', 'pm2_5': '7.25', 'pm10': '7.95', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 29, 'wind_degree': 48, 'wind_dir': 'NE', 'pressure': 1020, 'precip': 0, 'humidity': 64, 'cloudcover': 25, 'feelslike': 15, 'uv_index': 1, 'visibility': 16, 'is_day': 'yes'}}


#fetch_data(api_url)
mock_fetch_data()