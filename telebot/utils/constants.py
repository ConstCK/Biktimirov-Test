CITY_COORDS_URL = 'https://geocoding-api.open-meteo.com/v1/search'
WEATHER_FORECAST_URL = 'https://api.open-meteo.com/v1/forecast'

WEATHER_CODES = {

    (0,): ['Clear sky'],
    (1, 2, 3): ['Mainly clear', 'Partly cloudy', 'Overcast'],
    (45, 48): ['Fog', 'Depositing rime fog'],
    (51, 53, 55): ['Drizzle: Light', 'Drizzle:moderate', 'Drizzle: dense intensity'],
    (56, 57): ['Freezing Drizzle: Light', 'Freezing Drizzle: dense intensity'],
    (61, 63, 65): ['Rain: Slight', 'Rain:moderate', 'Rain: heavy intensity'],
    (66, 67): ['Freezing Rain: Light', 'Freezing Rain: heavy intensity'],
    (71, 73, 75): ['Snowfall: Slight', 'Snowfall:moderate', 'Snowfall: heavy intensity'],
    (77,): ['Snow grains'],
    (80, 81, 82): ['Rain showers: Slight', 'Rain showers:moderate', 'Rain showers: violent'],
    (85, 86): ['Snow showers: slight', 'Snow showers: heavy'],
    (95,): ['Thunderstorm: Slight or moderate'],
    (96, 99): ['Thunderstorm with slight hail',  'Thunderstorm with heavy hail']
}
