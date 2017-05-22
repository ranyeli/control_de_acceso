from datetime import datetime
from repository.generalcrud import *
from models.seguridad import Seguridad
from models.visita import Visita
from models.vehiculo import Vehiculo
from models.visitante import Visitante


def save_visita(request):
	f = request.form
	
	visitante = Visitante()
	visitante.nombre = f['visitanteNombre']
	visitante.cedula = f['visitanteCedula']
	insertdb(visitante)
	
	seguridad = Seguridad()
	seguridad.nombre = f['visitaAutorizada']
	insertdb(seguridad)
	
	vehiculo = Vehiculo()
	vehiculo.descripcion = f['vehiculoDesc']
	insertdb(vehiculo)
	
	visita = Visita()
	visita.origen = f['visitaOrigen']
	visita.destino = f['visitaDestino']
	visita.razon = f['visitaRazon']
	visita.fecha_visita = f['visitaFecha']
	visita.hora_visita = f['visitaHora']
	visita.fecha_evento = datetime.now()
	visita.seguridad_id = seguridad.id
	visita.vehiculo_id = vehiculo.id
	visita.visitante_id = visitante.id
	insertdb(visita)


