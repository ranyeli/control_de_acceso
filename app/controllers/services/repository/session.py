import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

settings = json.loads(os.environ['settings'])
engine = create_engine(settings["db"]["url"])
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

