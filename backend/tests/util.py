import requests

test_data={
        "name": "TestSkill1",
        "description": "TestSkill1",
        "active": true
        } 
url = domain+"/api/skills"

def test_post_api(url,test_data):
    response = requests.post(url,json=test_data)
    assert response.get("Code")==201

def test_get_all_api(url):
    response = requests.post(url,json=test_data)
    assert response.get("Code")==200

def test_get_id_api(url):
    response = requests.post(url,json=test_data)
    assert response.get("Code")==200