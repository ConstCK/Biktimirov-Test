from aiogram.fsm.state import StatesGroup, State


class UserStages(StatesGroup):
    adding_city = State()
    getting_forecast = State()