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
    data = request.json
    name = data['name']
    description = data['description']
    active = data['active']

    # if (Skill.query.filter_by(name=name).first()):
    #     return jsonify(
    #         {"message": "Skill already exists."}
    #     ), 400

    new_skill = Skill(name, description, active)


    db.session.add(new_skill)
    db.session.commit()
    return skill_schema.jsonify(new_skill),201

#Update Skill
@skill_api.route('/<id>', methods=['PUT'])
def update_skill(id):
    skill = Skill.query.get(id)
    
    data = request.json
    name = data['name']
    description = data['description']
    active = data['active']

    skill.name = name
    skill.description = description
    skill.active = active
    db.session.commit()
    return skill_schema.jsonify(skill),200


#Delete Skill
@skill_api.route('/<id>', methods=['DELETE'])
def remove_skill(id):
    skill = Skill.query.get(id)
    skill.active = False
    db.session.commit()

    return skill_schema.jsonify(skill),200
    

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