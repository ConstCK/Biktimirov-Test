from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from config import settings

# Создание движка для связи с БД
engine = create_async_engine(url=settings.db_url, future=True, echo=False)

# Создание асинхронной сессии
async_session = async_sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


# Создание класса-родителя для наследования при создании моделей
class Base(DeclarativeBase):
    pass


# Создание сессии
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
