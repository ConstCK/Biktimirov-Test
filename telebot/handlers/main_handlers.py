from aiogram import Router, F, Bot

from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(F.text.startswith('1'))
async def text_handler(message: Message):
    await message.answer(text=f'Добро пожаловать в приложение с прогнозом погоды')


@router.message(Command('help'))
async def cmd_start(bot: Bot, message: Message):
    await message.answer(text=f'Добро пожаловать в приложение с прогнозом погоды')
