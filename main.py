from fastapi import FastAPI, status
from contextlib import asynccontextmanager

from core.database import Base, engine
import routers.task as task_rou
import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)


app.include_router(task_rou.router)

# router_list = [task_rou.router]           При масштабировании и добавлении новых роутов

# for router in router_list:
#     app.include_router(router)


@app.get("/", status_code=status.HTTP_200_OK)
async def helloworld():
    return {"message": "Hello world"}
