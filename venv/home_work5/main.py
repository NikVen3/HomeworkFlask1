from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from typing import List, Optional

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str

class NewTask(BaseModel):
    title: str
    description: str
    status: str

TASKS = []

@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    return TASKS

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    task = next((task for task in TASKS if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks/", response_model=Task)
async def create_task(task: NewTask):
    new_task = Task(id=len(TASKS) + 1, **task.dict())
    TASKS.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: NewTask):
    for task in TASKS:
        if task.id == task_id:
            task.title = updated_task.title
            task.description = updated_task.description
            task.status = updated_task.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for index, task in enumerate(TASKS):
        if task.id == task_id:
            TASKS.pop(index)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")