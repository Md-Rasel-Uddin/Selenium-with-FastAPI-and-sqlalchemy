# app/routers/students.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..db import get_db

router = APIRouter(prefix="/students", tags=["students"])

@router.post("", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@router.get("/{student_id}", response_model=schemas.StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    s = crud.get_student(db, student_id)
    if not s:
        raise HTTPException(404, "Student not found")
    return s

@router.post("/{student_id}/enroll", response_model=schemas.EnrollmentOut, tags=["enrollments"])
def enroll(student_id: int, payload: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    try:
        ent = crud.enroll_student(db, student_id, payload.course_id)
        return ent
    except IntegrityError:
        raise HTTPException(400, "Already enrolled")
    except ValueError as e:
        raise HTTPException(400, str(e))
