import multiprocessing
import time
import pytest
import os

import subprocess
from request_handler import create_app
@pytest.fixture(autouse=True, scope="session")
def app():
    app=create_app()

    

    yield app


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
