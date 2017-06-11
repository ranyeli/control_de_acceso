from session import session, DBSession
from models.vehiculo import Vehiculo


def get_vehiculo(vehiculo_id):
    vehiculo = session.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).one()
    DBSession.remove()
    return vehiculo


def get_all_vehiculos():
    vehiculos = session.query(Vehiculo).order_by(Vehiculo.id.desc()).all()
    DBSession.remove()
    return vehiculos
