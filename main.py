from fastapi import FastAPI, Depends
from fastapi.responses import Response

from crud import *
from schemes import *
from database import get_db


HOST = "localhost"
PORT = 8000

app = FastAPI()

Responses = {
    200: Response("ok", 200),
    404: Response("task not found", 404),
}
DependsDB = Depends(get_db)


@app.post("/tasks/", response_model=TaskResponse)
def add_task(task: TaskCreate, db=DependsDB):
    return create_task(db, task)


@app.get("/tasks/", response_model=list[TaskResponse])
def list_tasks(db=DependsDB):
    return get_tasks(db)


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def complete_task(task_id: int, completed: bool, db=DependsDB):
    if task := update_task(db, task_id, completed):
        return task
    return Responses[404]


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int, db=DependsDB):
    return Responses[delete_task(db, task_id)]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)
