import sys
import os
import json
sys.path.append('../')
from sqlalchemy import create_engine
from models.base import Base
import models.visitante
import models.visita
import models.seguridad
import models.vehiculo

with open('../config.json') as json_data_file:
    data = json_data_file.read()

os.environ['settings'] = data;
settings = json.loads(os.environ['settings'])
engine = create_engine(settings["db"]["url"])
Base.metadata.create_all(engine)
