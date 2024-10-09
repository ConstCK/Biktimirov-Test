import datetime

from sqlalchemy import BigInteger, func
from sqlalchemy.orm import Mapped, mapped_column

from .config import Base


class Log(Base):
    __tablename__ = 'logs'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    command: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now()
                                                          , default=datetime.datetime.now())
    reply: Mapped[str]

