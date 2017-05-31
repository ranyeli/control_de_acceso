from session import session
from models.destino import Destino


def get_destino(destino_id):
    return session.query(Destino).filter(Destino.id == destino_id).one()


def get_all_destinos():
    return session.query(Destino).order_by(Destino.id.desc()).all()
