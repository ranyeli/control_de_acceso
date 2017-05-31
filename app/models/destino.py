from sqlalchemy import Column, Integer, String
from base import Base


class Destino(Base):
	__tablename__ = 'destino'
	id = Column(Integer, primary_key=True)
	empresa = Column(String(60), nullable=False)

	@property
	def serialize(self):
    		return {
				"destino": self.empresa,
				"destino_id": self.id
			}


