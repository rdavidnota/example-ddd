from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from app.persistence.entities.models import Base

engine = create_engine('sqlite:///app.sqlite', echo=True)
Base.metadata.create_all(engine)

session = Session(engine)
