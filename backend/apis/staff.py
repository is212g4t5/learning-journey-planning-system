from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.StaffModel import Staff
from schemas.StaffSchema import StaffSchema

staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)

staff_api = Blueprint('staff_api', __name__)


#check if login detail is correct
@staff_api.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    staff = Staff.query.filter_by(email=email).first()
    if staff:
        return jsonify(staff_schema.dump(staff))
    return jsonify({"msg": "Invalid login details"}), 401