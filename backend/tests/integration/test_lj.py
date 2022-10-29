import pytest
import json
from models.LearningJourneyModel import LearningJourney
from tests.util import get_all_testing, post_testing, put_testing
from models.SkillModel import Skill
from models.RoleModel import Role
from models.CourseModel import Course


class TestLJ:
    @pytest.fixture(autouse=True, scope="function")
    def add_lj_reqs(self,db_setup,app,create_roles,create_skills, create_staff):
        self.url="/api/learning_journeys/"
        self.db = db_setup
        self.app = app

    #test create LJ and invalid create LJ (duplicate name)
    def test_post_LJ(self,client,create_courses):
        test_data={
            "name":"NewLJ",
            "staff_id":3,
            "role_id":2,
            "course_ids":["COR001","COR003"]
        }
        post_testing(client,self.url+"create",test_data,"name","NewLJ")

    def test_post_courses(self,client,create_ljs):
        test_data={
            "course_ids":["COR002","COR003"]
        }
        put_testing(client,self.url+"1",test_data,"course_ids","courses")

    def test_remove_course(self,client,create_ljs):
        response = client.delete(self.url+"2/courses/COR002") 
        assert response.status_code==308
        assert 0==1, "response is "+str(response.data)
        res = json.loads(response.data.decode('utf-8'))
        courses = res["courses"]
        for course in courses:
            assert course.id != "COR002", "course ID is "+str(course.id)


    #test get all LJ
    def test_get_all_LJ(self,client, create_ljs):
        get_all_testing(client,self.url,2)

    #test get LJ by id
    def test_get_LJ_by_id(self,client, create_ljs):
        response = client.get(self.url+"2")
        assert response.status_code==200
        
        res = response.json

        with self.app.app_context():
            lj = LearningJourney.query.get(2)
            assert res["staff_id"] == lj.staff_id
            assert res["name"] == lj.name
            assert res["role_id"] == lj.role_id
            assert len(res["courses"]) == 2


    #test view courses in LJ that has yet to be added to LJ
    def test_get_eligible_courses_not_in_LJ(self,client, create_ljs):
        
        with self.app.app_context():
            #assign skills to courses
            course1 = Course.query.get("COR001")
            course2 = Course.query.get("COR002")
            course3 = Course.query.get("COR003")
            course1.skills = [Skill.query.get(1),Skill.query.get(2),Skill.query.get(3)]
            course2.skills = [Skill.query.get(1),Skill.query.get(2),Skill.query.get(3)]
            course3.skills = [Skill.query.get(1),Skill.query.get(2),Skill.query.get(3)]

            #assign skills to role
            role = Role.query.get(1)
            role.skills = [Skill.query.get(1),Skill.query.get(2),Skill.query.get(3)]

            #assign role to lj
            lj = LearningJourney.query.get(1)
            lj.role = role
            
            #assign courses to lj
            lj.courses = [course1,course2]

            self.db.session.commit()

            #test get eligible courses
            response = client.get(self.url+"1?courses_not_in_lj=true")
            assert response.status_code==200
            res = response.json
            assert len(res) == 1
            assert res[0]["id"] == "COR003"



            
    #test delete LJ
    def test_delete_LJ(self,client, create_ljs):
        response = client.delete(self.url+"2")
        assert response.status_code==200
        res = response.json
        assert res["message"] == "Learning Journey deleted"

        with self.app.app_context():
            lj = LearningJourney.query.get(2)
            assert lj == None

    #test delete LJ that does not exist
    def test_delete_LJ_not_exist(self,client, create_ljs):
        response = client.delete(self.url+"4")
        assert response.status_code==404
        res = response.json
        assert res["message"] == "Learning Journey does not exist"
        




    
    