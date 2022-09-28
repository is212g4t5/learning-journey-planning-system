import requests
from models.RoleModel import Role
from schemas.RoleSchema import RoleSchema

role_schema = RoleSchema()

#API test create role
def test_create_role(app):
    role = Role("Test Role", "Test Description")
    assert role.active==True
    with app.app_context():
        response = requests.post("http://localhost:5000/api/roles", json=role_schema.jsonify(role).json)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["name"] == "Test Role"

#API test for get all roles
def test_get_all_roles():
    response = requests.get("http://localhost:5000/api/roles")
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == 1

