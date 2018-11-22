from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Integer, Column, String, and_
from sqlalchemy import MetaData

meta = MetaData()

@as_declarative()
class Base(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


class Customer(Base):
    name = Column(String)
