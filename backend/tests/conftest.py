import multiprocessing
import time
import pytest
import os

import subprocess
from request_handler import create_app
from models.shared_model import db
from models.SkillModel import Skill
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



