from session import session
from models.visita import Visita
from models.visitante import Visitante
from sqlalchemy import text, func, or_, cast, Date, and_
from dateutil.parser import parse
from datetime import datetime
from generalcrud import *


#def get_visita(visita_id):
#    return session.query(Visita).filter(Visita.id == Visita_id).one()


#def get_visitas(cvvgvcx, hasta):
#    return session.query(Visita).order_by(Visita.fecha.asc())\
#		.filter(Visita.fecha_visita >= desde and Visita.fecha_visita <= hasta).all()
		
#def filter_visita(tables, conditions):
#	sql = text('select {tables} from {consitions}'\
#		.format(tables=tables, conditions=conditions))
#	return db.engine.execute(sql)
	
	
def get_all_visitas(params):
    offset = int(params.args.get('offset'))
    limit = int(params.args.get('limit'))

    hasta_fecha = params.args.get('hasta_fecha')
    hasta_fecha = "-".join(hasta_fecha.split("/")[::-1]) if hasta_fecha.strip() else None

    desde_fecha = params.args.get('desde_fecha')
    desde_fecha = "-".join(desde_fecha.split("/")[::-1]) if desde_fecha.strip() else None
    #if desde_fecha.strip():
    #    d,m,a = desde_fecha.split("/")
    #    desde_fecha = parse("{a}-{m}-{d}".format(a=a,m=m,d=d))
    #else:
    #    desde_fecha = None

    desde_hora = params.args.get('desde_hora')
    desde_hora = parse(desde_hora).time() if desde_hora else None

    hasta_hora = params.args.get('hasta_hora')
    hasta_hora = parse(hasta_hora).time() if hasta_hora else None

    buscar = params.args.get('buscar')

    buscar_por = params.args.get('buscar_por')

    print desde_fecha, hasta_fecha, desde_hora, hasta_hora
    total = session.query(func.count('*')).select_from(Visita).scalar()

    # visitas = session.query(Visita).\
    # filter(or_(Visita.visitante.has(cedula=buscar),
    # Visita.visitante.has(nombre=buscar))).order_by(Visita.id.desc()).\
    # offset(offset).limit(limit).all()

    visitas = session.query(Visita).join(Visita.visitante).\
    filter(or_(Visitante.nombre.like("%{n}%".format(n=buscar)), 
    Visitante.identidad.like("%{c}%".format(c=buscar)),
    Visita.fecha.between(desde_fecha, hasta_fecha))).\
    order_by(Visita.id.desc()).\
    offset(offset).limit(limit).all()
    return {"total": total, "rows": visitas}

def get_visita_reciente(tipo_id, identidad):
    visita = session.query(Visita).join(Visita.visitante).\
    filter( Visitante.tipo_id == tipo_id, Visitante.identidad == identidad ).\
    order_by(Visita.id.desc()).first();
    return visita

def actualizar_hora_salida(args):
    tipo_id = args.form['visitanteIdTipo']
    identidad = args.form['visitanteIdentidad']
    hora_salida = parse(args.form['visitaHora']).time()

    visita = session.query(Visita).join(Visita.visitante).\
    filter( Visitante.tipo_id == tipo_id, Visitante.identidad == identidad ).\
    order_by(Visita.id.desc()).first();

    visita.hora_salida = hora_salida
    insertdb(visita)


