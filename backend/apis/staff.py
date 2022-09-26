from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.StaffModel import Staff
from schemas.StaffSchema import StaffSchema

staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)

staff_api = Blueprint('staff_api', __name__)


