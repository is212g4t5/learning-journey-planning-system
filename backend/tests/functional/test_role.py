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
        self.db = db_setup
        self.app = app
        
        self.role1 = Role(name="TestRole1",description="TestDesc",active=True)
        self.role2 = Role(name="TestRole2",description="TestDesc",active=True)
        self.role3 = Role(name="TestRole3",description="TestDesc",active=True)

        with app.app_context():
            self.db.session.add(self.role1)
            self.db.session.add(self.role2)
            self.db.session.add(self.role3)
            self.db.session.commit()

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

    
    
    #test update role by id
    def test_update_role_by_id(self,client):
        put_data={
            "name": "TestUpdatedRole1",
            "description": "TestUpdatedDesc",
            "active": False
            } 
        response = client.put(self.url+"1",json=put_data)
        assert response.status_code==200,"response is "+str(response.status_code)
        
        with self.app.app_context():
            role = Role.query.get(1)
            assert role.name == put_data["name"]
            assert role.description == put_data["description"]
            assert role.active == put_data["active"]

    #test delete role by id
    def test_delete_role_by_id(self,client):
        response = client.delete(self.url+"1")
        assert response.status_code==200,"response is "+str(response.status_code)
        with self.app.app_context():
            role = Role.query.get(1)
            assert role.active == False