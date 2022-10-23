from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.LearningJourneyModel import LearningJourney
from models.RoleModel import Role
from models.SkillModel import Skill
from models.CourseModel import Course

from schemas.LearningJourneySchema import LearningJourneySchema, LearningJourneyWithCoursesSchema
from schemas.RoleSchema import RoleSchema
from schemas.StaffSchema import StaffSchema
from schemas.CourseSchema import CourseSchema

learning_journey_schema = LearningJourneySchema()
learning_journeys_schema = LearningJourneySchema(many=True)

learning_journey_with_courses_schema = LearningJourneyWithCoursesSchema
learning_journeys_with_courses_schema = LearningJourneyWithCoursesSchema(many=True)

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)

learning_journey_api = Blueprint('learning_journey_api', __name__)

#Get All Learning Journeys
@learning_journey_api.route('/', methods=['GET'])
def get_learning_journeys():
    all_learning_journeys = LearningJourney.query.all()
    return learning_journeys_schema.jsonify(all_learning_journeys)

#Get Single Learning Journey
@learning_journey_api.route('/<id>', methods=['GET'])
def get_learning_journey(id):
    learning_journey = LearningJourney.query.get(id)
    # if not learning_journey:
    #     return jsonify({"message": "Learning Journey not found"}), 404
    return role_schema.jsonify(learning_journey)

#Create Learning Journey
@learning_journey_api.route('/create', methods=['PUT'])
def create_learning_journey():
    name = request.json['name']
    staff_id = request.json['staff_id']
    role_id = request.json['role_id']

    new_learning_journey = LearningJourney(name, staff_id, role_id)

    db.session.add(new_learning_journey)
    db.session.commit()

    return learning_journey_schema.jsonify(new_learning_journey),201

#Add Course to Learning Journey
@learning_journey_api.route('/<id>/add', methods=['PUT'])
def add_course_to_learning_journey(id):
    learning_journey = LearningJourney.query.get(id)
    course_ids = request.json['course_ids']
    learning_journey.courses = []
    for course_id in course_ids: 
        course = Course.query.get(course_id)
        learning_journey.courses.append(course)
    try:
        db.session.commit()
        return learning_journey_with_courses_schema.jsonify(learning_journey), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


    