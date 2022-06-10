from sqlalchemy import create_engine
from models import *
from env import CONNECTION_URL_DATABASE

engine = create_engine(CONNECTION_URL_DATABASE)

#we define this method to drop all tables and then create to keep the new changes
def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    

recreate_database()