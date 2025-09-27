from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from . import models, schemas


# ---------------- Students ----------------
def create_student(db: Session, student: schemas.StudentCreate):
    db_obj = models.Student(full_name=student.full_name, email=student.email)
    db.add(db_obj)
    try:
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except IntegrityError:
        db.rollback()
        raise HTTPException(400, "Email already exists")


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


# ---------------- Teachers ----------------
def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_obj = models.Teacher(full_name=teacher.full_name, email=teacher.email)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()


# ---------------- Courses ----------------
def create_course(db: Session, course: schemas.CourseCreate):
    db_obj = models.Course(title=course.title, capacity=course.capacity, teacher_id=course.teacher_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


# ---------------- Enrollments ----------------
def enroll_student(db: Session, student_id: int, course_id: int):
    course = get_course(db, course_id)
    if not course:
        raise ValueError("Course not found")
    student = get_student(db, student_id)
    if not student:
        raise ValueError("Student not found")

    exists = db.query(models.Enrollment).filter_by(student_id=student_id, course_id=course_id).first()
    if exists:
        raise IntegrityError(None, None, None)

    current = db.query(models.Enrollment).filter_by(course_id=course_id).count()
    if current >= course.capacity:
        raise ValueError("Course full")

    ent = models.Enrollment(student_id=student_id, course_id=course_id)
    db.add(ent)
    db.commit()
    db.refresh(ent)
    return ent


# ---------------- Scraped Resources ----------------
def import_scraped(db: Session, items: list[schemas.ScrapedData]):
    objs = []
    for it in items:
        obj = models.ScrapedResource(
            title=it.title,
            url=it.url,
            category=it.category,
            price=it.price,
        )
        db.add(obj)
        objs.append(obj)
    db.commit()
    return objs

def get_scraped(db: Session):
    return db.query(models.ScrapedResource).all()
