from fastapi import FastAPI
from app.routers import task, user
from app.backend.db import engine, Base
from app.models import User, Task

app = FastAPI()

# Генерация таблиц
Base.metadata.create_all(bind=engine)

app.include_router(task.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}
