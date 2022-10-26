from models.CourseModel import Course
from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.LearningJourneyModel import LearningJourney
from schemas.LearningJourneySchema import LearningJourneySchema, LearningJourneyWithCoursesSchema, LearningJourneyWithCoursesWithSkillsSchema
from models.RoleModel import Role
from models.StaffModel import Staff
from schemas.RoleSchema import RoleSchema, RoleWithSkillsSchema
from schemas.StaffSchema import StaffSchema
from schemas.CourseSchema import CourseSchema

learning_journey_schema = LearningJourneySchema()
learning_journeys_schema = LearningJourneySchema(many=True)
lj_with_courses_schema = LearningJourneyWithCoursesSchema()
lj_with_courses_with_skills_schema = LearningJourneyWithCoursesWithSkillsSchema()

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

learning_journey_api = Blueprint('learning_journey_api', __name__)

#Get All Learning Journeys with Courses
@learning_journey_api.route('/', methods=['GET'])
def get_learning_journeys():
    all_learning_journeys = LearningJourney.query.all()
    return learning_journeys_schema.jsonify(all_learning_journeys)

#Get Single Learning Journey with Courses and it's skills
@learning_journey_api.route('/<id>', methods=['GET'])
def get_learning_journey(id):
    args = request.args
    if 'courses_not_in_lj' in args:
        lj = LearningJourney.query.get(id)
        role = Role.query.get(lj.role_id)
        courses = Course.query.all()
        courses_to_return = []
        for course in courses:
            if course not in lj.courses:
                for skill in course.skills:
                    if skill in role.skills:
                        courses_to_return.append(course)
                        break
        return courses_schema.jsonify(courses_to_return)


    learning_journey = LearningJourney.query.get(id)
    return lj_with_courses_with_skills_schema.jsonify(learning_journey)


#Create Learning Journey
@learning_journey_api.route('/create', methods=['POST'])
def create_learning_journey():
    name = request.json['name']
    staff_id = request.json['staff_id']
    role_id = request.json['role_id']
    course_ids = request.json['course_ids']

    if LearningJourney.query.filter_by(staff_id=staff_id, role_id=role_id).first():
        return jsonify({"message": "Learning Journey already exists"}),500
    
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
    course_ids = request.json['course_ids']
    for course_id in course_ids:
        course = Course.query.get(course_id)
        lj.courses.append(course)
    try:
        db.session.commit()
        return lj_with_courses_with_skills_schema.jsonify(lj), 201
    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."+str(e)
        }), 500



#delete courses added to learning journey
@learning_journey_api.route('/<lj_id>/courses/<course_id>', methods=['DELETE'])
def delete_course_for_lj(lj_id,course_id):
    lj = LearningJourney.query.get(lj_id)
    lj_courses = lj.courses
    courses_edited = []
    for course in lj_courses:
        if course.id!=course_id:
            courses_edited.append(course)
    lj.courses = courses_edited
    try:
        db.session.commit()
        return lj_with_courses_schema.jsonify(lj), 200
    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."+str(e)
        }), 500


    

#Delete Learning Journey
@learning_journey_api.route('/<id>', methods=['DELETE'])
def delete_learning_journey(id):
    learning_journey = LearningJourney.query.get(id)
    db.session.delete(learning_journey)
    db.session.commit()
    return learning_journey_schema.jsonify(learning_journey)