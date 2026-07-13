from flask import jsonify
from courses.models import Course

@app.route("/api/courses/", methods=["GET"])
def get_courses():
    courses = db.session.execute(db.select(Course)).scalars().all()

    result = [course.to_dict() for course in courses]

    return jsonify(result), 200
