import pytest
from models.LearningJourneyModel import LearningJourney
from tests.util import get_all_testing, post_testing


class TestLJ:
    @pytest.fixture(autouse=True, scope="function")
    def add_lj_reqs(self,db_setup,app,create_roles,create_skills, create_staff):
        self.url="/api/learning_journeys/"
        self.db = db_setup
        self.app = app

    def test_post_LJ(self,client,create_courses):
        test_data={
            "name":"NewLJ",
            "staff_id":3,
            "role_id":2,
            "course_ids":["COR001","COR003"]
        }
        post_testing(client,self.url+"create",test_data,"name","NewLJ")

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



    
    