# 🏗️ System Design – School Management System (SMS)

This document explains the **OOP principles** demonstrated in the project and how they are applied.

---

## 1️⃣ Abstraction
- `Person` is defined as an **abstract base class**.
- It provides common attributes (`id`, `name`, `email`) for all people in the system.
- Concrete classes (`Student`, `Teacher`) extend `Person` but `Person` itself cannot be instantiated.
- This hides unnecessary details and exposes only the **essential interface**.

---

## 2️⃣ Encapsulation
- Each class controls access to its data:
  - `Course.capacity` and `Enrollment` checks are wrapped in methods instead of being directly modified.
  - Enrollment logic (`enroll_student`) enforces business rules internally, ensuring data integrity.
- Encapsulation ensures state changes are safe and predictable.

---

## 3️⃣ Inheritance
- `Student` and `Teacher` inherit from `Person`, reusing shared fields and behaviors.
- Example hierarchy:
- Person (abstract)
--- Student
--- Teacher

- Promotes **code reuse** and reduces duplication.

---

## 4️⃣ Polymorphism
- Common methods behave differently based on the object:
- `__repr__()` shows different string representations for Student vs Teacher.
- `get_role()` can return `"student"` or `"teacher"` depending on the subclass.
- FastAPI + Pydantic also demonstrate **response polymorphism** in how models are serialized.

---

## 📐 Business Rules
1. **Prevent duplicate enrollment**  
 - Before inserting into `Enrollment`, check if `(student_id, course_id)` already exists.
2. **Enforce course capacity**  
 - If the number of enrollments ≥ `course.capacity`, reject the new enrollment.

---

## 🔄 Data Flow
1. **Scraper** gathers external resources.  
2. **Import endpoint** (`/resources/import`) saves scraped data into the `scraped_resources` table.  
3. **CRUD APIs** provide access to students, teachers, courses, and enrollments.  
4. **Business logic** applies constraints before saving to DB.  

---

## 🧪 Testing
- `test_enrollment.py` → checks duplicate & capacity rules.  
- `test_api.py` → validates CRUD endpoints.  
- `test_scraper.py` → ensures scraped data is parsed and imported correctly.  

---

## 🐳 Deployment & Extras
- **Alembic migrations** ensure DB schema consistency.  
- **Dockerfile** supports containerized deployment.  
- Environment variables (`DATABASE_URL`) keep config secure and flexible.  

---
