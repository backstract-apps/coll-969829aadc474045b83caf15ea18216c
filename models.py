from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Students(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String, primary_key=False)
    last_name = Column(String, primary_key=False)
    dob = Column(Date, primary_key=False)
    gender = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    phone = Column(String, primary_key=False)
    address = Column(String, primary_key=False)
    enrollment_date = Column(Date, primary_key=False)


class Courses(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String, primary_key=False)
    course_code = Column(String, primary_key=False)
    description = Column(String, primary_key=False)
    credits = Column(Integer, primary_key=False)


class Classes(Base):
    __tablename__ = 'classes'
    class_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, primary_key=False)
    instructor_id = Column(Integer, primary_key=False)
    semester = Column(String, primary_key=False)
    schedule = Column(String, primary_key=False)


class Instructors(Base):
    __tablename__ = 'instructors'
    instructor_id = Column(Integer, primary_key=True)
    first_name = Column(String, primary_key=False)
    last_name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    phone = Column(String, primary_key=False)
    department = Column(String, primary_key=False)


class Enrollments(Base):
    __tablename__ = 'enrollments'
    enrollment_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, primary_key=False)
    course_id = Column(Integer, primary_key=False)
    enrolled_on = Column(Date, primary_key=False)
    grade = Column(String, primary_key=False)


