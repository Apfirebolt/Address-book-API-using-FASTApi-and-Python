from fastapi import HTTPException, status
from typing import List
from . import models


async def create_new_task(request, database) -> models.Task:
    new_task = models.Task(name=request.name, description=request.description)
    database.add(new_task)
    database.commit()
    database.refresh(new_task)
    return new_task


async def get_all_tasks(database) -> List[models.Task]:
    tasks = database.query(models.Task).all()
    return tasks


async def get_task_by_id(task_id, database):
    task = database.query(models.Task).get(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Data Not Found !"
        )
    return task


async def delete_task_by_id(task_id, database):
    database.query(models.Task).filter(
        models.Task.id == task_id).delete()
    database.commit()


async def update_task_by_id(task_id, request, database):
    task = database.query(models.Task).get(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task Not Found !"
        )
    task.name = request.name if request.name else task.name
    task.description = request.description if request.description else task.description
    database.commit()




