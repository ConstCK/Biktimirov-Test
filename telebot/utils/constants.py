CITY_COORDS_URL = 'https://geocoding-api.open-meteo.com/v1/search'
WEATHER_FORECAST_URL = 'https://api.open-meteo.com/v1/forecast'

WEATHER_CODES = {

    (0,): 'Clear sky',
    (1, 2, 3): 'Mainly clear, partly cloudy, and overcast',
    (45, 48): 'Fog and depositing rime fog',
    (51, 53, 55): 'Drizzle: Light, moderate, and dense intensity',
    (56, 57): 'Freezing Drizzle: Light and dense intensity',
    (61, 63, 65): 'Rain: Slight, moderate and heavy intensity',
    (66, 67): 'Freezing Rain: Light and heavy intensity',
    (71, 73, 75): 'Snowfall: Slight, moderate, and heavy intensity',
    (77,): 'Snow grains',
    (80, 81, 82): 'Rain showers: Slight, moderate, and violent',
    (85, 86): 'Snow showers: slight and heavy',
    (95,): 'Thunderstorm: Slight or moderate',
    (96, 99): 'Thunderstorm with slight and heavy hail'
}
