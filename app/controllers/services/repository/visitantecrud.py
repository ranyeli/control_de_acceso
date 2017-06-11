from session import session, DBSession
from models.visitante import Visitante


def get_visitante(visitante_id):
    visitante = session.query(Visitante).filter(Visitante.id == visitante_id).one()
    DBSession.remove()
    return visitante


def get_all_visitante():
    visitantes =  session.query(Visitante).order_by(Visitante.id.desc()).all()
    DBSession.remove()
    return visitantes
