from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.SkillModel import Skill
from schemas.SkillSchema import SkillSchema



skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)

skill_api = Blueprint('skill_api', __name__)

#Create a Skill
@skill_api.route('/', methods=['POST'])
def add_skill():

    name = request.json['name']
    description = request.json['description']
    active = request.json['active']

    new_skill = Skill(name, description, active)

    db.session.add(new_skill)
    db.session.commit()

    try:
        db.session.add(new_skill)
        db.session.commit()
        return skill_schema.jsonify(new_skill),201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

#Get All Skills
@skill_api.route('/', methods=['GET'])
def get_skills():
    all_skills = Skill.query.all()
    try:
        return skills_schema.dump(all_skills),200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500