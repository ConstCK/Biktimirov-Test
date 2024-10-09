from fastapi import FastAPI
import uvicorn
from fastapi_pagination import add_pagination, set_params, Params, resolve_params

from config import settings
from routers.logs import router as log_router


# Создание основного приложения
app = FastAPI(
    title='Logs API',
    description='API для получение логов запросов к WEATHER API',
)
add_pagination(app)
set_params(Params(page=2, size=10))
print(resolve_params())
# Включение маршрутов в основное приложение
app.include_router(log_router, tags=['logs'])


@app.get('/', description='Приветственная надпись', )
async def greetings() -> dict:
    return {'message': 'Greetings, sir'}


# Запуск сервера
if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.db_host, port=8000, reload=True)
