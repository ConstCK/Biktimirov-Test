import os

from dotenv import load_dotenv
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    bot_token: SecretStr = os.getenv('BOT_TOKEN')
    db_url: str = f'postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}'
    db_host: str = 'localhost'
    # Настройки для использования переменных из .env
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='allow')


settings = Settings()
