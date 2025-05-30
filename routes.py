from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/student_id')
async def get_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_student_id(db, student_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/student_id')
async def delete_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_student_id(db, student_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/courses/')
async def get_courses(db: Session = Depends(get_db)):
    try:
        return await service.get_courses(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/courses/course_id')
async def get_courses_course_id(course_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_courses_course_id(db, course_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/courses/course_id/')
async def put_courses_course_id(course_id: int, course_name: str, course_code: str, description: str, credits: int, db: Session = Depends(get_db)):
    try:
        return await service.put_courses_course_id(db, course_id, course_name, course_code, description, credits)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/courses/course_id')
async def delete_courses_course_id(course_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_courses_course_id(db, course_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/instructors/')
async def get_instructors(db: Session = Depends(get_db)):
    try:
        return await service.get_instructors(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/instructors/instructor_id')
async def get_instructors_instructor_id(instructor_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_instructors_instructor_id(db, instructor_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/instructors/instructor_id/')
async def put_instructors_instructor_id(instructor_id: int, first_name: str, last_name: str, email: str, phone: str, department: str, db: Session = Depends(get_db)):
    try:
        return await service.put_instructors_instructor_id(db, instructor_id, first_name, last_name, email, phone, department)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/instructors/instructor_id')
async def delete_instructors_instructor_id(instructor_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_instructors_instructor_id(db, instructor_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/instructors/')
async def post_instructors(raw_data: schemas.PostInstructors, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_instructors(db, raw_data, headers)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(raw_data: schemas.PostStudents, db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/courses/')
async def post_courses(raw_data: schemas.PostCourses, db: Session = Depends(get_db)):
    try:
        return await service.post_courses(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/student_id/')
async def put_students_student_id(student_id: int, first_name: str, last_name: str, dob: str, gender: str, email: str, phone: str, address: str, enrollment_date: str, page_limit: str, page_number: str, db: Session = Depends(get_db)):
    try:
        return await service.put_students_student_id(db, student_id, first_name, last_name, dob, gender, email, phone, address, enrollment_date, page_limit, page_number)
    except Exception as e:
        raise HTTPException(500, str(e))

