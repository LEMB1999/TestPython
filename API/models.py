#In this file we define all models that we use in the API_REST
#we use sqlalchemy like orm to perfom querys to database

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey ,Integer, String, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

#we use this class that represent a table in database to execute queries
class Publication(Base):
    #we declare the name of the table for this model
    __tablename__ = 'publications'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(String)
    status = Column(String)
    published = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    #we use a foreign key to represent the relationship between the two tables
    id_user = Column(Integer, ForeignKey("users.id"))

    #we define this method to return a representation of an instance of model
    def serialize(self):
        return {"title":self.title, "description":self.description, "priority":self.priority, "status": self.status }


class User(Base):
    #we declare the name of the table for this model
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String ,unique=True)
    password = Column(String)
    role = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    photo = Column(String)
    publication = relationship("Publication")

    #we define this method to return a representation of an instance of model
    def serialize(self):
        return {"email": self.email , "first_name": self.first_name , "last_name": self.last_name }

