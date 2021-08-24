# import motor.motor_asyncio
from bson.objectid import ObjectId


# MONGO_DETAILS = "mongodb://localhost:27017"

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database = client.students

# student_collection = database.get_collection("students_collection")

from pymongo import MongoClient
client = MongoClient()
database = client["students"]
student_collection = database.get_collection("students_collection")
subject_collection = database.get_collection("subject_collection")
todolist_collection = database.get_collection("todo_collection")

# helpers

def todo_helper(todo) -> dict:
    return {
        "task_name":todo["task_name"],
        "priority" : todo["priority"]
    }
