from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .db import Base

class Person(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)


class Student(Person):
    __tablename__ = "students"
    enrollments = relationship("Enrollment", back_populates="student")


class Teacher(Person):
    __tablename__ = "teachers"
    courses = relationship("Course", back_populates="teacher")


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))

    teacher = relationship("Teacher", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")


class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    __table_args__ = (UniqueConstraint("student_id", "course_id", name="uix_student_course"),)


class ScrapedResource(Base):
    __tablename__ = "scraped_resources"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    category = Column(String)
    price = Column(String)
