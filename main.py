from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

import model
import schema
from database import engine, get_db


# =====================================================
# CREATE DATABASE TABLES
# =====================================================

model.Base.metadata.create_all(bind=engine)


# =====================================================
# CREATE FASTAPI APP
# =====================================================

app = FastAPI(title="ToDo API")


# =====================================================
# FRONTEND CONFIGURATION
# =====================================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(
    directory="templates"
)


# =====================================================
# HOME
# =====================================================

@app.get("/")
def home():

    return {
        "message": "Welcome to ToDo API"
    }


# =====================================================
# FRONTEND
# =====================================================

@app.get(
    "/frontend",
    response_class=HTMLResponse
)
def frontend(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


# =====================================================
# CREATE TASK
# =====================================================

@app.post(
    "/todo",
    response_model=schema.CreateTaskResponse
)
def create_task(
    task: schema.CreateTaskRequest,
    db: Session = Depends(get_db)
):

    db_task = model.Task(
        task_name=task.task_name,
        description=task.description,
        time_limit=task.time_limit,
        status=task.status
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


# =====================================================
# GET ALL TASKS
# =====================================================

@app.get(
    "/todo",
    response_model=list[schema.CreateTaskResponse]
)
def get_all_tasks(
    db: Session = Depends(get_db)
):

    tasks = db.query(model.Task).all()

    return tasks


# =====================================================
# GET TASK BY ID
# =====================================================

@app.get(
    "/todo/{task_id}",
    response_model=schema.CreateTaskResponse
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    task = db.query(model.Task).filter(
        model.Task.id == task_id
    ).first()

    if task is None:

        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    return task


# =====================================================
# UPDATE ENTIRE TASK
# =====================================================

@app.put(
    "/todo/{task_id}",
    response_model=schema.UpdateTaskResponse
)
def update_task(
    task_id: int,
    task: schema.UpdateTaskRequest,
    db: Session = Depends(get_db)
):

    db_task = db.query(model.Task).filter(
        model.Task.id == task_id
    ).first()

    if db_task is None:

        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    db_task.task_name = task.task_name
    db_task.description = task.description
    db_task.time_limit = task.time_limit
    db_task.status = task.status

    db.commit()
    db.refresh(db_task)

    return db_task


# =====================================================
# PATCH TASK STATUS
# =====================================================

@app.patch(
    "/todo/{task_id}",
    response_model=schema.PatchTaskResponse
)
def patch_task(
    task_id: int,
    task: schema.PatchTaskRequest,
    db: Session = Depends(get_db)
):

    db_task = db.query(model.Task).filter(
        model.Task.id == task_id
    ).first()

    if db_task is None:

        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    if task.status is not None:

        db_task.status = task.status

    db.commit()
    db.refresh(db_task)

    return db_task


# =====================================================
# MARK ALL TASKS AS DONE
# =====================================================

@app.put("/todo")
def mark_all_done(
    db: Session = Depends(get_db)
):

    tasks = db.query(model.Task).all()

    if not tasks:

        raise HTTPException(
            status_code=404,
            detail="No Tasks Found"
        )

    for task in tasks:

        task.status = "Done"

    db.commit()

    return {
        "message": "All Tasks Marked as Done"
    }


# =====================================================
# DELETE TASK
# =====================================================

@app.delete("/todo/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    task = db.query(model.Task).filter(
        model.Task.id == task_id
    ).first()

    if task is None:

        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task Deleted Successfully"
    }


# =====================================================
# DELETE ALL TASKS
# =====================================================

@app.delete("/todo")
def delete_all_tasks(
    db: Session = Depends(get_db)
):

    tasks = db.query(model.Task).all()

    if not tasks:

        raise HTTPException(
            status_code=404,
            detail="No Tasks Found"
        )

    db.query(model.Task).delete()

    db.commit()

    return {
        "message": "All Tasks Deleted Successfully"
    }


# =====================================================
# HEALTH CHECK
# =====================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "message": "API is running successfully"
    }
