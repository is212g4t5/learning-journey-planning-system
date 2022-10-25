from models.CourseModel import Course
from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.LearningJourneyModel import LearningJourney
from schemas.LearningJourneySchema import LearningJourneySchema, LearningJourneyWithCoursesSchema
from models.RoleModel import Role
from models.StaffModel import Staff
from schemas.RoleSchema import RoleSchema, RoleWithSkillsSchema
from schemas.StaffSchema import StaffSchema
from schemas.CourseSchema import CourseSchema

learning_journey_schema = LearningJourneySchema()
learning_journeys_schema = LearningJourneySchema(many=True)

lj_with_courses_schema = LearningJourneyWithCoursesSchema()
role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

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
    return learning_journey_schema.jsonify(learning_journey)

#Create Learning Journey
@learning_journey_api.route('/create', methods=['POST'])
def create_learning_journey():
    name = request.json['name']
    staff_id = request.json['staff_id']
    role_id = request.json['role_id']
    course_ids = request.json['course_ids']
  
    new_learning_journey = LearningJourney(name, staff_id, role_id)
    for course_id in course_ids:
        course = Course.query.get(course_id)
        new_learning_journey.courses.append(course)
        
    db.session.add(new_learning_journey)
    try:
        db.session.commit()
        return lj_with_courses_schema.jsonify(new_learning_journey),201
    except Exception as e:
        return jsonify({"message":"unable to commit to database"+str(e)
        }),500

#Update courses added to learning journey
@learning_journey_api.route('/<id>', methods=['PUT'])
def update_course_for_lj(id):
    lj = LearningJourney.query.get(id)
    print(lj)
    course_ids = request.json['course_id']
    lj.courses = []
    for course_id in course_ids:
        course = Course.query.get(course_id)
        lj.courses.append(course)
    try:
        db.session.commit()
        return lj_with_courses_schema.jsonify(lj), 201
    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."+str(e)
        }), 500


    
