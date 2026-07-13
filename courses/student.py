class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)

    # One Student -> Many Enrollments
    enrollments = db.relationship(
        "Enrollment",
        back_populates="student",
        lazy=True
    )