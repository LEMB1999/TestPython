from sqlalchemy import create_engine
from models import *

engine = create_engine('postgresql+psycopg2://postgres:IbFNAn1VCuTyBlP@localhost:3306/API_INFO')


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

recreate_database()