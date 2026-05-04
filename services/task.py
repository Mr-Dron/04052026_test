from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from models import Tasks

import schemas.task as task_sch


async def create_task(data: task_sch.TaskCreate, db: AsyncSession) -> task_sch.TaskOut:
    task_data = data.model_dump()

    new_task = Tasks(**task_data)
    db.add(new_task)

    await db.commit()
    await db.refresh(new_task)

    return new_task


async def get_all_tasks(db: AsyncSession) -> list[task_sch.TaskOut]:

    tasks_list = (await db.execute(select(Tasks))).scalars().all()

    return tasks_list


async def get_task(task_id: int, db: AsyncSession) -> task_sch.TaskOut:
    task = (
        await db.execute(select(Tasks).where(Tasks.id == task_id))
    ).scalar_one_or_none()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"Task with id {task_id} not found "},
        )

    return task
