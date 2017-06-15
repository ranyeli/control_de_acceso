from session import session, DBSession
from models.vehiculo import Vehiculo


def get_vehiculo(vehiculo_id):
    vehiculo = None
    try:
        vehiculo = session.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).one()
    except:
        DBSession.rollback()
        vehiculo = get_vehiculo(vehiculo_id)
    finally:
        DBSession.remove()
    return vehiculo


def get_all_vehiculos():
    vehiculos = None
    try:
        vehiculos = session.query(Vehiculo).order_by(Vehiculo.id.desc()).all()
    except:
        DBSession.rollback()
        vehiculos = get_all_vehiculos()
    finally:
        DBSession.remove()
    return vehiculos
