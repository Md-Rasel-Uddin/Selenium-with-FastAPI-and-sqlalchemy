# tests/test_import_scraped.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base
from app import crud, models

TEST_DB = "sqlite:///./test_sms2.db"

def test_import_scraped():
    engine = create_engine(TEST_DB, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db = Session()

    items = [
        {"title":"T1", "url":"http://a", "category":"cat", "price":"£5"},
        {"title":"T2", "url":"http://b", "category":"cat2", "price":"£6"},
    ]
    objs = crud.import_scraped(db, items)
    assert len(objs) == 2
    db.close()
    Base.metadata.drop_all(engine)
