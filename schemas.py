from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Students(BaseModel):
    student_id: int
    first_name: str
    last_name: str
    dob: datetime.date
    gender: str
    email: str
    phone: str
    address: str
    enrollment_date: datetime.date


class ReadStudents(BaseModel):
    student_id: int
    first_name: str
    last_name: str
    dob: datetime.date
    gender: str
    email: str
    phone: str
    address: str
    enrollment_date: datetime.date
    class Config:
        from_attributes = True


class Courses(BaseModel):
    course_id: int
    course_name: str
    course_code: str
    description: str
    credits: int


class ReadCourses(BaseModel):
    course_id: int
    course_name: str
    course_code: str
    description: str
    credits: int
    class Config:
        from_attributes = True


class Classes(BaseModel):
    class_id: int
    course_id: int
    instructor_id: int
    semester: str
    schedule: str


class ReadClasses(BaseModel):
    class_id: int
    course_id: int
    instructor_id: int
    semester: str
    schedule: str
    class Config:
        from_attributes = True


class Instructors(BaseModel):
    instructor_id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    department: str


class ReadInstructors(BaseModel):
    instructor_id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    department: str
    class Config:
        from_attributes = True


class Enrollments(BaseModel):
    enrollment_id: int
    student_id: int
    course_id: int
    enrolled_on: datetime.date
    grade: str


class ReadEnrollments(BaseModel):
    enrollment_id: int
    student_id: int
    course_id: int
    enrolled_on: datetime.date
    grade: str
    class Config:
        from_attributes = True




class PostInstructors(BaseModel):
    instructor_id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    department: str

    class Config:
        from_attributes = True



class PostStudents(BaseModel):
    student_id: int
    first_name: str
    last_name: str
    dob: Any
    gender: str
    email: str
    phone: str
    address: str
    enrollment_date: Any
    page_size: int
    page_number: int

    class Config:
        from_attributes = True



class PostCourses(BaseModel):
    course_id: int
    course_name: str
    course_code: str
    description: str
    credits: int

    class Config:
        from_attributes = True

