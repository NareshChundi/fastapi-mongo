from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
    add_subject,
)
from server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
    Subjects
)

router = APIRouter()

@router.post("/", response_description="Student data added into the database")
def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = add_student(student)
    return ResponseModel(new_student, "Student added successfully.")

@router.get("/", response_description="Students retrieved")
def get_students():
    students = retrieve_students()
    if students:
        return ResponseModel(students, "Students data retrieved successfully")
    return ResponseModel(students, "Empty list returned")

@router.post("/subject/",response_description="subject and teacher added successfully")
def add_subject_data(subject: Subjects = Body(...)):
    subject = jsonable_encoder(subject)
    new_subject = add_subject(subject)
    return ResponseModel(new_subject, "Student added successfully.")

@router.delete("/{id}", response_description="Student data deleted from the database")
def delete_student_data(id: str):
    deleted_student = delete_student(id)
    if deleted_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id), "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )