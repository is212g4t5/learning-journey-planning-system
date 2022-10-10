from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.CourseModel import Course
from models.SkillModel import Skill
from schemas.CourseSchema import CourseSchema, CourseWithSkillsSchema
from schemas.SkillSchema import SkillSchema

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)

course_with_skills_schema = CourseWithSkillsSchema()
courses_with_skills_schema = CourseWithSkillsSchema(many= True)

course_api = Blueprint('course_api', __name__)

#Get All Courses
@course_api.route('/', methods=['GET'])
def get_courses():
    all_courses = Course.query.all()
    return courses_schema.jsonify(all_courses)

#Get All Active Courses
@course_api.route('/active', methods=['GET'])
def get_courses_active():
    all_active_courses = Course.query.filter_by(status = 'Active')
    return courses_schema.jsonify(all_active_courses)

#Get courses with skills
@course_api.route('/skills', methods=['GET'])
def get_courses_with_skills():
    all_courses = Course.query.all()
    return courses_with_skills_schema.jsonify(all_courses)

#Get active courses with skills
@course_api.route('/active/skills', methods=['GET'])
def get_courses_with_skills_active():
    all_active_courses = Course.query.filter_by(status = 'Active')
    return courses_with_skills_schema.jsonify(all_active_courses)

#Update skills assigned for a course
@course_api.route('/<id>/skills', methods=['PUT'])
def update_skills_for_course(id):
    course = Course.query.get(id)
    skill_ids = request.json['skill_ids']
    course.skills = []
    for skill_id in skill_ids:
        skill = Skill.query.get(skill_id)
        course.skills.append(skill)
    try:
        db.session.commit()
        return course_with_skills_schema.jsonify(course), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# Get a course with skills
@course_api.route('/<id>/skills', methods=['GET'])
def get_course_with_skills(id):
    course = Course.query.get(id)
    return course_with_skills_schema.jsonify(course)
