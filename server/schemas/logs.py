import datetime

from pydantic import BaseModel



# Базовая схема для log
class BaseLog(BaseModel):
    tg_id: int
    command: str
    created_at: datetime.datetime
    reply: str


# Схема для получения log
class Log(BaseLog):
    id: int


# Схема для создания log
class LogCreation(BaseLog):
    pass
