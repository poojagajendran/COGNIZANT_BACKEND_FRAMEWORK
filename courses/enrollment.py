class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )

    grade = db.Column(db.String(2))

    # Many Enrollments -> One Student
    student = db.relationship(
        "Student",
        back_populates="enrollments"
    )

    # Many Enrollments -> One Course
    course = db.relationship(
        "Course",
        back_populates="enrollments"
    )