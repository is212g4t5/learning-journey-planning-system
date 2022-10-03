from util import post_testing, get_all_testing



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


