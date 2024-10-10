from redis import asyncio as aioredis


class CacheService:
    def __init__(self) -> None:
        self.red = aioredis.from_url('redis://127.0.0.1:6379/0', encoding='utf8',
                                     decode_responses=True)

    async def set_item(self, key: str, item: str, expire_time: int = 60) -> None:
        # Создание объекта в БД типа str
        await self.red.set(key, item, expire_time)

    async def get_item(self, key: str) -> str | None:
        # Получение объекта из БД
        result = await self.red.get(key)
        return result

