import datetime
from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from models.logs import Log
from pydantic import Field


class LogFilter(Filter):
    created_at__gte: Optional[datetime.date] = Field(default=None, description='>')
    created_at__lte: Optional[datetime.date] = Field(default=None)

    class Constants(Filter.Constants):
        model = Log

    class Config:
        populate_by_name = True
