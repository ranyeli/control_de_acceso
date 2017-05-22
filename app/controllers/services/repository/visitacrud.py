from session import session
from models.visita import Visita
from sqlalchemy import text


#def get_visita(visita_id):
#    return session.query(Visita).filter(Visita.id == Visita_id).one()


#def get_visitas(cvvgvcx, hasta):
#    return session.query(Visita).order_by(Visita.fecha.asc())\
#		.filter(Visita.fecha_visita >= desde and Visita.fecha_visita <= hasta).all()
		
#def filter_visita(tables, conditions):
#	sql = text('select {tables} from {consitions}'\
#		.format(tables=tables, conditions=conditions))
#	return db.engine.execute(sql)
	
	
def get_all_visitas():
    return session.query(Visita).order_by(Visita.id.desc()).all()
