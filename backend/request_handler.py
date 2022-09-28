#flask server
from pprint import pprint
from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
load_dotenv(".env")

#create database
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

#get db and ma
from models.shared_model import db
from schemas.shared_schema import ma

#Init Class/Model here because Schemas are dependent on it
from models.LearningJourneyModel import LearningJourney
from models.RoleModel import Role
from models.SkillModel import Skill
from models.UserTypeModel import UserType
from models.StaffModel import Staff
from models.CourseModel import Course
from models.RegistrationModel import Registration

#import all API route/blueprint
from apis.role import role_api
from apis.skill import skill_api
from apis.learning_journey import learning_journey_api
from apis.user_type import user_type_api
from apis.staff import staff_api
from apis.course import course_api
from apis.registration import registration_api

#Create app function
def create_app():


    # Get database address.
    db_addr = "localhost"
    # Get username of the database.
    db_user = "root"
    # Get password.
    PASS = os.getenv("DB_PASSWORD") 
    if not PASS:
        PASS = ""
    db_pass = PASS
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
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #handle CORS
    CORS(app)

    #Create Tables
    with app.app_context():
        db.init_app(app)
        db.create_all()

        ma.init_app(app)

    #Register API route/blueprint
    app.register_blueprint(role_api, url_prefix='/api/roles')
    app.register_blueprint(skill_api, url_prefix='/api/skills')
    app.register_blueprint(learning_journey_api, url_prefix='/api/learning_journeys')
    app.register_blueprint(user_type_api, url_prefix='/api/user_types')
    app.register_blueprint(staff_api, url_prefix='/api/staffs')
    app.register_blueprint(course_api, url_prefix='/api/courses')
    app.register_blueprint(registration_api, url_prefix='/api/registrations')

    return app

#Run Server
if __name__ == '__main__':
    create_app().run(debug=True)

# Run the server
# python main.py



