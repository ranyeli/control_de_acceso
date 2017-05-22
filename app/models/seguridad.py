from sqlalchemy import Column, Integer, String
from base import Base


class Seguridad(Base):
	__tablename__ = 'seguridad'
	id = Column(Integer, primary_key=True)
	nombre = Column(String(50), nullable=False)


