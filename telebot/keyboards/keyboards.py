# Создание клавиатуры для использования в /start
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Создание клавиатуры для использования в /start
async def base_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text='Установить любимый город'))
    builder.add(KeyboardButton(text='Получить прогноз любимого города'))
    return builder.adjust(2).as_markup(resize_keyboard=True)