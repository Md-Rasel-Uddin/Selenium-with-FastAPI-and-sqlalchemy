# app/routers/courses.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..db import get_db

router = APIRouter(prefix="/courses", tags=["courses"])

@router.post("", response_model=schemas.CourseOut)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    # optional: validate teacher exists if provided
    if course.teacher_id:
        if not crud.get_teacher(db, course.teacher_id):
            raise HTTPException(400, "Teacher not found")
    return crud.create_course(db, course)

@router.get("/{course_id}", response_model=schemas.CourseOut)
def get_course(course_id: int, db: Session = Depends(get_db)):
    c = crud.get_course(db, course_id)
    if not c:
        raise HTTPException(404, "Course not found")
    return c
