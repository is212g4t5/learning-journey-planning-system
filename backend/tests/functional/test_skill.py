import requests


domain = "http://localhost:5000"

def test_create_skill():
    test_data={
        "name": "TestSkill2",
        "description": "TestSkill2",
        "active": True
        } 
    url = domain+"/api/skills"
    response = requests.post(url,json=test_data)
    assert response.status_code==201

def test_get_skills():
    url = domain+"/api/skills"
    response = requests.get(url)
    assert response.status_code==200


    

