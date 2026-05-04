from sqlalchemy import Integer, Column, String, Enum
from core.database import Base, StatusEnum


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(StatusEnum), nullable=False)
