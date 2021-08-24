from starlette.responses import Response
from server.models.student import ResponseModel
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from server.database import todo_helper,todolist_collection
from server.models.todolist import ToDoList

router = APIRouter()

@router.post("/",response_description="Task added successfully")
def add_task_data(todo: ToDoList = Body(...)):
    todo = jsonable_encoder(todo)
    new_todo = todolist_collection.insert_one(todo)
    todo_details = todolist_collection.find_one({"_id": new_todo.inserted_id})
    return Response ("Task added successfully.")

@router.delete("/{id}",response_description="Task has been deleted successfully")
def del_task_data(id:str):
    todo = todolist_collection.find_one({"_id": ObjectId(id)})
    if todo:
        todolist_collection.delete_one({"_id": ObjectId(id)})
        return True

@router.get("/all/",response_description="List of Task and its respective priorities")
def get_task_data():
        todo_list = []
        if todolist_collection.find():
            for task in todolist_collection.find():
                todo_list.append(todo_helper(task))
        return todo_list

@router.get("/",response_description="subject detials of the selected id")
def get_task_details(id:str):
    tasks = todolist_collection.find_one({"_id": ObjectId(id)})
    return todo_helper(tasks)

@router.put("/{id}",response_description="subject data has been deleted successfully")
def update_task_data(id:str,todo: ToDoList = Body(...)):
    
    req = {k: v for k, v in todo.dict().items() if v is not None}
    subject = todolist_collection.update_one({"_id": ObjectId(id)},{"$set":req})
    if subject:
        return True
    else:
        return False