from server.models.student import ResponseModel
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from server.database import subject_collection,subject_helper

from server.database import (
    add_subject
)
from server.models.student import (
    Subjects
)

router = APIRouter()

@router.post("/",response_description="subject and teacher added successfully")
def add_subject_data(subject: Subjects = Body(...)):
    subject = jsonable_encoder(subject)
    new_subject = add_subject(subject)
    return ResponseModel(new_subject, "Subject added successfully.")

@router.delete("/{id}",response_description="subject data has been deleted successfully")
def del_subject_data(id:str):
    del_id = ObjectId(id)
    subject = subject_collection.find_one({"_id": ObjectId(id)})
    if subject:
        subject_collection.delete_one({"_id": ObjectId(id)})
        return True

@router.get("/all/",response_description="List of subjects and its respective teachers")
def get_subject_data():
        subjects = []
        for subject in subject_collection.find():
            subjects.append(subject_helper(subject))
        return subjects

@router.get("/",response_description="subject detials of the selected id")
def get_subject_details(id:str):
    subject_id = ObjectId(id)
    subject = subject_collection.find_one({"_id": ObjectId(id)})
    return subject_helper(subject)

@router.put("/{id}",response_description="subject data has been deleted successfully")
def update_subject_data(id:str,subject: Subjects = Body(...)):
    
    req = {k: v for k, v in subject.dict().items() if v is not None}
    print("aaaaaaaaaaa",req)
    update_id = ObjectId(id)
    subject = subject_collection.update_one({"_id": ObjectId(id)},{"$set":req})
    if subject:
        return True
    else:
        return False
        


