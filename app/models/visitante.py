from sqlalchemy import Column, Integer, String
from base import Base


class Visitante(Base):
	__tablename__ = 'visitante'
	id = Column(Integer, primary_key=True)
	nombre = Column(String(40), nullable=False)
	cedula = Column(String(20), nullable=False)

	@property
	def serialize(self):
		return {
			'id':self.id, 
			'nombre':self.nombre, 
			'cedula':self.cedula
		}

