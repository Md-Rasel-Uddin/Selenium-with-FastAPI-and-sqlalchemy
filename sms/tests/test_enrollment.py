# tests/test_enrollment.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base, get_db
from app import crud, models

TEST_DB = "sqlite:///./test_sms.db"

@pytest.fixture(scope="module")
def db_session():
    engine = create_engine(TEST_DB, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_enroll_and_capacity(db_session):
    # create student
    s = models.Student(full_name="S1", email="s1@example.com")
    db_session.add(s)
    # create course with capacity 1
    c = models.Course(title="C1", capacity=1)
    db_session.add(c)
    db_session.commit()

    ent = crud.enroll_student(db_session, s.id, c.id)
    assert ent.student_id == s.id

    # second student should not be able to enroll
    s2 = models.Student(full_name="S2", email="s2@example.com")
    db_session.add(s2)
    db_session.commit()

    with pytest.raises(ValueError):
        crud.enroll_student(db_session, s2.id, c.id)
