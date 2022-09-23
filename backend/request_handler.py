#flask server
from pprint import pprint
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import Session, relationship, sessionmaker
import os

#init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                        '@localhost:3306/ljps'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#handle CORS
CORS(app)

#init db
db = SQLAlchemy(app)

#init ma
ma = Marshmallow(app)

#association table between Staff and Skill
staff_skill = db.Table('staff_skill',db.Model.metadata,
    db.Column('staff_id', db.Integer, db.ForeignKey('staff.id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True)
)

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
    skills = db.relationship('Skill', secondary=staff_skill, backref='staffs', lazy=True)

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
    active = db.Column(db.Boolean, default=True)
    learning_journeys = db.relationship('LearningJourney', backref='role', lazy=True)
    skills = db.relationship('Skill', secondary=role_skill, backref='roles', lazy=True)

    def __init__(self, name, active):
        self.name = name
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
class UserTypeSchema(ma.Schema):
    class Meta:
        model = UserType

#Staff Schema
class StaffSchema(ma.Schema):
    class Meta:
        model = Staff

#LearningJourney Schema
class LearningJourneySchema(ma.Schema):
    class Meta:
        model = LearningJourney

#Role Schema
class RoleSchema(ma.Schema):
    class Meta:
        model = Role

#Skill Schema
class SkillSchema(ma.Schema):
    class Meta:
        model = Skill

#Course Schema
class CourseSchema(ma.Schema):
    class Meta:
        model = Course

#Registration Schema
class RegistrationSchema(ma.Schema):
    class Meta:
        model = Registration

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



#Run Server
if __name__ == '__main__':
    app.run(debug=True)

# Run the server
# python main.py



