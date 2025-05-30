from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

import requests

from pathlib import Path


async def get_students(db: Session):

    query = db.query(models.Students)

    students_all = query.all()
    students_all = (
        [new_data.to_dict() for new_data in students_all]
        if students_all
        else students_all
    )
    res = {
        "students_all": students_all,
    }
    return res


async def get_students_student_id(db: Session, student_id: int):

    query = db.query(models.Students)

    students_one = query.first()

    students_one = (
        (
            students_one.to_dict()
            if hasattr(students_one, "to_dict")
            else vars(students_one)
        )
        if students_one
        else students_one
    )

    res = {
        "students_one": students_one,
    }
    return res


async def delete_students_student_id(db: Session, student_id: int):

    students_deleted = None
    record_to_delete = (
        db.query(models.Students)
        .filter(models.Students.student_id == student_id)
        .first()
    )

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        students_deleted = record_to_delete.to_dict()

    res = {
        "students_deleted": students_deleted,
    }
    return res


async def get_courses(db: Session):

    query = db.query(models.Courses)

    courses_all = query.all()
    courses_all = (
        [new_data.to_dict() for new_data in courses_all] if courses_all else courses_all
    )
    res = {
        "courses_all": courses_all,
    }
    return res


async def get_courses_course_id(db: Session, course_id: int):

    query = db.query(models.Courses)

    courses_one = query.first()

    courses_one = (
        (
            courses_one.to_dict()
            if hasattr(courses_one, "to_dict")
            else vars(courses_one)
        )
        if courses_one
        else courses_one
    )

    res = {
        "courses_one": courses_one,
    }
    return res


async def put_courses_course_id(
    db: Session,
    course_id: int,
    course_name: str,
    course_code: str,
    description: str,
    credits: int,
):

    courses_edited_record = (
        db.query(models.Courses).filter(models.Courses.course_id == course_id).first()
    )
    for key, value in {
        "credits": credits,
        "course_id": course_id,
        "course_code": course_code,
        "course_name": course_name,
        "description": description,
    }.items():
        setattr(courses_edited_record, key, value)
    db.commit()
    db.refresh(courses_edited_record)
    courses_edited_record = courses_edited_record.to_dict()

    res = {
        "courses_edited_record": courses_edited_record,
    }
    return res


async def delete_courses_course_id(db: Session, course_id: int):

    courses_deleted = None
    record_to_delete = (
        db.query(models.Courses).filter(models.Courses.course_id == course_id).first()
    )

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        courses_deleted = record_to_delete.to_dict()

    res = {
        "courses_deleted": courses_deleted,
    }
    return res


async def get_instructors(db: Session):

    query = db.query(models.Instructors)

    instructors_all = query.all()
    instructors_all = (
        [new_data.to_dict() for new_data in instructors_all]
        if instructors_all
        else instructors_all
    )
    res = {
        "instructors_all": instructors_all,
    }
    return res


async def get_instructors_instructor_id(db: Session, instructor_id: int):

    query = db.query(models.Instructors)

    instructors_one = query.first()

    instructors_one = (
        (
            instructors_one.to_dict()
            if hasattr(instructors_one, "to_dict")
            else vars(instructors_one)
        )
        if instructors_one
        else instructors_one
    )

    res = {
        "instructors_one": instructors_one,
    }
    return res


async def put_instructors_instructor_id(
    db: Session,
    instructor_id: int,
    first_name: str,
    last_name: str,
    email: str,
    phone: str,
    department: str,
):

    instructors_edited_record = (
        db.query(models.Instructors)
        .filter(models.Instructors.instructor_id == instructor_id)
        .first()
    )
    for key, value in {
        "email": email,
        "phone": phone,
        "last_name": last_name,
        "department": department,
        "first_name": first_name,
        "instructor_id": instructor_id,
    }.items():
        setattr(instructors_edited_record, key, value)
    db.commit()
    db.refresh(instructors_edited_record)
    instructors_edited_record = instructors_edited_record.to_dict()

    res = {
        "instructors_edited_record": instructors_edited_record,
    }
    return res


async def delete_instructors_instructor_id(db: Session, instructor_id: int):

    instructors_deleted = None
    record_to_delete = (
        db.query(models.Instructors)
        .filter(models.Instructors.instructor_id == instructor_id)
        .first()
    )

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        instructors_deleted = record_to_delete.to_dict()

    res = {
        "instructors_deleted": instructors_deleted,
    }
    return res


async def post_instructors(
    db: Session, raw_data: schemas.PostInstructors, request: Request
):
    instructor_id: int = raw_data.instructor_id
    first_name: str = raw_data.first_name
    last_name: str = raw_data.last_name
    email: str = raw_data.email
    phone: str = raw_data.phone
    department: str = raw_data.department

    header_authorization: str = request.headers.get("header-authorization")

    record_to_be_added = {
        "email": email,
        "phone": phone,
        "last_name": last_name,
        "department": department,
        "first_name": first_name,
        "instructor_id": instructor_id,
    }
    new_instructors = models.Instructors(**record_to_be_added)
    db.add(new_instructors)
    db.commit()
    db.refresh(new_instructors)
    instructors_inserted_record = new_instructors.to_dict()

    headers = {"authorization": header_authorization}
    auth = ("", "")
    payload = {}
    apiResponse = requests.get(
        "https://cc1fbde45ead-in-south-01.backstract.io/sigma/api/v1/workspace/list",
        headers=headers,
        json=payload if "params" == "raw" else None,
    )
    workspace = apiResponse.json() if "dict" in ["dict", "list"] else apiResponse.text

    headers = {"authorization": header_authorization}
    auth = ("", "")
    payload = {"workspace_name": first_name, "workspace_description": last_name}
    apiResponse = requests.post(
        "https://cc1fbde45ead-in-south-01.backstract.io/sigma/api/v1/workspace/create",
        headers=headers,
        json=payload if "raw" == "raw" else None,
    )
    create_workspace = (
        apiResponse.json() if "dict" in ["dict", "list"] else apiResponse.text
    )
    res = {
        "instructors_inserted_record": instructors_inserted_record,
        "get_external_apis": workspace,
        "post_external_apis": create_workspace,
    }
    return res


async def post_students(db: Session, raw_data: schemas.PostStudents):
    student_id: int = raw_data.student_id
    first_name: str = raw_data.first_name
    last_name: str = raw_data.last_name
    dob: datetime.date = raw_data.dob
    gender: str = raw_data.gender
    email: str = raw_data.email
    phone: str = raw_data.phone
    address: str = raw_data.address
    enrollment_date: datetime.date = raw_data.enrollment_date
    page_size: int = raw_data.page_size
    page_number: int = raw_data.page_number

    record_to_be_added = {
        "dob": dob,
        "email": email,
        "phone": phone,
        "gender": gender,
        "address": address,
        "last_name": last_name,
        "first_name": first_name,
        "student_id": student_id,
        "enrollment_date": enrollment_date,
    }
    new_students = models.Students(**record_to_be_added)
    db.add(new_students)
    db.commit()
    db.refresh(new_students)
    students_inserted_record = new_students.to_dict()

    # user gproile
    headers = {"hellow": last_name}
    auth = ("", "")
    payload = {"hellometor": student_id}
    apiResponse = requests.get(
        "https://jsonplaceholder.typicode.com/todos/1",
        headers=headers,
        json=payload if "params" == "raw" else None,
    )
    user_details = (
        apiResponse.json() if "dict" in ["dict", "list"] else apiResponse.text
    )

    # mxhmdjfhg,sd
    headers = {}
    auth = ("", "")
    payload = {}
    apiResponse = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        headers=headers,
        json=payload if "raw" == "raw" else None,
    )
    user_details1 = (
        apiResponse.json() if "list" in ["dict", "list"] else apiResponse.text
    )
    res = {
        "students_inserted_record": students_inserted_record,
        "externa_json": user_details1,
        "extera_Detoa": user_details,
    }
    return res


async def post_courses(db: Session, raw_data: schemas.PostCourses):
    course_id: int = raw_data.course_id
    course_name: str = raw_data.course_name
    course_code: str = raw_data.course_code
    description: str = raw_data.description
    credits: int = raw_data.credits

    record_to_be_added = {
        "credits": credits,
        "course_id": course_id,
        "course_code": course_code,
        "course_name": course_name,
        "description": description,
    }
    new_courses = models.Courses(**record_to_be_added)
    db.add(new_courses)
    db.commit()
    db.refresh(new_courses)
    courses_inserted_record = new_courses.to_dict()

    res = {
        "courses_inserted_record": courses_inserted_record,
    }
    return res


async def put_students_student_id(
    db: Session,
    student_id: int,
    first_name: str,
    last_name: str,
    dob: str,
    gender: str,
    email: str,
    phone: str,
    address: str,
    enrollment_date: str,
    page_limit: str,
    page_number: str,
):

    students_edited_record = (
        db.query(models.Students)
        .filter(models.Students.student_id == student_id)
        .first()
    )
    for key, value in {
        "dob": dob,
        "email": email,
        "phone": phone,
        "gender": gender,
        "address": address,
        "last_name": last_name,
        "first_name": first_name,
        "student_id": student_id,
        "enrollment_date": enrollment_date,
    }.items():
        setattr(students_edited_record, key, value)
    db.commit()
    db.refresh(students_edited_record)
    students_edited_record = students_edited_record.to_dict()

    res = {
        "students_edited_record": students_edited_record,
    }
    return res
