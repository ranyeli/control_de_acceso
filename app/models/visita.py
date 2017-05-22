from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base
from vehiculo import Vehiculo
from visitante import Visitante
from seguridad import Seguridad
from dateutil.parser import parse 


class Visita(Base):
	__tablename__ = 'visita'
	id = Column(Integer, primary_key=True)
	origen = Column(String(50), nullable=False)
	destino = Column(String(50), nullable=False)
	razon = Column(String(500), nullable=True)
	fecha_visita = Column(String(50), nullable=False)
	hora_visita = Column(String(50), nullable=False)
	fecha_evento = Column(String(50), nullable=False)
	vehiculo_id = Column(ForeignKey('vehiculo.id'))
	visitante_id = Column(ForeignKey('visitante.id'), nullable=False)
	seguridad_id = Column(ForeignKey('seguridad.id'), nullable=False)
	vehiculo = relationship(Vehiculo)
	visitante = relationship(Visitante)
	seguridad = relationship(Seguridad)
	
	@property
	def serialize(self):
		return {
			"origen": self.origen, "destino": self.destino,
			"razon": self.razon, "fecha": self.fecha_visita,
			"hora": self.hora_visita, 
			"fecha_evento": parse(self.fecha_evento).strftime("%d/%m/%Y %I:%M:%S %p"),
			"visitante": self.visitante.nombre, 
			"vehiculo": self.vehiculo.descripcion,
			"autorizada_por": self.seguridad.nombre
		}

