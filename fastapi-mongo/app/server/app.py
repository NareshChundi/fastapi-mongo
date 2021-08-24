from fastapi import FastAPI
from server.routes.student import router as StudentRouter
from server.routes.subjects import router as SubjectRouter
from server.routes.todolist import router as TaskRouter

app = FastAPI()


app.include_router(TaskRouter, tags=["Tasks"], prefix="/tasks")
# app.include_router(StudentRouter, tags=["Student"], prefix="/student")
# app.include_router(SubjectRouter, tags=["subject"], prefix="/subject")



# @app.get("/", tags=["Root"])
# def read_root():
#     return {"message": "Welcome to this fantastic app!"}