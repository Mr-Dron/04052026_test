from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
import enum

from core.settings import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(
    DATABASE_URL, echo=True
)  # echo для вывода всех выполняемых SQL-запросов в консоль, полено на стадии разработки

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,  # после комита данные остаются актуальные без повторного запроса в БД
    class_=AsyncSession,
)  # указывает на создание асинхронных сессий


class Base(DeclarativeBase):
    pass


class StatusEnum(str, enum.Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    DONE = "done"
