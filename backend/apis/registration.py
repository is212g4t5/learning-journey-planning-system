from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.RegistrationModel import Registration
from schemas.RegistrationSchema import RegistrationSchema

registration_schema = RegistrationSchema()
registrations_schema = RegistrationSchema(many=True)

registration_api = Blueprint('registration_api', __name__)
