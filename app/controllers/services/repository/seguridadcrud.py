from session import session, DBSession
from models.seguridad import Seguridad


def get_seguridad(seguridad_id):
    seguridad = session.query(Seguridad).filter(Seguridad.id == seguridad_id).one()
    DBSession.remove()
    return seguridad


def get_all_seguridad():
    oficiales = session.query(Seguridad).order_by(Seguridad.id.desc()).all()
    DBSession.remove()
    return oficiales
