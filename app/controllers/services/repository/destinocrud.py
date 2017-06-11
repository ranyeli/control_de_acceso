from session import session, DBSession
from models.destino import Destino


def get_destino(destino_id):
    destino = session.query(Destino).filter(Destino.id == destino_id).one()
    DBSession.remove()
    return destino


def get_all_destinos():
    destinos = session.query(Destino).order_by(Destino.id.desc()).all()
    DBSession.remove()
    return destinos
