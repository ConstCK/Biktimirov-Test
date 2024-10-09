import datetime
import requests

from .constants import CITY_COORDS_URL, WEATHER_FORECAST_URL


def get_coords_by_city(city_name: str) -> dict[str, str] | None:
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
    # Получение температуры на ближайший час по координатам города с API
    params = {
        'latitude': lat,
        'longitude': lon,
        'hourly': 'temperature_2m',
        'forecast_days': 1,
    }
    try:
        response = requests.get(WEATHER_FORECAST_URL,
                                params=params).json()
        current_time = datetime.datetime.now().hour
        # Список всех временных отрезков суток
        time_list = response.get('hourly').get('time')
        # Перевод в datetime формат
        time_obj_list = list(map(lambda x: datetime.datetime.strptime(
            x, '%Y-%m-%dT%H:%M'), time_list))
        # Выбор часа больше текущего
        forecast_time = [x for x in time_obj_list if x.hour > current_time][0]
        forecast_hour = forecast_time.hour
        # Выбор температуры на ближайший час
        forecast_temp = response.get('hourly').get(
            'temperature_2m')[forecast_hour]
        return {'hour': forecast_hour, 'temperature': forecast_temp}

    except Exception:
        return None

