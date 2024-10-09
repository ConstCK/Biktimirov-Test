import logging
import asyncio
import os

from handlers.main_handlers import router as main_router
from config import dp, bot

# Добавление маршрута с обработчиками к диспетчеру
dp.include_routers(main_router,)


async def main():
    # запуск функции с созданием всех таблиц в БД
    # await create_tables()
    # Удаление всех необработанных сообщений после отключения бота
    # await bot.delete_webhook(drop_pending_updates=True)
    # Запуск обработчика всех событий
    await dp.start_polling(bot)


if __name__ == '__main__':
    # For development only (too slow for production)
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exiting program...')
