from pydantic import BaseModel, ConfigDict
from typing import Optional
from core.database import StatusEnum


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: StatusEnum


class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: StatusEnum

    model_config = ConfigDict(from_attributes=True)
