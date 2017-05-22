from sqlalchemy import Column, Integer, String
from base import Base


class Vehiculo(Base):
	__tablename__ = 'vehiculo'
	id = Column(Integer, primary_key=True)
	#tipo = Column(String(40), nullable=False)
	descripcion = Column(String(250), nullable=False)


