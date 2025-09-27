# 🎓 School Management System (SMS)

A backend system built with **FastAPI + SQLAlchemy** to manage students, teachers, courses, and enrollments.  
This project demonstrates **OOP principles**, enforces business rules, and integrates scraped resources.

---

## 🚀 Features
- **Domain classes**
  - `Person` (abstract base class)
  - `Student`
  - `Teacher`
  - `Course`
  - `Enrollment`
- **CRUD Endpoints** for students, teachers, courses, enrollments.
- **Business Rules**
  - Prevent duplicate enrollment in a course.
  - Enforce course capacity.
- **Data Import**
  - Scraped resources can be imported into the database via an API endpoint.
- **Configurable Database**
  - Uses environment variables for database connection.
- **Testing**
  - Includes `pytest` tests:
    - Enrollment rules
    - API endpoints
    - Scraper parsing

---
