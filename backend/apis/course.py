from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.CourseModel import Course
from schemas.CourseSchema import CourseSchema

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

course_api = Blueprint('course_api', __name__)




