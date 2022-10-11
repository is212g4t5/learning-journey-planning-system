from util import post_testing, get_all_testing
import json



test_data={
        "name": "TestSkill1",
        "description": "TestSkill1",
        "active": True
        } 
url="/api/skills/"

def test_post_skills(test_post_client):
    post_testing(test_post_client,url,test_data,"name","TestSkill1")

    
def test_get_skills(test_get_client):
    get_all_testing(test_get_client,url,3)

def test_update_skill_by_id(test_get_client):
    put_data={
        "name": "TestUpdatedSkill1",
        "description": "TestUpdatedDesc",
        "active": False
        } 
    fail_data={
        "name": "TestSkill2",
        "description": "TestUpdatedDesc",
        "active": True
        } 
    response = test_get_client.put(url+"1",json=put_data)
    assert response.status_code==200,"response is "+str(response.status_code)
    res = json.loads(response.data.decode('utf-8'))
    for key,value in put_data.items():
        assert res[key] == value, str(res[key]) +" == " +str(value) + "\nres is "+str(res)
    
    #test bad request 400 for empty body
    response = test_get_client.put(url,json={})
    assert response.status_code==405, str(response.status_code) +" == " +str(400) + "\nresponse is "+str(response.status_code)
  
    #test bad request 400 for missing body
    response = test_get_client.put(url)
    assert response.status_code==405, str(response.status_code) +" == " +str(400) + "\nresponse is "+str(response.status_code)

    #test unique name clash
    response = test_get_client.put(url+"1",json=fail_data)
    assert response.status_code==400,"response is "+str(response.status_code)



def test_delete_skill_by_id(test_get_client):
    response = test_get_client.delete(url+"2")
    assert response.status_code==200,"response is "+str(response.status_code)
    res = json.loads(response.data.decode('utf-8'))
    assert res["active"] == False, str(res["active"]) +" == " +str(False) + "\nres is "+str(res)
    


