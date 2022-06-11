from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from typing import List

import db

from . import schema
from .import services

router = APIRouter(
    tags=['Tasks'],
    prefix='/tasks'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_task(request: schema.TaskBase,
                         database: Session = Depends(db.get_db)):

    task = await services.create_new_task(request, database)
    return task


@router.get('/', response_model=List[schema.TaskBase])
async def get_all_tasks(database: Session = Depends(db.get_db)):
    return await services.get_all_tasks(database)
