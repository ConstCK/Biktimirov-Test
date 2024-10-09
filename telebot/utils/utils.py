import requests

from .constants import CITY_COORDS_URL, WEATHER_FORECAST_URL, WEATHER_CODES


def get_city_coords(city_name: str) -> dict[str, str] | None:
    # Получение координат города по его названию с API

    params = {
        'name': city_name,
        'language': 'ru',
        'count': 1,
    }
    try:
        response = requests.get(
            CITY_COORDS_URL, params=params).json().get('results')[0]
        lat = response.get('latitude')
        lon = response.get('longitude')
        return {'latitude': lat, 'longitude': lon}
    except Exception:
        return None


def get_weather_forecast(lat: str, lon: str) -> dict[str, int] | None:
    # Получение текущих данных о погоде по указанным координатам с API
    params = {
        'latitude': lat,
        'longitude': lon,
        'current': ["temperature_2m", "apparent_temperature", "relative_humidity_2m", "weather_code", "wind_speed_10m"],
        'forecast_days': 1,
    }
    try:
        response = requests.get(WEATHER_FORECAST_URL,
                                params=params).json()
        forecast_temp = response.get('current').get(
            'temperature_2m')
        apparent_temperature = response.get('current').get(
            'apparent_temperature')
        wind_speed = response.get('current').get(
            'wind_speed_10m')
        humidity = response.get('current').get(
            'relative_humidity_2m')
        weather_code = response.get('current').get(
            'weather_code')
        weather = ''
        for k, v in WEATHER_CODES.items():
            if weather_code in k:
                weather = v
        return {'temperature': forecast_temp,
                'apparent_temperature': apparent_temperature,
                'wind_speed': wind_speed,
                'humidity': humidity,
                'weather': weather}

    except Exception:
        return None
