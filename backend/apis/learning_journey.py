from models.CourseModel import Course
from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.LearningJourneyModel import LearningJourney
from schemas.LearningJourneySchema import LearningJourneySchema, LearningJourneyWithCoursesSchema

learning_journey_schema = LearningJourneySchema()
learning_journeys_schema = LearningJourneySchema(many=True)

lj_with_skills_schema = LearningJourneyWithCoursesSchema()

learning_journey_api = Blueprint('learning_journey_api', __name__)


#Update courses added to learning journey
@learning_journey_api.route('/<id>/courses', methods=['PUT'])
def update_course_for_lj(id):
    lj = LearningJourney.query.get(id)
    course_ids = request.json['course_ids']
    lj.courses = []
    for course_id in course_ids:
        course = Course.query.get(course_id)
        lj.courses.append(course)
    try:
        db.session.commit()
        return lj_with_skills_schema.jsonify(lj), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500



