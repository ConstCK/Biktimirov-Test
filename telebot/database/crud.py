import datetime

from sqlalchemy import insert

from .config import async_session
from .models import Log


# Добавление log записи в БД
async def add_log(tg_id: int, command: str, created_at: datetime.datetime, reply: str) -> None:
    async with async_session() as session:
        stmt = insert(Log).values(tg_id=tg_id,
                                  command=command,
                                  created_at=created_at,
                                  reply=reply
                                  )
        await session.execute(stmt)
        await session.commit()




