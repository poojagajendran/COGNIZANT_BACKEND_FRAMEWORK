from app import db

class Department(db.Model):
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # One Department -> Many Courses
    courses = db.relationship(
        "Course",
        back_populates="department",
        lazy=True
    )