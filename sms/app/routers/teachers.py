# app/routers/teachers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..db import get_db

router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.post("", response_model=schemas.TeacherOut)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud.create_teacher(db, teacher)

@router.get("/{teacher_id}", response_model=schemas.TeacherOut)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    t = crud.get_teacher(db, teacher_id)
    if not t:
        raise HTTPException(404, "Teacher not found")
    return t
