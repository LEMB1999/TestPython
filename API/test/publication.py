
import requests
from sqlalchemy.orm import Session 
from datetime import datetime

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


#this test check the creation of publication
def test_create_publication():
    data = {
        "title":"Publication 1",
        "description":"This is a test",
        "priority":"Medium",
        "status":"published",
        "published":datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),
    }
    response = request.post("http://localhost:3000/publication", json = data)
    assert response.json()["status"] == 200


#this test check if the user doesnt send a title
def test_create_user_without_title():
    data = {
        "description":"This is a test",
        "priority":"Medium",
        "status":"published",
        "published":datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    }
    response = request.post("http://localhost:3000/publication", json = data)
    assert response.json()["status"] == 400
    assert response.json()["message"] == "The param title is required"

#this test check if the user  send a incorrect status
def test_create_publication_with_incorrect_status():
    data = {
       "title":"Publication 2",
       "description":"This is a test",
       "priority":"Medium",
       "status":"unknown status",
       "published":datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    }
    status = [ "published", "pending", "deleted" ]
    response = request.post("http://localhost:3000/publication", json = data)
    assert response.json()["status"] == 400
    assert response.json()["message"] == "The values allowed for status are {0}".format(status)

#this test check if the user send a incorrect priority
def test_create_publication_with_incorrect_priority():
    data = {
       "title":"Publication 3",
       "description":"This is a test",
       "priority":"unknown priority",
       "status":"published",
       "published":datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    }
    
    priority = [ "High", "Medium", "Low" ]
    response = request.post("http://localhost:3000/publication", json = data)
    assert response.json()["status"] == 400
    assert response.json()["message"] == "The values allowed for priority are {0}".format(priority)


#this test check if user send a request and doesnt authenticated
def test_create_publication_without_credentials():
    data = {
        "title":"Publication 1",
        "description":"This is a test",
        "priority":"Medium",
        "status":"published",
        "published":datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    }
    response = requests.post("http://localhost:3000/publication", json = data)
    assert response.json()["status"] == 401
    assert response.json()["message"] == "Please login to continue with the process"


#this test check the fetch of all publications
def test_get_publications():
    response = request.get("http://localhost:3000/publications")
    assert response.json()["status"] == 200


#this test check if user send request to get publication without credentials
def test_get_publications_without_credentials():
    response = requests.get("http://localhost:3000/publications")
    assert response.json()["status"] == 401
    assert response.json()["message"] == "Please login to continue with the process"

#this test check fetch specific publication
def test_get_publication():
    response = request.get("http://localhost:3000/publication/{0}".format(1))
    assert response.json()["status"] == 200

#this test check fetch specific publication and not found
def test_get_publication_not_found():
    response = request.get("http://localhost:3000/publication/{0}".format(100))
    assert response.json()["status"] == 400
    assert response.json()["message"] == "Publication not Found"

#this test check fetch specific publication without credentials
def test_get_publication_without_credentials():
    response = requests.get("http://localhost:3000/publication/{0}".format(1))
    assert response.json()["status"] == 401
    assert response.json()["message"] == "Please login to continue with the process"
    
#this test validate the updated of the publication
def test_update_publication():
    data = {
        "title":"Publication updated",
        "description":"This is a test",
        "priority":"Medium",
        "status":"published",
        "published":datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),
    }
    response = request.put("http://localhost:3000/publication/{0}".format(1), json = data)
    assert response.json()["status"] == 200

#this test validate when user not send a required params to update  a publication
def test_update_publication():
    
    data = {
        "description":"This is a test",
        "priority":"Medium",
        "status":"published",
        "published":datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),
    }

    response = request.put("http://localhost:3000/publication/{0}".format(2), json = data)
    assert response.json()["status"] == 400
    assert response.json()["message"] == "The param title is required"

#this  test validate when user try to update a publication but is not loggin
def test_update_user_without_credentials():
    data = {
        "title":"Publication 10",
        "description":"This is a test",
        "priority":"Medium",
        "status":"published",
        "published":datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),
    }
    response = requests.put("http://localhost:3000/publication/{0}".format(1), json = data)
    assert response.json()["status"] == 401
    assert response.json()["message"] == "Please login to continue with the process"

#this test validate when user try to delete a some publication
def test_delete_publication():
    response = request.delete("http://localhost:3000/publication/{0}".format(1))
    assert response.json()["status"] == 200
    assert response.json()["message"] == "Publication was deleted"

#this test validate when user try to delete a some publication but is not loggin
def test_delete_publication_without_credentials():
    response = requests.delete("http://localhost:3000/publication/{0}".format(2))
    assert response.json()["status"] == 401
    assert response.json()["message"] == "Please login to continue with the process"

