from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.CourseModel import Course
from schemas.CourseSchema import CourseSchema

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

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


