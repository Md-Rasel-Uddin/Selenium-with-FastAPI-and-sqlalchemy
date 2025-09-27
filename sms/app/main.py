from fastapi import FastAPI
from .db import engine, Base
from .routers import students, teachers, courses

app = FastAPI(title="SMS Simple API")

Base.metadata.create_all(bind=engine)

app.include_router(students.router)
app.include_router(teachers.router)
app.include_router(courses.router)

@app.get("/")
def root():
    return {"status": "ok"}
