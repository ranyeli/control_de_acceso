from session import session, DBSession
from models.destino import Destino


def get_destino(destino_id):
    destino = None
    try:
        destino = session.query(Destino).filter(Destino.id == destino_id).one()
    except:
        DBSession.rollback()
        destino = get_destino(destino_id)
    finally:
        DBSession.remove()
    return destino


def get_all_destinos():
    destinos = None
    try:
        destinos = session.query(Destino).order_by(Destino.id.desc()).all()
    except:
        DBSession.rollback()
        destinos = get_all_destinos()
    finally:
        DBSession.remove()
    return destinos
