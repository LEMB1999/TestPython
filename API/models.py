from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey ,Integer, String, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

class Publication(Base):
    __tablename__ = 'publications'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(String)
    status = Column(String)
    published = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    id_user = Column(Integer, ForeignKey("users.id"))

    def serialize(self):
        return {"title":self.title, "description":self.description, "priority":self.priority, "status": self.status }


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    role = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    photo = Column(String)
    publication = relationship("Publication")

    def serialize(self):
        return {"email": self.email , "first_name": self.first_name , "last_name": self.last_name }

