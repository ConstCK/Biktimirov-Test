import datetime
import json

from aiogram import Router, F

from aiogram.filters import CommandStart, Command, CommandObject, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.utils import get_city_coords, get_weather_forecast
from database.crud import add_log
from keyboards.keyboards import base_keyboard
from states.states import UserStages
from services.validators import city_name_is_valid
from cache.service import CacheService

router = Router()
cache_service = CacheService()


# Стартовая команда
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=f'Добро пожаловать в приложение с прогнозом погоды {message.from_user.first_name}.\n'
                              f'Используйте команду "/weather <город>" для получения текущего прогноза погоды.\n'
                              f'Данный бот создан в качестве теста для компании BobrAi.',
                         reply_markup=await base_keyboard())


# Обработчик команды (/weather) получения прогноза погоды
@router.message(Command(commands=['weather']))
async def forecast_handler(message: Message, command: CommandObject):
    if command.args:
        city = command.args
        cached_data = await cache_service.get_item(key=city)
        if cached_data:
            cached_data = json.loads(cached_data)
            await message.answer(text='Получение данных из кэша...')
            await message.answer(text=f'Текущая погода для города {message.text}:\n'
                                      f'Текущая температура: {
                                      cached_data.get('temperature')} ℃,\n'
                                      f'Ощущаемая температура: {cached_data.get('apparent_temperature')} ℃,\n'
                                      f'Скорость ветра: {
                                      cached_data.get('wind_speed')} м/с,\n'
                                      f'Влажность воздуха: {
                                      cached_data.get('humidity')} %,\n'
                                      f'Описание погоды: {cached_data.get('weather')}.',
                                 reply_markup=await base_keyboard())
        else:
            if city_name_is_valid(city):
                coords = get_city_coords(city_name=city)
                if coords is not None:
                    await message.answer(text=f'Получен город {command.args}.')
                    forecast = get_weather_forecast(lat=coords.get(
                        'latitude'), lon=coords.get('longitude'))
                    if forecast is not None:
                        await message.answer(text=f'Текущая погода для города {message.text}:\n'
                                                  f'Текущая температура: {
                                                  forecast.get('temperature')} ℃,\n'
                                                  f'Ощущаемая температура: {
                                                  forecast.get('apparent_temperature')} ℃,\n'
                                                  f'Скорость ветра: {
                                                  forecast.get('wind_speed')} м/c,\n'
                                                  f'Влажность воздуха: {
                                                  forecast.get('humidity')} %,\n'
                                                  f'Описание погоды: {forecast.get('weather')}.',
                                             reply_markup=await base_keyboard())

                        await add_log(tg_id=message.from_user.id,
                                      command=f'/{command.command} {command.args}',
                                      created_at=datetime.datetime.now(),
                                      reply=json.dumps(forecast))
                        await message.answer(text='Кэширование данных...')
                        await cache_service.set_item(key=city,
                                                     item=json.dumps({'temperature': forecast.get('temperature'),
                                                                      'apparent_temperature': forecast.get(
                                                                          'apparent_temperature'),
                                                                      'wind_speed': forecast.get('wind_speed'),
                                                                      'humidity': forecast.get('humidity'),
                                                                      'weather': forecast.get('weather')
                                                                      }))

                else:
                    await message.answer(text='Невозможно определить расположение указанного города. Повторите ввод...')
            else:
                await message.answer(text='Некорректное название города. Повторите ввод...')
    else:
        await message.answer(text='Произошла ошибка получения данных. Введите название города заново...')


# Обработчик запроса любимого города
@router.message(F.text == 'Установить любимый город')
async def city_request_handler(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(UserStages.adding_city)
    await message.answer(text='Введите название любимого города.')


# Обработчик добавления любимого города
@router.message(StateFilter(UserStages.adding_city))
async def weather_handler(message: Message, state: FSMContext):
    city = message.text
    coords = get_city_coords(city_name=city)
    if coords:
        await message.answer(text=f'Ваш любимый город {city}.',
                             reply_markup=await base_keyboard())
        await state.update_data(lat=coords.get(
            'latitude'), lon=coords.get('longitude'), city=city)
        await state.set_state(state=None)
    else:
        await message.answer(text=f'Ошибка получения любимого города. Повторите ввод...',
                             reply_markup=await base_keyboard())


# Обработчик запроса прогноза погоды для любимого города
@router.message(F.text == 'Получить прогноз любимого города')
async def city_request_handler(message: Message, state: FSMContext):
    await state.set_state(state=None)
    data_storage = await state.get_data()
    city = data_storage.get('city')
    if city:
        forecast = get_weather_forecast(lat=data_storage.get(
            'lat'), lon=data_storage.get('lon'))
        if forecast is not None:
            await message.answer(text=f'Текущая погода для города {city}:\n'
                                      f'Текущая температура: {
                                      forecast.get('temperature')} ℃,\n'
                                      f'Ощущаемая температура: {
                                      forecast.get('apparent_temperature')} ℃,\n'
                                      f'Скорость ветра: {
                                      forecast.get('wind_speed')} м/с,\n'
                                      f'Влажность воздуха: {
                                      forecast.get('humidity')} %,\n'
                                      f'Описание погоды: {forecast.get('weather')}.',
                                 reply_markup=await base_keyboard())

            await add_log(tg_id=message.from_user.id,
                          command=f'/weather {city}',
                          created_at=datetime.datetime.now(),
                          reply=json.dumps(forecast))

    else:
        await message.answer(text=f'Произошла ошибка получения данных. Введите название города заново...',
                             reply_markup=await base_keyboard())
