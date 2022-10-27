import multiprocessing
import time
from models.CourseModel import Course
from models.LearningJourneyModel import LearningJourney
import pytest
import os

import subprocess
from models.UserTypeModel import UserType
from request_handler import create_app
from models.shared_model import db
from models.SkillModel import Skill
from models.RoleModel import Role
from models.StaffModel import Staff
@pytest.fixture( scope="session")
def app():
    app=create_app()  
    app.config.update({
        "TESTING": True,
    })

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

@pytest.fixture( scope="function")
def db_setup(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

    yield db


#Create data for testing

#create a fixture for creating data required to test create learning journey
@pytest.fixture( scope="function")
def create_courses(app):
    course1 = Course(id="COR001", name="TestC1",description="TestDesc",status="active",type="testType1",category="testCat1")
    course2 = Course(id="COR002", name="TestC2",description="TestDesc",status="active",type="testType2",category="testCat2")
    course3 = Course(id="COR003", name="TestC3",description="TestDesc",status="active",type="testType3",category="testCat3")
    
    with app.app_context():

        db.session.add(course1)
        db.session.add(course2)
        db.session.add(course3)
        db.session.commit()
    
    return course1,course2,course3

#create a fixture for creating lj
@pytest.fixture( scope="function")
def create_ljs(app):
    course1 = Course(id="COR001", name="TestC1",description="TestDesc",status="active",type="testType1",category="testCat1")
    course2 = Course(id="COR002", name="TestC2",description="TestDesc",status="active",type="testType2",category="testCat2")
    course3 = Course(id="COR003", name="TestC3",description="TestDesc",status="active",type="testType3",category="testCat3")
    lj1 = LearningJourney(name="TestLJ1",staff_id=1,role_id=1)
    lj1.courses=[course1]
    lj2 = LearningJourney(name="TestLJ2",staff_id=2,role_id=1)
    lj2.courses=[course2,course3]
    
    with app.app_context():
        db.session.add(lj1)
        db.session.add(lj2)
        db.session.commit()
    
    return lj1,lj2

#create a fixture for adding skills to db
@pytest.fixture( scope="function")
def create_skills(app):
    skill1 = Skill(name="TestSkill1",description="TestDesc",active=True)
    skill2 = Skill(name="TestSkill2",description="TestDesc",active=True)
    skill3 = Skill(name="TestSkill3",description="TestDesc",active=True)
    
    with app.app_context():
        db.session.add(skill1)
        db.session.add(skill2)
        db.session.add(skill3)
        db.session.commit()
    
    return skill1,skill2,skill3

#create a fixture for adding roles to db
@pytest.fixture( scope="function")
def create_roles(app):
    role1 = Role(name="TestRole1",description="TestDesc",active=True)
    role2 = Role(name="TestRole2",description="TestDesc",active=True)
    role3 = Role(name="TestRole3",description="TestDesc",active=True)

    with app.app_context():
        db.session.add(role1)
        db.session.add(role2)
        db.session.add(role3)
        db.session.commit()
    
    return role1,role2,role3

#create a fixture for adding usertype to db
@pytest.fixture( scope="function")
def create_usertype(app):
    usertype1 = UserType(type="TestType1")
    usertype2 = UserType(type="TestType2")
    usertype3 = UserType(type="TestType3")

    with app.app_context():
        db.session.add(usertype1)
        db.session.add(usertype2)
        db.session.add(usertype3)
        db.session.commit()
    
    return usertype1,usertype2,usertype3

#create a fixture for adding staff to db
@pytest.fixture( scope="function")
def create_staff(app,create_usertype):
    staff1 = Staff(first_name="TestFirstName1",last_name="TestLastName1", department="TestDepartment1",email="TestEmail1",user_type_id=1)
    staff2 = Staff(first_name="TestFirstName2",last_name="TestLastName2", department="TestDepartment2",email="TestEmail2",user_type_id=1)
    staff3 = Staff(first_name="TestFirstName3",last_name="TestLastName3", department="TestDepartment3",email="TestEmail3",user_type_id=1)

    with app.app_context():
        db.session.add(staff1)
        db.session.add(staff2)
        db.session.add(staff3)
        db.session.commit()
    
    return staff1,staff2,staff3

@pytest.fixture(scope='function')
def test_post_client():
    # Create a Flask app configured for testing
    flask_app = create_app()
    #flask_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            db.drop_all()
            db.create_all()
            yield testing_client  # this is where the testing happens!

@pytest.fixture(scope='function')
def test_get_client():
    # Create a Flask app configured for testing
    flask_app = create_app()
    #flask_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            db.drop_all()
            db.create_all()
            # Insert skill data
            skill1 = Skill(name="TestSkill1",description="TestDesc",active=True)
            skill2 = Skill(name="TestSkill2",description="TestDesc",active=True)
            skill3 = Skill(name="TestSkill3",description="TestDesc",active=True)
            db.session.add(skill1)
            db.session.add(skill2)
            db.session.add(skill3)

            # Commit the changes for the users
            db.session.commit()
            yield testing_client  # this is where the testing happens!

#sample data array:
toAddData = []

#try insert with tuple
def add_to_db(data_array, some_class):
    for each_dict in data_array:
        to_insert = some_class(each_dict)
        db.session.add(to_insert)
    db.session.commit



