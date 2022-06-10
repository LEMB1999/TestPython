
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

#check if ther user doesnt send a email when try to login
def test_login_without_email():
    data = {
        "password":"password"
    }

    response = requests.post("http://localhost:3000/login", json = data)
    assert response.json()["status"] == 400

#check if ther user doesnt send a password when try to login
def test_login_without_password():
    data = {
        "email":"mendezemmanuel1999@gmail.com",
    }

    response = requests.post("http://localhost:3000/login", json = data)
    assert response.json()["status"] == 400

#this test  check if the user not exist or the credentials are incorrect 
def test_login_bad_credentials():
    data = {
        "email":"mendezemmanuel1999@gmail.com",
        "password":"12345"
    }
    response = requests.post("http://localhost:3000/login", json = data)
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
    

#this test check the creation of users
def test_create_user():
    data = {
        "email":"angel1@gmail.com",
        "password":"12345678",
        "first_name":"angel",
        "last_name":"arce",
        "role":"admin",
        "photo":"http://foto.com"
    }
    response = request.post("http://localhost:3000/user", json = data)
    assert response.json()["status"] == 200


#this test check if user input a large info
def test_create_user_large_info():
    data = {
        "email":"angel2@gmail.com",
        "password":"12345678",
        "first_name":"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sollicitudin leo a diam porttitor posuere. Mauris pellentesque rutrum tellus, et molestie nibh. Praesent eros ante, lacinia at vulputate id, semper eu tortor. Duis sapien odio, maximus in viverra egestas, convallis vel dolor. Sed ac arcu metus. Donec sem neque, rhoncus vel aliquet vitae, laoreet in risus. In a feugiat sem, quis faucibus lorem. Sed sollicitudin molestie pulvinar. Curabitur imperdiet erat et euismod molestie. Aliquam sit amet massa est. Mauris volutpat hendrerit dui vel auctor. Integer ornare, neque id feugiat malesuada, arcu justo ultricies dui, id lacinia ipsum ipsum vitae quam. Etiam risus tellus, consequat in elit et, consectetur sodales erat.Etiam tortor leo, pharetra quis velit eu, iaculis fermentum neque. Pellentesque pellentesque lobortis massa vitae luctus. Duis vel mollis ligula. Nullam et orci luctus, egestas lectus dictum, commodo lectus. Fusce et suscipit neque. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Duis in efficitur lacus.
                     Pellentesque nec tortor sem. Phasellus vel viverra felis, ac venenatis felis. Praesent mattis feugiat dui, quis dignissim augue laoreet in. Vestibulum imperdiet, quam sed lacinia mattis, nulla risus eleifend risus, nec dictum nunc ipsum quis nibh. Curabitur lobortis viverra molestie. Nunc vel lacus sem. Donec at libero lectus. Curabitur elementum consectetur nulla, ut luctus odio facilisis et. Maecenas vel quam imperdiet, lacinia arcu ut, fermentum felis. Sed egestas elit vitae libero imperdiet, quis aliquam neque elementum. Curabitur nulla sem, gravida in tortor quis, venenatis iaculis magna. Pellentesque molestie commodo nibh.""",
        "last_name":"arce",
        "role":"admin",
        "photo":"http://foto.com"
    }
    response = request.post("http://localhost:3000/user", json = data)
    assert response.json()["status"] == 400 
    assert response.json()["message"] == "The first_name field only allows 255 characters"

#this test check if user pass an unknown field
def test_create_user_unknown_field():
    data = {
        "email":"angel1@gmail.com",
        "password":"12345678",
        "first_name":"angel",
        "last_name":"arce",
        "role":"admin",
        "photo":"http://foto.com",
        "test" : "discon"
    }
    response = request.post("http://localhost:3000/user", json = data)
    assert response.json()["status"] == 400
    assert response.json()["message"] == "The field test is not known"

#this test check if user pass string params 
def test_create_user_params_type():
    data = {
        "email":"angel3@gmail.com",
        "password":"12345678",
        "first_name":"Emma",
        "last_name":"arce",
        "role":"admin",
        "photo": 1
    }
    response = request.post("http://localhost:3000/user", json = data)
    assert response.json()["status"] == 400 
    assert response.json()["message"] == "The param photo its must be string"

#this test check if the user doesnt send a last name
def test_create_user_without_last_name():
    data = {
        "email":"angel4@gmail.com",
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
        "email":"angel5@gmail.com",
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
        "email":"angel6@gmail.com",
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
    assert response.json()["message"] == "The param email is required"

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
    
#this test check the action update for some user 
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
    assert response.json()["message"] == "The param email is required"

#this test check if user pass string params 
def test_udpate_user_params_type():
    data = {
        "email":"angel3@gmail.com",
        "password":"12345678",
        "first_name":"Emma",
        "last_name":"arce",
        "role":"admin",
        "photo": 1
    }
    response = request.put("http://localhost:3000/user/{0}".format(2), json = data)
    assert response.json()["status"] == 400 
    assert response.json()["message"] == "The param photo its must be string"

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