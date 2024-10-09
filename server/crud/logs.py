from fastapi import Depends
from fastapi_pagination import Page, paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from models.logs import Log as LogTable

from schemas.logs import Log

from filters.logs import LogFilter

from database.db import get_session


class LogService:
    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        self.db = session

    # Получение списка всех пользователей
    async def get_logs(self, date_filter) -> Page[Log] | list:

            query = date_filter.filter(select(LogTable))
            # query = select(LogTable)
            result = await self.db.execute(query)
            return paginate(result.scalars().all())


    # Получение списка всех пользователей
    async def get_logs_by_user(self, tg_id: int) -> Page[Log] | list:
        query = select(LogTable).where(LogTable.tg_id == tg_id)
        result = await self.db.execute(query)
        return paginate(result.scalars().all())
