import json
from request_handler import create_app

#umbrella function for post testing
def post_testing(test_client,url,test_data,key,value):
    #test sucessful posting 
    response = test_client.post(url,json=test_data) 
    assert response.status_code==201,"response is "+str(response.status_code)
    res = json.loads(response.data.decode('utf-8'))
    assert res[key] == value,"returned value is incorrect"
    #test bad request 400 for missing body
    response = test_client.post(url,json={})
    assert response.status_code==400, "response is "+ str(response.status_code)
    #test bad request 400 for missing body
    response = test_client.post(url)
    assert response.status_code==400, "response is "+ str(response.status_code)

#function for testing get ALL
def get_all_testing(test_client,url,length):
    response = test_client.get(url)
    assert response.status_code==200,"response is "+str(response.status_code)
    res = json.loads(response.data.decode('utf-8'))
    assert len(res)==length, "res is "+str(res)

#function for testing get by ID
def get_id_testing(test_client,url,key,value):
    response = test_client.get(url)
    assert response.status_code==200,"response is "+str(response.status_code)
    res = json.loads(response.data.decode('utf-8'))
    assert res[key] == value,"returned value is incorrect"