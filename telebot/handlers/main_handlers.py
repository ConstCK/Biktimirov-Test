from aiogram import Router, F, Bot

from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.states import WeatherStages
from utils.utils import get_city_coords, get_weather_forecast

router = Router()


# Стартовая команда
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(text=f'Добро пожаловать в приложение с прогнозом погоды {message.from_user.first_name}\n'
                              f'Используйте команду "/weather" для получения текущего прогноза погоды')


# Обработчик команды (/weather) получения прогноза погоды
@router.message(Command('weather'))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text='Введите название города для получения текущего прогноза погоды:')
    await state.set_state(WeatherStages.adding_city)


# Обработчик команды с полученным городомэ
@router.message(StateFilter(WeatherStages.adding_city))
async def cmd_start(message: Message, state: FSMContext):
    city = message.text
    coords = get_city_coords(city_name=city)
    if coords is not None:
        forecast = get_weather_forecast(lat=coords.get('latitude'), lon=coords.get('longitude'))
        if forecast is not None:
            await message.answer(text=f'Текущая погода для города {message.text}:\n'
                                      f'Текущая температура: {forecast.get('temperature')},\n'
                                      f'Ощущаемая температура: {forecast.get('apparent_temperature')},/n'
                                      f'Скорость ветра: {forecast.get('wind_speed')},\n'
                                      f'Влажность воздуха: {forecast.get('humidity')},\n'
                                      f'Описание погоды: {forecast.get('weather')}')
            await state.clear()
            # add_data_to_db()
    else:
        await message.answer(text=f'Произошла ошибка получения данных. Введите город заново.')
