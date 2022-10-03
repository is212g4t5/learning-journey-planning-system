import multiprocessing
import time
import pytest
import os

import subprocess
from request_handler import create_app
from models.shared_model import db
from models.SkillModel import Skill
@pytest.fixture(autouse=True, scope="session")
def app():
    app=create_app()

    

    yield app

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


# @pytest.fixture(autouse=True, scope="session")
# def start_server(app):
    
#     # app.run()
#     # other setup can go here
#     p = multiprocessing.Process(target=create_app().run)
#     p.start()
#     print("setup")
#     yield app
#     print("teardown")
#     p.terminate()

# @pytest.fixture()
# def client(app):
#     return app.test_client()


# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()
