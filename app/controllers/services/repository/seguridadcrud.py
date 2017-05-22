from session import session
from models.seguridad import Seguridad


def get_seguridad(seguridad_id):
    return session.query(Seguridad).filter(Seguridad.id == seguridad_id).one()


def get_all_seguridad():
    return session.query(Seguridad).order_by(Seguridad.id.desc()).all()
