# Course Management System (Flask)

## Overview

The **Course Management System** is a Flask-based web application that demonstrates the use of **Flask-SQLAlchemy** and **Flask-Migrate** to manage a relational database using the Object Relational Mapper (ORM). The project follows a simple academic course management schema consisting of Departments, Courses, Students, and Enrollments.

This project was developed as part of a hands-on learning exercise to understand database modeling, ORM relationships, and database migrations in Flask.

---

## Features

* Flask application using the Application Factory pattern
* Flask-SQLAlchemy ORM integration
* Flask-Migrate for database migrations
* Department, Course, Student, and Enrollment models
* One-to-Many and Many-to-Many relationships
* CRUD-ready database schema
* SQLite database support
* Interactive database operations using the Flask Shell

---

## Technologies Used

* Python 3.x
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* SQLAlchemy
* SQLite
* Git & GitHub

---

## Project Structure

```text
course_management/
│
├── app.py
├── requirements.txt
├── migrations/
├── instance/
│   └── courses.db
├── courses/
│   ├── __init__.py
│   └── models.py
└── README.md
```

---

## Database Schema

### Department

* id (Primary Key)
* name

### Course

* id (Primary Key)
* title
* credits
* department_id (Foreign Key)

### Student

* id (Primary Key)
* name
* email

### Enrollment

* id (Primary Key)
* student_id (Foreign Key)
* course_id (Foreign Key)
* grade

---

## Relationships

* One Department can have many Courses.
* One Course belongs to one Department.
* One Student can have many Enrollments.
* One Course can have many Enrollments.
* Enrollment acts as the junction table between Students and Courses.

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd course_management
```

### Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
flask run
```

The application will start on:

```text
http://127.0.0.1:5000/
```

---

## Database Migration

Initialize migrations:

```bash
flask db init
```

Create a migration:

```bash
flask db migrate -m "Initial schema"
```

Apply the migration:

```bash
flask db upgrade
```

---

## Using Flask Shell

Start the Flask shell:

```bash
flask shell
```

Example:

```python
from app import db
from courses.models import Department, Course

dept = Department(name="Computer Science")
db.session.add(dept)
db.session.commit()
```

---

## Learning Outcomes

This project demonstrates:

* Flask application setup
* SQLAlchemy ORM models
* Database relationships
* Database migrations using Flask-Migrate
* CRUD operations using the ORM
* Flask Shell usage
* Git and GitHub project management

---

## Future Enhancements

* User authentication and authorization
* REST API using Flask
* Course registration interface
* Student dashboard
* Search and filtering
* Admin panel
* Unit testing
* Docker deployment

---

## Author

**Pooja G**

BE Computer Science Engineering (Artificial Intelligence & Machine Learning)

Rajalakshmi Institute of Technology

---

## License

This project is created for educational purposes.
