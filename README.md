Скопируйте проект к себе на ПК при помощи: git clone **_Path_**
Перейдите в папку проекта
В терминале создайте виртуальное окружение (например python -m venv venv) и активируйте его (venv\scripts\activate)
Установите все зависимости при помощи pip install -r requirements.txt
Создайте файл .env в каталоге проекта и пропишите в нем настройки по примеру .env.example
Ключ для Django можно сгенерировать по пути https://djecrety.ir/ 
Создайте BOT_TOKEN при помощи Telegram BotFather 
Примечание: на ПК должно быть установлено PostgreSQL

Запуск:
Запустите сервер из каталога server (python main.py)
Запустите telebot из каталога telebot (python main.py)
Следуйте инструкциям в telegram в https://t.me/constantin_weather_bot

EndPoints:
http://127.0.0.1:8000/api/v1/logs - Все логи
http://127.0.0.1:8000/api/v1/logs/ID - Все логи пользователя с указанным ID
http://127.0.0.1:8000/docs - Swagger документация
http://127.0.0.1:8000/redoc - Альтернативный вариант документации