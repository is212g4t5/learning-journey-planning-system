from flask import Blueprint, jsonify, request
from models.shared_model import db
from models.RoleModel import Role
from models.SkillModel import Skill
from schemas.RoleSchema import RoleSchema, RoleWithSkillsSchema
from schemas.SkillSchema import SkillSchema


role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)

role_with_skills_schema = RoleWithSkillsSchema()
roles_with_skills_schema = RoleWithSkillsSchema(many= True)


role_api = Blueprint('role_api', __name__)
#Create a Role
@role_api.route('/', methods=['POST'])
def add_role():
    name = request.json['name']
    description = request.json['description']
    active = request.json['active']

    new_role = Role(name, description, active)

    db.session.add(new_role)
    db.session.commit()

    return role_schema.jsonify(new_role),201

#Get All Roles
@role_api.route('/', methods=['GET'])
def get_roles():
    all_roles = Role.query.all()
    return roles_schema.jsonify(all_roles)

#Get Single Role
@role_api.route('/<id>', methods=['GET'])
def get_role(id):
    role = Role.query.get(id)
    return role_schema.jsonify(role)

#Update a Role
@role_api.route('/<id>', methods=['PUT'])
def update_role(id):
    role = Role.query.get(id)

    name = request.json['name']
    description = request.json['description']
    active = request.json['active']

    role.name = name
    role.description = description
    role.active = active

    db.session.commit()

    return role_schema.jsonify(role)

#Soft Delete Role
@role_api.route('/<id>', methods=['DELETE'])
def delete_role(id):
    role = Role.query.get(id)
    role.active = False
    db.session.commit()

    return role_schema.jsonify(role)

#Get roles with skills
@role_api.route('/skills', methods=['GET'])
def get_roles_with_skills():
    all_roles = Role.query.all()
    return roles_with_skills_schema.jsonify(all_roles)


#Update skills assigned for a role
@role_api.route('/<id>/skills', methods=['PUT'])
def update_skills_for_role(id):
    role = Role.query.get(id)
    skill_ids = request.json['skill_ids']
    role.skills = []
    for skill_id in skill_ids:
        skill = Skill.query.get(skill_id)
        role.skills.append(skill)
   
    db.session.commit()
    return role_with_skills_schema.jsonify(role)
 


#Get a role with skills
@role_api.route('/<id>/skills', methods=['GET'])
def get_role_with_skills(id):
    role = Role.query.get(id)
    return role_with_skills_schema.jsonify(role)