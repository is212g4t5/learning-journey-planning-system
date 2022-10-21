from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.LearningJourneyModel import LearningJourney
from models.RoleModel import Role
from models.StaffModel import Staff

from schemas.LearningJourneySchema import LearningJourneySchema
from schemas.RoleSchema import RoleSchema, RoleWithSkillsSchema
from schemas.StaffSchema import StaffSchema

learning_journey_schema = LearningJourneySchema()
learning_journeys_schema = LearningJourneySchema(many=True)

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)

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
    # if not learning_journey:
    #     return jsonify({"message": "Learning Journey not found"}), 404
    return role_schema.jsonify(learning_journey)

#Create Learning Journey
@learning_journey_api.route('/create', methods=['PUT'])
def create_learning_journey():
    name = request.json['name']
    staff_id = request.json['staff_id']
    role_id = request.json['role_id']

    new_learning_journey = LearningJourney(name, staff_id, role_id)

    db.session.add(new_learning_journey)
    db.session.commit()

    return learning_journey_schema.jsonify(new_learning_journey),201
