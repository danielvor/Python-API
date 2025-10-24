from fastapi import FastAPI, HTTPException
from models import Task
from typing import List
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["*"] para todos os domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Config MongoDB
MONGO_URI = os.getenv("MONGO_URI")

@app.on_event("startup")
async def start_db():
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(database=client.todo_db, document_models=[Task])


class TaskUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    await task.create()
    return task


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return await Task.find_all().to_list()


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: str):
    task = await Task.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, update: TaskUpdate):
    task = await Task.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if update.title is not None:
        task.title = update.title
    if update.content is not None:
        task.content = update.content
    
    await task.save()
    return task


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    task = await Task.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    await task.delete()
    return {"message": "Task deleted"}
