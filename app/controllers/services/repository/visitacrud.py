from session import session
from models.visita import Visita
from models.visitante import Visitante
from models.seguridad import Seguridad
from sqlalchemy import text, func, or_, cast, Date, and_
from dateutil.parser import parse
from datetime import datetime
from generalcrud import insertdb


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
    hasta_fecha = "-".join(hasta_fecha.split("/")[::-1]) if hasta_fecha.strip() else str(datetime.now().date())

    desde_fecha = params.args.get('desde_fecha')
    desde_fecha = "-".join(desde_fecha.split("/")[::-1]) if desde_fecha.strip() else "1970-01-01"

    desde_hora = params.args.get('desde_hora')
    desde_hora = parse(desde_hora).time() if desde_hora else "00:00:01"

    hasta_hora = params.args.get('hasta_hora')
    hasta_hora = parse(hasta_hora).time() if hasta_hora else "23:59:59"

    buscar = params.args.get('search')

    buscar_por = params.args.get('buscarPor')
    buscar_por = buscar_por.strip().lower() if buscar_por else None

    print desde_fecha, hasta_fecha, desde_hora, hasta_hora
    total = session.query(func.count('*')).select_from(Visita).scalar()

    or_visitante = or_(Visitante.nombre.like("%{n}%".format(n=buscar)), 
    Visitante.identidad.like("%{i}%".format(i=buscar)))

    seguridad_turno = Seguridad.nombre.like("%{n}%".format(n=buscar))

    autoriza = Visita.autorizada_por.like("%{n}%".format(n=buscar))

    buscar_by = or_visitante

    buscar_by = autoriza if buscar_por == "autorizado por" else buscar_by

    buscar_by = seguridad_turno if buscar_por == "seguridad" else buscar_by

    print str(seguridad_turno), str(autoriza), buscar_por

    visitas = session.query(Visita).join(Visita.seguridad).join(Visita.visitante).\
    filter(and_(buscar_by, Visita.fecha.between(desde_fecha, hasta_fecha),
    and_(and_(Visita.hora_entrada.between(desde_hora, hasta_hora)), 
    and_(Visita.hora_salida.between(desde_hora, hasta_hora))))).\
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


