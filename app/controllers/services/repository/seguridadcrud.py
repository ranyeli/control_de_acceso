from session import session, DBSession
from models.seguridad import Seguridad


def get_seguridad(seguridad_id):
    seguridad = None
    try:
        seguridad = session.query(Seguridad).filter(Seguridad.id == seguridad_id).one()
    except:
        DBSession.rollback()
        seguridad = get_seguridad(seguridad_id)
    finally:
        DBSession.remove()
    return seguridad


def get_all_seguridad():
    oficiales = None
    try:
        oficiales = session.query(Seguridad).order_by(Seguridad.id.desc()).all()
    except:
        DBSession.rollback()
        oficiales = get_all_seguridad()
    finally:
        DBSession.remove()
    return oficiales
