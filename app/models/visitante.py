from sqlalchemy import Column, Integer, String
from base import Base


class Visitante(Base):
	__tablename__ = 'visitante'
	id = Column(Integer, primary_key=True)
	nombre = Column(String(40), nullable=False)
	apellido = Column(String(40), nullable=True)
	identidad = Column(String(40), nullable=False)
	tipo_id = Column(String(40), nullable=False)

	@property
	def serialize(self):
		return {
			'id':self.id, 
			'nombre':self.nombre,
			'apellido':self.apellido,
			'identidad':self.identidad,
			'tipo_id':self.tipo_id
		}

