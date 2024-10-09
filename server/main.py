
from fastapi import FastAPI
import uvicorn
from fastapi_pagination import add_pagination, set_params, Params

from config import settings
from routers.logs import router as log_router


# Создание основного приложения
app = FastAPI(
    title='Logs API',
    description='API для получение логов запросов к WEATHER API',
)

# Добавление пагинации в приложение
add_pagination(app)


# Включение маршрутов в основное приложение
app.include_router(log_router, tags=['logs'])


@app.get('/', description='Приветственная надпись', )
async def greetings() -> dict:
    return {'message': 'Добро пожаловать в API получения логов'}


# Запуск сервера
if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.db_host, port=8000, reload=True)
