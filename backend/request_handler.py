#flask server
from pprint import pprint
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


# Get database address.
db_addr = "localhost"
# Get username of the database.
db_user = "root"
# Get password.
db_pass = ""
# Get the database name.
db_name = "ljps"
# join the inputs into a complete database url.
db_url = f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_addr}/{db_name}"

# Create an engine object.
engine = create_engine(db_url, echo=True)

# Create database if it does not exist.
if not database_exists(engine.url):
    create_database(engine.url)
    print("Database created.")


#init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#handle CORS
CORS(app)

#init db
db = SQLAlchemy(app)

#init ma
ma = Marshmallow(app)


#association table between Role and Skill
role_skill = db.Table('role_skill',db.Model.metadata,
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True)
)

#association table between Course and Skill
course_skill = db.Table('course_skill',db.Model.metadata,
    db.Column('course_id', db.String(20), db.ForeignKey('course.id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True)
)

#association table between LearningJourney and Courses
lj_course = db.Table('lj_course',db.Model.metadata,
    db.Column('lj_id', db.Integer, db.ForeignKey('learning_journey.id'), primary_key=True),
    db.Column('course_id', db.String(20), db.ForeignKey('course.id'), primary_key=True)
)

#UserType Class/Model
class UserType(db.Model):
    __tablename__ = 'user_type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), unique=True, nullable=False)
    Staffs = db.relationship('Staff', backref='user_type', lazy=True)

    def __init__(self, type):
        self.type = type

        
#Staff Class/Model
class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.id'), nullable=False)
    learning_journeys = db.relationship('LearningJourney', backref='staff', lazy=True)
 
    def __init__(self, first_name, last_name, department, email, user_type_id):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email
        self.user_type_id = user_type_id


#LearningJourney Class/Model
class LearningJourney(db.Model):
    __tablename__ = 'learning_journey'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    courses = db.relationship('Course', secondary=lj_course, backref='learning_journeys', lazy=True)

    def __init__(self, name, staff_id, role_id):
        self.name = name
        self.staff_id = staff_id
        self.role_id = role_id



#Role Class/Model
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=True, nullable=False)
    description = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)
    learning_journeys = db.relationship('LearningJourney', backref='role', lazy=True)
    skills = db.relationship('Skill', secondary=role_skill, backref='roles', lazy=True)

    def __init__(self, name, description, active):
        self.name = name
        self.description = description
        self.active = active



#Skill Class/Model
class Skill(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)

    def __init__(self, name, description,active):
        self.name = name
        self.description = description
        self.active = active
      
    
#Course Class/Model
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(50),unique=True, nullable=False)
    description = db.Column(db.String(255))
    status = db.Column(db.String(15), default = 'Active')
    type = db.Column(db.String(10))
    category = db.Column(db.String(50))

    active = db.Column(db.Boolean, default=True)
    skills = db.relationship('Skill', secondary=course_skill, backref='courses', lazy=True)

    def __init__(self, id, name, description, status, type, category, active):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.type = type
        self.category = category
        self.active = active



#Registration Class/Model
class Registration(db.Model):
    __tablename__ = 'registration'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(20), db.ForeignKey('course.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    reg_status = db.Column(db.String(20), default = 'Waitlist', nullable=False)
    completion_status = db.Column(db.String(20), default = 'Not Started', nullable=False)

    def __init__(self, course_id, staff_id, reg_status, completion_status):
        self.course_id = course_id
        self.staff_id = staff_id
        self.reg_status = reg_status
        self.completion_status = completion_status


#UserType Schema
class UserTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserType
        include_fk= True

#Staff Schema
class StaffSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Staff
        include_fk =True

#LearningJourney Schema
class LearningJourneySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LearningJourney
        include_fk =True

#Role Schema
class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_fk =True

#Skill Schema
class SkillSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Skill
        include_fk =True

#Course Schema
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        include_fk =True

#Registration Schema
class RegistrationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Registration
        include_fk =True

#Init Schema
user_type_schema = UserTypeSchema()
user_types_schema = UserTypeSchema(many=True)

staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)

learning_journey_schema = LearningJourneySchema()
learning_journeys_schema = LearningJourneySchema(many=True)

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

registration_schema = RegistrationSchema()
registrations_schema = RegistrationSchema(many=True)

#Create Tables
db.create_all()

#Create a skill
@app.route('/skill', methods=['POST'])
def add_skill():
    name = request.json['name']
    desc = request.json['description']
    active = request.json['active']

    new_skill = Skill(name, desc,active)

    try:
        db.session.add(new_skill)
        db.session.commit()
        return skill_schema.jsonify(new_skill),201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

#Get All Skills
@app.route('/skill', methods=['GET'])
def get_skills():
    all_skills = Skill.query.all()
    return skills_schema.dump(all_skills),200

#Create a Role
@app.route('/role', methods=['POST'])
def add_role():
    name = request.json['name']
    description = request.json['description']
    active = request.json['active']

    new_role = Role(name, description, active)

    db.session.add(new_role)
    db.session.commit()

    return role_schema.jsonify(new_role)

#Get All Roles
@app.route('/role', methods=['GET'])
def get_roles():
    all_roles = Role.query.all()
    return roles_schema.jsonify(all_roles)

#Get Single Role
@app.route('/role/<id>', methods=['GET'])
def get_role(id):
    role = Role.query.get(id)
    return role_schema.jsonify(role)

#Update a Role
@app.route('/role/<id>', methods=['PUT'])
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
@app.route('/role/<id>', methods=['DELETE'])
def delete_role(id):
    role = Role.query.get(id)
    role.active = False
    db.session.commit()

    return role_schema.jsonify(role)

#Add skills to a role
@app.route('/role/<id>/skill', methods=['POST'])
def add_skills_to_role(id):
    role = Role.query.get(id)
    skill_ids = request.json['skill_ids']
    for skill_id in skill_ids:
        skill = Skill.query.get(skill_id)
        role.skills.append(skill)
    db.session.commit()
    return role_schema.jsonify(role)

# #Get skills by role
@app.route('/role/<id>/skill', methods=['GET'])
def get_skills_by_role(id):
    role = Role.query.get(id)
    skills = role.skills
    return skills_schema.jsonify(skills)


#Run Server
if __name__ == '__main__':
    app.run(debug=True)

# Run the server
# python main.py



