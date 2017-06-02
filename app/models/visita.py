from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time, DateTime
from sqlalchemy.orm import relationship
from base import Base
from vehiculo import Vehiculo
from visitante import Visitante
from seguridad import Seguridad
from destino import Destino
from dateutil.parser import parse
from datetime import datetime


class Visita(Base):
	__tablename__ = 'visita'
	id = Column(Integer, primary_key=True)
	origen = Column(String(50), nullable=False)
	razon = Column(String(300), nullable=True)
	fecha = Column(Date, nullable=False)
	hora_entrada = Column(Time, nullable=False)
	hora_salida = Column(Time, nullable=True)
	autorizada_por = Column(String(50), nullable=False)
	creado_en = Column(DateTime, default=datetime.now())
	modificado_en = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
	vehiculo_id = Column(ForeignKey('vehiculo.id'))
	visitante_id = Column(ForeignKey('visitante.id'), nullable=False)
	seguridad_id = Column(ForeignKey('seguridad.id'), nullable=False)
	destino_id = Column(ForeignKey('destino.id'), nullable=False)
	vehiculo = relationship(Vehiculo)
	visitante = relationship(Visitante)
	seguridad = relationship(Seguridad)
	destino = relationship(Destino)

	
	@property
	def serialize(self):
		hora_salida = self.hora_salida or self.hora_entrada
		return {
			"origen": self.origen, "destino": self.destino.empresa,
			"razon": self.razon, "fecha": str(self.fecha.strftime("%d/%m/%Y")),
			"hora_entrada": str(self.hora_entrada.strftime("%I:%M:%S %p")),
			"hora_salida": str(hora_salida.strftime("%I:%M:%S %p")), 
			"creado_en": str(self.creado_en.strftime("%d/%m/%Y %I:%M:%S %p")),
			"modificado_en": str(self.modificado_en.strftime("%d/%m/%Y %I:%M:%S %p")),
			"visitante_nombre": self.visitante.nombre, "visitante_identidad": self.visitante.identidad,
			"visitante_tipo_id": self.visitante.tipo_id, "visitante_apellido": self.visitante.apellido,
			"vehiculo_marca": self.vehiculo.marca, "vehiculo_tipo": self.vehiculo.tipo, 
			"vehiculo_placa": self.vehiculo.placa,"vehiculo_color": self.vehiculo.color, 
			"autorizada_por": self.autorizada_por, "seguridad_de_turno": self.seguridad.nombre
		}

