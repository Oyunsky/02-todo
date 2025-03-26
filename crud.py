__all__ = ["create_task", "get_tasks", "update_task", "delete_task"]

from sqlalchemy.orm import Session

from models import Task
from schemes import TaskCreate


def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session):
    return db.query(Task).all()


def update_task(db: Session, task_id: int, completed: bool):
    if task := db.query(Task).filter(Task.id == task_id).first():
        task.completed = completed
        db.commit()
    return task


def delete_task(db: Session, task_id: int):
    if task := db.query(Task).filter(Task.id == task_id).first():
        db.delete(task)
        db.commit()
        return 200
    return 404
