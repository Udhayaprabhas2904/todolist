from pydantic import BaseModel
from typing import Optional



class CreateTaskRequest(BaseModel):
    task_name: str
    description: str
    time_limit: int
    status: str


class CreateTaskResponse(BaseModel):
    id: int
    task_name: str
    description: str
    time_limit: int
    status: str

    class Config:
        from_attributes = True




class UpdateTaskRequest(BaseModel):
    task_name: str
    description: str
    time_limit: int
    status: str


class UpdateTaskResponse(BaseModel):
    id: int
    task_name: str
    description: str
    time_limit: int
    status: str

    class Config:
        from_attributes = True


# ---------- PATCH ----------

class PatchTaskRequest(BaseModel):
    status: Optional[str] = None


class PatchTaskResponse(BaseModel):
    id: int
    task_name: str
    description: str
    time_limit: int
    status: str

    class Config:
        from_attributes = True