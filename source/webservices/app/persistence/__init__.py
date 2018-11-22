from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from app.persistence.entities.models import Base
from config import DATABASE

uri_database = ""

if DATABASE['engine'] == 'sqlite':
    uri_database = 'sqlite:///' + DATABASE['database'] + '.sqlite'
elif DATABASE['engine'] == 'mysql':
    uri_database = 'mysql+pymysql://' + DATABASE['username'] + ':' + DATABASE['password'] + '@' + DATABASE[
        'host'] + ':' + DATABASE['port'] + '/' + DATABASE['database'] + ''

engine = create_engine(uri_database)

Base.metadata.create_all(engine)

session = Session(engine)
