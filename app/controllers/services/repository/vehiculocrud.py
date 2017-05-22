from session import session
from models.vehiculo import Vehiculo


def get_vehiculo(vehiculo_id):
    return session.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).one()


def get_all_vehiculos():
    return session.query(Vehiculo).order_by(Vehiculo.id.desc()).all()
