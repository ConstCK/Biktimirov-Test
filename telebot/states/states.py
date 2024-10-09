from aiogram.fsm.state import StatesGroup, State


class WeatherStages(StatesGroup):
    adding_city = State()
    forecast_getting = State()
