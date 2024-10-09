import datetime
import json

from aiogram import Router

from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message

from utils.utils import get_city_coords, get_weather_forecast

from database.crud import add_log

router = Router()


# Стартовая команда
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=f'Добро пожаловать в приложение с прогнозом погоды {message.from_user.first_name}\n'
                         f'Используйте команду "/weather <город>" для получения текущего прогноза погоды\n'
                         f'Данный бот создан в качестве теста для компании BobrAi')


# Обработчик команды (/weather) получения прогноза погоды
@router.message(Command(commands=['weather']))
async def weather_handler(message: Message, command: CommandObject):
    await message.answer(text=f'Получен город {command.args}')
    if command.args:
        city = command.args
        coords = get_city_coords(city_name=city)
        if coords is not None:
            forecast = get_weather_forecast(lat=coords.get(
                'latitude'), lon=coords.get('longitude'))
            if forecast is not None:
                await message.answer(text=f'Текущая погода для города {message.text}:\n'
                                          f'Текущая температура: {
                                          forecast.get('temperature')},\n'
                                          f'Ощущаемая температура: {
                                          forecast.get('apparent_temperature')},/n'
                                          f'Скорость ветра: {
                                          forecast.get('wind_speed')},\n'
                                          f'Влажность воздуха: {
                                          forecast.get('humidity')},\n'
                                          f'Описание погоды: {forecast.get('weather')}')

                await add_log(tg_id=message.from_user.id,
                              command=f'/{command.command} {command.args}',
                              created_at=datetime.datetime.now(),
                              reply=json.dumps(forecast))


    else:
        await message.answer(text=f'Произошла ошибка получения данных. Введите название города заново.')




# Обработчик команды с полученным городом
# @router.message(StateFilter(WeatherStages.adding_city))
# async def weather_forecast_handler(message: Message, state: FSMContext):
#     city = message.text
#     coords = get_city_coords(city_name=city)
#     if coords is not None:
#         forecast = get_weather_forecast(lat=coords.get(
#             'latitude'), lon=coords.get('longitude'))
#         if forecast is not None:
#             await message.answer(text=f'Текущая погода для города {message.text}:\n'
#                                  f'Текущая температура: {
#                                      forecast.get('temperature')},\n'
#                                  f'Ощущаемая температура: {
#                                      forecast.get('apparent_temperature')},/n'
#                                  f'Скорость ветра: {
#                                      forecast.get('wind_speed')},\n'
#                                  f'Влажность воздуха: {
#                                      forecast.get('humidity')},\n'
#                                  f'Описание погоды: {forecast.get('weather')}')
#             await state.clear()
#
#             await add_log(tg_id=message.from_user.id,
#                           command=f'/weather {message.text}',
#                           created_at=datetime.datetime.now(),
#                           reply=json.dumps(forecast))
#     else:
#         await message.answer(text=f'Произошла ошибка получения данных. Введите название города заново.')
