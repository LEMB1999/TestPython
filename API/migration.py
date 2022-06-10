from sqlalchemy import create_engine
from models import *
from env import CONNECTION_URL_DATABASE
from sqlalchemy.orm import Session 
import bcrypt

engine = create_engine(CONNECTION_URL_DATABASE)

#we define this method to drop all tables and then create to keep the new changes
def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    #we need create a defaul user for testing
    #save the new user
    with Session(engine) as conn:
        #there is an issue problem when using Postgres as SGBD because Postgres automatically encode the password
        #so the problem is that when you try to check the password, the password be encoded two times
        #before saving the password decode it
        user = User(
            email = "mendezemmanuel1999@gmail.com",
            password = bcrypt.hashpw("password".encode("utf8"),bcrypt.gensalt()).decode("utf8"),
            first_name = "Luis",
            last_name = "Mendez",
            photo = "http://foto.com",
            role = "admin"
        )
        conn.add(user)
        conn.commit()
    
recreate_database()