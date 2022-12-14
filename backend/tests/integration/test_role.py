from models.SkillModel import Skill
from models.RoleModel import Role
from util import post_testing, get_all_testing, get_id_testing
import pytest


#create a class fixture for testing roles api
class TestRole:

    role1=role2=role3=None
    #add fixture to add roles to db
    @pytest.fixture(autouse=True, scope="function")
    def add_roles(self,db_setup,app,create_roles):
        self.url="/api/roles/"
        self.db = db_setup
        self.app = app
        
    #test create role and invalide create role
    def test_create_role(self,client):
        post_data={
            "name": "TestRoleX",
            "description": "TestDescX",
            "active": True
            } 
        #post testing test for both valid and duplicate data
        post_testing(client,self.url,post_data,"name",post_data["name"])


    #test get all roles
    def test_get_all_roles(self,client):
        get_all_testing(client,self.url,3)

        
    #test get role by id
    def test_get_role_by_id(self,client):
        response = client.get(self.url+"1")
        assert response.status_code==200
        
        res = response.json

        with self.app.app_context():
            role = Role.query.get(1)
            assert res["id"] == role.id
            assert res["name"] == role.name
            assert res["description"] == role.description
            assert res["active"] == role.active

    #test get role by invalid id
    def test_get_role_by_invalid_id(self,client):
        response = client.get(self.url+"100")
        assert response.status_code==404
    
    
    #test update role by id
    def test_update_role_by_id(self,client):
        put_data={
            "name": "TestUpdatedRole1",
            "description": "TestUpdatedDesc",
            "active": False
            } 
        response = client.put(self.url+"1",json=put_data)
        assert response.status_code==200
        
        with self.app.app_context():
            role = Role.query.get(1)
            assert role.name == put_data["name"]
            assert role.description == put_data["description"]
            assert role.active == put_data["active"]

    #test update role by invalid id
    def test_update_role_by_invalid_id(self,client):
        put_data={
            "name": "TestUpdatedRole1",
            "description": "TestUpdatedDesc",
            "active": False
            } 
        response = client.put(self.url+"100",json=put_data)
        assert response.status_code==404

    #test delete role by id
    def test_delete_role_by_id(self,client):
        response = client.delete(self.url+"1")
        assert response.status_code==200
        
        with self.app.app_context():
            role = Role.query.get(1)
            assert role.active == False

    #test delete role by invalid id
    def test_delete_role_by_invalid_id(self,client):
        response = client.delete(self.url+"100")
        assert response.status_code==404

    #test assign skills to role
    def test_assign_skills_to_role(self,client, create_skills):

        put_data={
            "skill_ids": [1,2,3]
            } 
        response = client.put(self.url+"1/skills",json=put_data)
        assert response.status_code==200
        
        with self.app.app_context():
            role = Role.query.get(1)
            assert len(role.skills) == len(put_data["skill_ids"])
            for skill in role.skills:
                assert skill.id in put_data["skill_ids"]
    
    #test assign skills to role with invalid role id
    def test_assign_skills_to_role_with_invalid_role_id(self,client, create_skills):
            put_data={
                "skill_ids": [1,2,3]
                } 
            response = client.put(self.url+"100/skills",json=put_data)
            assert response.status_code==404

    #test assign skills to role with invalid skill id
    def test_assign_skills_to_role_with_invalid_skill_id(self,client, create_skills):
            put_data={
                "skill_ids": [1,2,100]
                } 
            response = client.put(self.url+"1/skills",json=put_data)
            assert response.status_code==404

    #test get role with skills
    def test_get_role_with_skills(self,client, create_skills):

        skill1,skill2,skill3 = create_skills

        #add skills to role
        with self.app.app_context():
            role1 = Role.query.get(1)
            role1.skills.append(skill1)
            role1.skills.append(skill2)
            role1.skills.append(skill3)
            self.db.session.commit()
        
            response = client.get(self.url+"1/skills")
            assert response.status_code==200,"response is "+str(response.status_code)
            
            res = response.json
            assert res["id"] == role1.id
            assert res["name"] == role1.name
            assert res["description"] == role1.description
            assert res["active"] == role1.active
            assert len(res["skills"]) == len(role1.skills), res
            for skill in res["skills"]:
                assert skill["id"] in [skill.id for skill in role1.skills]
                assert skill["name"] in [skill.name for skill in role1.skills]
                assert skill["description"] in [skill.description for skill in role1.skills]
                assert skill["active"] in [skill.active for skill in role1.skills]

    #test get role with skills with invalid role id
    def test_get_role_with_skills_with_invalid_role_id(self,client, create_skills):
        response = client.get(self.url+"100/skills")
        assert response.status_code==404

        