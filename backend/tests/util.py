import json
from request_handler import create_app



#umbrella function for post testing
def post_testing(test_client,url,test_data,key,value):
    #test sucessful posting 
    response = test_client.post(url,json=test_data) 
    assert response.status_code==201,str(response.status_code) +" == " +str(201) + "\nresponse is "+str(response.status_code)
    res = json.loads(response.data.decode('utf-8'))
    assert res[key] == value, str(res[key]) +" == " +str(value) + "\nres is "+str(res)
   
    #test bad request 400 for empty body
    response = test_client.post(url,json={})
    assert response.status_code==400, str(response.status_code) +" == " +str(400) + "\nresponse is "+str(response.status_code)
  
    #test bad request 400 for missing body
    response = test_client.post(url)
    assert response.status_code==400, str(response.status_code) +" == " +str(400) + "\nresponse is "+str(response.status_code)

#function for testing get ALL
def get_all_testing(test_client,url,length):
    response = test_client.get(url)
    assert response.status_code==200, str(response.status_code) +" == " +str(200) + "\nresponse is "+str(response.status_code)
    res = json.loads(response.data.decode('utf-8'))
    assert len(res)==length, str(len(res)) +" == " +str(length) + "\nres is "+str(res)

#function for testing get by ID
def get_id_testing(test_client,url,key,value):
    response = test_client.get(url)
    assert response.status_code==200,str(response.status_code) +" == " +str(200) + "\nresponse is "+str(response.status_code)
    res = json.loads(response.data.decode('utf-8'))
    assert res[key] == value, str(res[key]) +" == " +str(value) + "\nres is "+str(res)

#function for testing update(PUT) by ID
def post_testing(test_client,url,test_data,key,value):
    #test sucessful posting 
    response = test_client.post(url,json=test_data) 
    assert response.status_code==200,str(response.status_code) +" == " +str(200) + "\nresponse is "+str(response.status_code)
    res = json.loads(response.data.decode('utf-8'))
    assert res[key] == value, str(res[key]) +" == " +str(value) + "\nres is "+str(res)
   
    #test bad request 400 for empty body
    response = test_client.post(url,json={})
    assert response.status_code==400, str(response.status_code) +" == " +str(400) + "\nresponse is "+str(response.status_code)
  
    #test bad request 400 for missing body
    response = test_client.post(url)
    assert response.status_code==400, str(response.status_code) +" == " +str(400) + "\nresponse is "+str(response.status_code)
