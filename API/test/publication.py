#import Environment Variables

import requests
from sqlalchemy.orm import Session 

request = requests.Session()

#we need to login into the API to perform the requests and evaluate the response
def test_login():
    
    #this user was created when you execute the migration.py file
    data = {
        "email":"mendezemmanuel1999@gmail.com",
        "password":"password"
    }

    response = request.post("http://localhost:3000/login", json = data)
    assert response.json()["status"] == 200


#this test check the creation of users
def test_create_publication():
    data = {
        "title":"Publication 1",
        "description":"This is a test",
        "priority":"",
        "status":"",
        "published":""
    }
    response = request.post("http://localhost:3000/publication", json = data)
    assert response.json()["status"] == 200

#this test check if the user doesnt send a last name
def test_create_user_without_last_name():
    data = {
        "email":"angel2@gmail.com",
        "password":"12345678",
        "first_name":"angel",
        "role":"admin",
        "photo":"http://foto.com"
    }
    response = request.post("http://localhost:3000/user", json = data)
    assert response.json()["status"] == 200

#this test check if the user doesnt send a photo
def test_create_user_without_photo():
    data = {
        "email":"angel3@gmail.com",
        "password":"12345678",
        "first_name":"angel",
        "last_name":"arce",
        "role":"admin",
    }
    response = request.post("http://localhost:3000/user", json = data)
    assert response.json()["status"] == 200

#this test check if the user doesnt a last name and photo
def test_create_user_without_last_name_and_photo():
    data = {
        "email":"angel4@gmail.com",
        "password":"12345678",
        "first_name":"angel",
        "role":"admin",
    }
    response = request.post("http://localhost:3000/user", json = data)
    assert response.json()["status"] == 200

#this test check when user doesnt send a required param
def test_create_user_without_email():
    data = {
        "password":"12345678",
        "first_name":"angel",
        "role":"admin",
    }

    response = request.post("http://localhost:3000/user", json = data)
    assert response.json()["status"] == 400
    assert response.json()["message"] == "The params email,password,fist_name and role are required"

#this test check if user send a request and doesnt authenticated
def test_create_user_without_credentials():
    data = {
        "email":"angel@gmail.com",
        "password":"12345678",
        "first_name":"angel",
        "role":"admin",
    }
    response = requests.post("http://localhost:3000/user", json = data)
    assert response.json()["status"] == 401



#this test check the fetch of all users
def test_get_users():
    response = request.get("http://localhost:3000/users")
    assert response.json()["status"] == 200

#this test check if user send request to get user without credentials
def test_get_users_without_credentials():
    response = requests.get("http://localhost:3000/users")
    assert response.json()["status"] == 401
    assert response.json()["message"] == "Unauthorized request"
    


#this test check fetch specific user
def test_get_user():
    response = request.get("http://localhost:3000/user/{0}".format(2))
    assert response.json()["status"] == 200

#this test check fetch specific user and not found
def test_get_user_not_found():
    response = request.get("http://localhost:3000/user/{0}".format(100))
    assert response.json()["status"] == 400
    assert response.json()["message"] == "User not Found"

#this test check fetch specific user without credentials
def test_get_user_without_credentials():
    response = requests.get("http://localhost:3000/user/{0}".format(2))
    assert response.json()["status"] == 401
    assert response.json()["message"] == "Unauthorized request"
    

def test_update_user():
    data = {
        "email":"angel_1_updated@gmail.com",
        "password":"12345678",
        "first_name":"angel",
        "last_name":"arce",
        "role":"admin",
        "photo":"http://foto.com"
    }
    response = request.put("http://localhost:3000/user/{0}".format(2), json = data)
    assert response.json()["status"] == 200

def test_update_user():
    data = {
        "password":"12345678",
        "first_name":"angel",
        "last_name":"arce",
        "role":"admin",
        "photo":"http://foto.com"
    }
    response = request.put("http://localhost:3000/user/{0}".format(2), json = data)
    assert response.json()["status"] == 400
    assert response.json()["message"] == "The params email,password,fist_name and role are required"

def test_update_user_without_credentials():
    data = {
        "email":"angel_updated@gmail.com",
        "password":"12345678",
        "first_name":"angel",
        "last_name":"arce",
        "role":"admin",
        "photo":"http://foto.com"
    }
    response = requests.put("http://localhost:3000/user/{0}".format(2), json = data)
    assert response.json()["status"] == 401
    assert response.json()["message"] == "Unauthorized request"

def test_delete_user():
    response = request.delete("http://localhost:3000/user/{0}".format(2))
    assert response.json()["status"] == 200
    assert response.json()["message"] == "User was deleted"

def test_delete_user_without_credentials():
    response = requests.delete("http://localhost:3000/user/{0}".format(3))
    assert response.json()["status"] == 401
    assert response.json()["message"] == "Unauthorized request"

def logout():
    response = request.delete("http://localhost:3000/logout")
    assert response.json()["status"] == 200




def test_get_publications():
    pass

def test_get_publication():
    pass 

def test_create_publication():
    pass

def test_delete_publication():
    pass 

def test_update_publication():
    pass
