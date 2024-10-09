Скопируйте проект к себе на ПК при помощи: git clone **_Path_**
Перейдите в папку проекта
В терминале создайте виртуальное окружение (например python -m venv venv) и активируйте его (venv\scripts\activate)
Установите все зависимости при помощи pip install -r requirements.txt
Создайте файл .env в каталоге проекта и пропишите в нем настройки по примеру .env.example
Ключ для Django можно сгенерировать по пути https://djecrety.ir/
Создайте BOT_TOKEN при помощи Telegram BotFather 
Запустите сервер из каталога server (python manage.py runserver)
Запустите telebot из каталога telebot (python main.py)
Примечание: на ПК должно быть установлено PostgreSQL

EndPoints:
http://127.0.0.1:8000/api/ - Descriptions