from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.UserTypeModel import UserType
from schemas.UserTypeSchema import UserTypeSchema

user_type_schema = UserTypeSchema()
user_types_schema = UserTypeSchema(many=True)

user_type_api = Blueprint('user_type_api', __name__)
