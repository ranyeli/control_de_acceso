from sqlalchemy import Column, Integer, String
from base import Base


class Vehiculo(Base):
	__tablename__ = 'vehiculo'
	id = Column(Integer, primary_key=True)
	marca = Column(String(40), nullable=False)
	tipo = Column(String(40), nullable=False)
	placa = Column(String(30), nullable=False)
	color = Column(String(25), nullable=False)


