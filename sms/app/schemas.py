from pydantic import BaseModel, EmailStr
from typing import Optional

class PersonBase(BaseModel):
    full_name: str
    email: EmailStr


class StudentCreate(PersonBase):
    pass

class StudentOut(PersonBase):
    id: int
    class Config:
        from_attributes = True  # SQLAlchemy 2.x


class TeacherCreate(PersonBase):
    pass

class TeacherOut(PersonBase):
    id: int
    class Config:
        from_attributes = True


class CourseCreate(BaseModel):
    title: str
    capacity: int = 30
    teacher_id: Optional[int] = None

class CourseOut(CourseCreate):
    id: int
    class Config:
        from_attributes = True


class EnrollmentCreate(BaseModel):
    course_id: int

class EnrollmentOut(BaseModel):
    id: int
    student_id: int
    course_id: int
    class Config:
        from_attributes = True


class ScrapedData(BaseModel):
    title: str
    url: str
    category: Optional[str] = None
    price: Optional[str] = None
