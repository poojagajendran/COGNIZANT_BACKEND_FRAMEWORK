class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=False
    )

    # Many Courses -> One Department
    department = db.relationship(
        "Department",
        back_populates="courses"
    )

    # One Course -> Many Enrollments
    enrollments = db.relationship(
        "Enrollment",
        back_populates="course",
        lazy=True
    )
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "credits": self.credits,
            "department_id": self.department_id
        }
    
