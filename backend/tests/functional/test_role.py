from models.RoleModel import Role
from schemas.RoleSchema import RoleSchema
from util import post_testing, get_all_testing, get_id_testing
import pytest


#create a class fixture for testing roles api
class TestRole:

    #add fixture to add roles to db
    @pytest.fixture(autouse=True, scope="function")
    def add_roles(self,db_setup,app):
        self.url="/api/roles/"
        db = db_setup
        self.app = app
        
        self.role1 = Role(name="TestRole1",description="TestDesc",active=True)
        self.role2 = Role(name="TestRole2",description="TestDesc",active=True)
        self.role3 = Role(name="TestRole3",description="TestDesc",active=True)

        with app.app_context():
            db.session.add(self.role1)
            db.session.add(self.role2)
            db.session.add(self.role3)
            db.session.commit()

    #test get all roles
    def test_get_all_roles(self,client):
        get_all_testing(client,self.url,3)
        # response = client.get(url)
        # assert response.status_code == 200
        # assert len(response.json) == 4

        
    #test get role by id
    def test_get_role_by_id(self,client):
        # get_id_testing(client,self.url+"1","name","TestRole1")
        response = client.get(self.url+"1")
        assert response.status_code==200,"response is "+str(response.status_code)
        res = response.json
        assert res["name"] == "TestRole1"
        assert res["description"] == "TestDesc"
        assert res["active"] == True

    

    
    

    