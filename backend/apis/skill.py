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
    try:
        data = request.json
        name = data['name']
        description = data['description']
        active = data['active']
    except Exception as json_error:
        return jsonify({
            "message": "Unable to commit to database. "+str(json_error)
        }), 400

    if (Skill.query.filter_by(name=name).first()):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "name": name
                },
                "message": "Skill already exists."
            }
        ), 400

    new_skill = Skill(name, description, active)

    try:
        db.session.add(new_skill)
        db.session.commit()
        return skill_schema.jsonify(new_skill),201
    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database. "+str(e)
        }), 500

#Get All Skills
@skill_api.route('/', methods=['GET'])
def get_skills():
    all_skills = Skill.query.all()
    try:
        return skills_schema.dump(all_skills),200
    except Exception as e:
        return jsonify({
            "message": "Unable to retrieve data. "+str(e)
        }), 500