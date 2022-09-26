from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.LearningJourneyModel import LearningJourney
from schemas.LearningJourneySchema import LearningJourneySchema

learning_journey_schema = LearningJourneySchema()
learning_journeys_schema = LearningJourneySchema(many=True)

learning_journey_api = Blueprint('learning_journey_api', __name__)



