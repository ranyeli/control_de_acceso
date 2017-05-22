from session import session
from models.visitante import Visitante


def get_visitante(visitante_id):
    return session.query(Visitante).filter(Visitante.id == visitante_id).one()


def get_all_visitante():
    return session.query(Visitante).order_by(Visitante.id.desc()).all()
