from typing import Optional

from pydantic import BaseModel, EmailStr,Field

class ToDoList(BaseModel):
    task_name:str=Field(...)
    priority:str=Field(...)