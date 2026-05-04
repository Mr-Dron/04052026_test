from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status

from core.config import get_session
import services.task as task_ser
import schemas.task as task_sch

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=task_sch.TaskOut)
async def create_task(
    data: task_sch.TaskCreate, db: AsyncSession = Depends(get_session)
):
    return await task_ser.create_task(data=data, db=db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[task_sch.TaskOut])
async def get_all(db: AsyncSession = Depends(get_session)):
    return await task_ser.get_all_tasks(db=db)


@router.get("/id/{id}", status_code=status.HTTP_200_OK, response_model=task_sch.TaskOut)
async def get_task(id: int, db: AsyncSession = Depends(get_session)):
    return await task_ser.get_task(task_id=id, db=db)
