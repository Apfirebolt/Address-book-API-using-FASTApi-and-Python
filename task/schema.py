from typing import Optional
from pydantic import BaseModel, constr


class TaskBase(BaseModel):
    id: Optional[int]
    name: str
    description: str

    class Config:
        orm_mode = True
