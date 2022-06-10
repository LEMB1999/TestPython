#import Environment Variables

import requests
from sqlalchemy.orm import Session 
from ..migration import *
from ..models import *
from sqlalchemy import create_engine
from flask_bcrypt import Bcrypt

request = requests.Session()
engine = create_engine("postgresql+psycopg2://postgres:IbFNAn1VCuTyBlP@localhost:3306/API_INFO")

#create the default user only for testing
with Session(engine) as conn:
    user = User(
                email = "mendezemmanuel1999@gmail.com",
                password = "$12$4/U9u8y6SirySnwxZKWnRu8d/NbfT97KEjkpYPxEqF2MIdoBmNEz.", # value --> password
                first_name = "Luis",
                last_name = "Mendez",
                photo = "http://fotos.com",
                role = "admin"
            )

    conn.add(user)
    conn.commit()

def login():
    
    data = {
        "email": "mendezemmanuel1999@gmail.com",
        "password": "password"
    }

    request.post("http://localhost:3000/login", json = data)

login()


def test_get_users():
    response = request.get("http://localhost:3000/users")
    assert response.json()["status"] == 200

def test_create_user():
    data = {
        "email":"angel@gmail.com",
        "password":"12345678",
        "first_name":"angel",
        "last_name":"arce",
        "role":"admin",
        "photo":"http://foto.com"
    }
    response = request.post("http://localhost:3000/user", json = data)
    assert response.json()["status"] == 200

def test_get_user():
    response = request.get("http://localhost:3000/user/{0}".format(2))
    assert response.json()["status"] == 200

def test_update_user():
    data = {
        "email":"angel_updated@gmail.com",
        "password":"12345678",
        "first_name":"angel",
        "last_name":"arce",
        "role":"admin",
        "photo":"http://foto.com"
    }
    response = request.put("http://localhost:3000/user/{0}".format(2), json = data)
    assert response.json()["status"] == 200

"""def test_delete_user():
    response = request.delete("http://localhost:3000/user/{0}".format(2))
    assert response.json()["status"] == 200"""
