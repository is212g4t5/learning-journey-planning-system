from telnetlib import STATUS
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

# @course_api.route('/', methods=['GET'])
# def get_courses():
#     all_courses = Course.query.all()
#     try:
#         return courses_schema.dump(all_courses),200
#     except Exception as e:
#         return jsonify({
#             "message": "Unable to retrieve data. "+str(e)
#         }), 500



