from fastapi import FastAPI
from server.routes.todolist import router as TaskRouter

app = FastAPI()


app.include_router(TaskRouter, tags=["Tasks"], prefix="/tasks")
