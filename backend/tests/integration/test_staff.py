from models.StaffModel import Staff
from util import post_testing, get_all_testing, get_id_testing
import pytest


#create a class fixture for testing roles api
class TestStaff:
    
        staff1=staff2=staff3=None
        #add fixture to add roles to db
        @pytest.fixture(autouse=True, scope="function")
        def add_staff(self,db_setup,app,create_staff):
            self.url="/api/staffs/"
            self.db = db_setup
            self.app = app
            
        #test staff login
        def test_staff_login(self,client):
            post_data={"email": "TestEmail1"}
            response = client.post(self.url+"login",json=post_data)
            assert response.status_code==200,"response is "+str(response.status_code)

            res = response.json
            with self.app.app_context():
                staff = Staff.query.filter_by(email=post_data["email"]).first()
                assert res["id"] == staff.id
                assert res["first_name"] == staff.first_name
                assert res["last_name"] == staff.last_name
                assert res["department"] == staff.department
                assert res["email"] == staff.email
                assert res["user_type_id"] == staff.user_type_id
               